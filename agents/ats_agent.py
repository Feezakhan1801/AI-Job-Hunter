import re


def clean_keywords(text):
    text = text.lower()

    # remove junk words (VERY IMPORTANT FIX)
    noise_words = {
        "the", "and", "or", "a", "an", "to", "for", "of", "in",
        "on", "with", "we", "you", "is", "are", "will", "be",
        "should", "must", "role", "responsibilities",
        "qualification", "preferred", "candidate", "looking",
        "experience", "job", "overview", "skills", "good",
        "strong", "knowledge", "ability", "field"
    }

    words = re.findall(r"[a-zA-Z+#.]+", text)

    return set([w for w in words if len(w) > 2 and w not in noise_words])


def ats_score(resume_text: str, job_description: str):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    tips = []

    # ---------------------------
    # KEYWORD EXTRACTION
    # ---------------------------
    resume_keywords = clean_keywords(resume_text)
    job_keywords = clean_keywords(job_description)

    matched = resume_keywords & job_keywords
    missing = job_keywords - resume_keywords

    # ---------------------------
    # SAFE SCORE START (IMPORTANT FIX)
    # ---------------------------
    score = 40  # base score so it NEVER becomes 0

    # ---------------------------
    # MATCH SCORE
    # ---------------------------
    if len(job_keywords) > 0:
        match_score = (len(matched) / len(job_keywords)) * 100
    else:
        match_score = 50

    score += match_score * 0.6

    # ---------------------------
    # PENALTY FOR MISSING
    # ---------------------------
    if missing:
        tips.append("Missing important skills: " + ", ".join(list(missing)[:10]))
        score -= len(missing) * 0.5  # reduced penalty (important fix)

    # ---------------------------
    # PROJECT CHECK
    # ---------------------------
    if len(re.findall(r"project", resume_text)) >= 2:
        score += 8
    else:
        tips.append("Add 2–3 strong projects")

    # ---------------------------
    # EXPERIENCE CHECK
    # ---------------------------
    if "intern" in resume_text or "experience" in resume_text:
        score += 5
    else:
        tips.append("Add internship or experience section")

    # ---------------------------
    # IMPACT VERBS
    # ---------------------------
    verbs = ["built", "developed", "implemented", "designed", "deployed", "optimized"]
    verb_count = sum(1 for v in verbs if v in resume_text)

    score += min(verb_count * 2, 10)

    if verb_count < 3:
        tips.append("Use impact verbs like built, developed, deployed")

    # ---------------------------
    # FINAL FIX (VERY IMPORTANT)
    # ---------------------------
    final_score = max(10, min(round(score, 2), 100))

    # ---------------------------
    # FEEDBACK
    # ---------------------------
    if final_score >= 85:
        tips.append("🔥 Excellent ATS match")
    elif final_score >= 70:
        tips.append("✅ Good match, minor improvements needed")
    else:
        tips.append("⚠️ Improve alignment with job description")

    return {
        "ats_score": final_score,
        "matched_keywords": list(matched),
        "missing_keywords": list(missing),
        "tips": list(set(tips))
    }