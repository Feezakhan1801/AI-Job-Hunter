from utils.matcher import match_score
from agents.ats_agent import clean_keywords

def rank_jobs(resume_text, jobs):

    ranked_jobs = []

    resume_keywords = clean_keywords(resume_text)

    for job in jobs:

        job_text = f"{job['title']} {job['company']} {job.get('description','')}"

        # -------------------------
        # 1. Semantic similarity
        # -------------------------
        similarity = match_score(resume_text, job_text)

        # -------------------------
        # 2. Keyword overlap score
        # -------------------------
        job_keywords = clean_keywords(job_text)

        if len(job_keywords) > 0:
            keyword_score = len(resume_keywords & job_keywords) / len(job_keywords) * 100
        else:
            keyword_score = 0

        # -------------------------
        # FINAL SCORE (HYBRID AI)
        # -------------------------
        final_score = (similarity * 0.6) + (keyword_score * 0.4)

        job["score"] = round(final_score, 2)

        ranked_jobs.append(job)

    # sort best first
    ranked_jobs.sort(key=lambda x: x["score"], reverse=True)

    return ranked_jobs


def get_top_jobs(resume_text, jobs, top_k=5):

    ranked = rank_jobs(resume_text, jobs)

    # smart filtering (remove bad matches)
    filtered = [j for j in ranked if j["score"] > 30]

    return filtered[:top_k]