from fastapi import FastAPI, UploadFile, File, Form
from agents.job_search import search_jobs
from agents.cover_letter import generate_cover
from agents.ats_agent import ats_score
from agents.recommender import get_top_jobs,rank_jobs   # ✅ FIXED NAME

import PyPDF2
import io
import docx

app = FastAPI()


# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def home():
    return {"message": "AI Job Hunter 🚀"}


# =========================
# RESUME ANALYSIS + AI JOB RECOMMENDER
# =========================
@app.post("/analyze_resume/")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(default="")
):

    content = await file.read()
    text = ""

    filename = file.filename.lower()

    try:
        # ---------------- PDF ----------------
        if filename.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(content))
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        # ---------------- DOCX ----------------
        elif filename.endswith(".docx"):
            doc = docx.Document(io.BytesIO(content))
            for para in doc.paragraphs:
                text += para.text + " "

        # ---------------- TXT ----------------
        else:
            text = content.decode("utf-8", errors="ignore")

    except Exception as e:
        return {
            "error": "File parsing failed",
            "details": str(e)
        }

    text = text.strip()

    # =========================
    # ATS ENGINE
    # =========================
    ats = ats_score(text, job_description)

    # =========================
    # SMART JOB KEYWORD (DYNAMIC)
    # =========================
    # extract simple intent from resume
    lower_text = text.lower()

    if "data" in lower_text or "pandas" in lower_text:
        keyword = "data scientist"
    elif "ai" in lower_text or "ml" in lower_text or "machine learning" in lower_text:
        keyword = "ai engineer"
    elif "backend" in lower_text or "fastapi" in lower_text:
        keyword = "backend developer"
    else:
        keyword = "software developer"

    # =========================
    # JOB SEARCH
    # =========================
    jobs = search_jobs(keyword)

    # safety fallback
    if not jobs:
        jobs = []

    # =========================
    # AI RANKING (TOP 5 JOBS)
    # =========================
    top_jobs = get_top_jobs(text, jobs, top_k=5)

    return {
        "keyword_used": keyword,
        "ats_score": ats.get("ats_score", 0),
        "skills": ats.get("matched_keywords", []),
        "missing": ats.get("missing_keywords", []),
        "tips": ats.get("tips", []),
        "recommended_jobs": top_jobs
    }


# =========================
# JOB SEARCH (RAW API)
# =========================
@app.get("/jobs/{keyword}")
def jobs(keyword: str):
    return search_jobs(keyword)


# =========================
# COVER LETTER GENERATOR
# =========================
@app.post("/cover/")
def cover(job: str, skills: str):
    return {
        "cover_letter": generate_cover(job, skills)
    }