import streamlit as st
import requests

backend = "http://127.0.0.1:8000"

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Job Hunter",
    page_icon="🚀",
    layout="wide"
)

# =========================
# SESSION STATE (NEW - NAVIGATION)
# =========================
if "page" not in st.session_state:
    st.session_state.page = "home"

# =========================
# GLOBAL CSS (UPGRADED SaaS UI)
# =========================
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top, #0b1220, #020617);
    color: white;
    font-family: "Inter", sans-serif;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0b1220;
    border-right: 1px solid rgba(255,255,255,0.06);
}

/* Title */
.title {
    font-size: 40px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 25px;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(14px);
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 15px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.35);
    transition: 0.25s;
}

.card:hover {
    transform: translateY(-4px);
    border: 1px solid rgba(56,189,248,0.6);
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    color: white;
    border-radius: 12px;
    padding: 10px 18px;
    font-weight: 600;
}

/* Inputs */
.stTextInput input,
.stTextArea textarea {
    background: rgba(255,255,255,0.05);
    color: white;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* Metrics */
[data-testid="stMetricValue"] {
    color: #38bdf8;
    font-weight: 800;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR (SLACK STYLE NAV)
# =========================
st.sidebar.markdown("""
<div style="font-size:22px; font-weight:800; color:#38bdf8;">
🚀 AI Job Hunter 
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### ⚡ Navigation")

if st.sidebar.button("🏠 Dashboard"):
    st.session_state.page = "home"

if st.sidebar.button("📄 Resume Analyzer"):
    st.session_state.page = "resume"

if st.sidebar.button("🔎 Job Search"):
    st.session_state.page = "jobs"

if st.sidebar.button("✍️ Cover Letter"):
    st.session_state.page = "cover"

st.sidebar.markdown("---")
st.sidebar.markdown("💡 AI Career Assistant")

# =========================
# 🏠 DASHBOARD HOME PAGE
# =========================
if st.session_state.page == "home":

    st.markdown('<div class="title">AI Job Hunter Pro</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI Resume Analyzer • Smart Job Matching • Cover Letter Generator</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>📄 Resume Intelligence</h3>
            <p>AI analyzes resume & gives ATS score</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🔎 Job Matching</h3>
            <p>Smart AI-ranked job recommendations</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>✍️ Cover Letters</h3>
            <p>Auto-generated professional letters</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Start Resume Analysis"):
            st.session_state.page = "resume"

    with col2:
        if st.button("Find Jobs"):
            st.session_state.page = "jobs"

    with col3:
        if st.button("Generate Cover Letter"):
            st.session_state.page = "cover"

    st.stop()

# =========================
# 📄 RESUME ANALYZER
# =========================
if st.session_state.page == "resume":

    st.markdown("## 📄 Upload Resume")

    col1, col2 = st.columns([1, 1])

    with col1:
        file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])

    with col2:
        jd = st.text_area("Paste Job Description (Optional)", height=200)

    if file:

        with st.spinner("🧠 AI analyzing your resume..."):

            res = requests.post(
                f"{backend}/analyze_resume/",
                files={"file": (file.name, file.getvalue())},
                data={"job_description": jd}
            )

            data = res.json()

        st.success("Analysis Complete 🚀")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.metric("🎯 ATS Score", f"{data['ats_score']}/100")
            st.progress(int(data["ats_score"]))
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.metric("🧠 Skills Found", len(data["skills"]))
            st.write(data["skills"])
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.metric("❌ Missing Skills", len(data["missing"]))
            st.write(data["missing"])
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("## 💡 AI Tips")

        for tip in data["tips"]:
            st.markdown(f"""<div class="card">⚡ {tip}</div>""", unsafe_allow_html=True)

        st.markdown("## 🏆 Recommended Jobs")

        jobs = data.get("recommended_jobs", [])

        for job in jobs:
            st.markdown(f"""
            <div class="card">
                <h3>💼 {job['title']}</h3>
                <p>🏢 {job['company']}</p>
                <p>📍 {job['location']}</p>
                <p>⭐ {job['score']}</p>
                <a href="{job['link']}" target="_blank">🚀 Apply Now</a>
            </div>
            """, unsafe_allow_html=True)

# =========================
# 🔎 JOB SEARCH
# =========================
elif st.session_state.page == "jobs":

    st.markdown("## 🔎 Search Jobs")

    keyword = st.text_input("Enter Role")

    if st.button("Search"):

        res = requests.get(f"{backend}/jobs/{keyword}")
        jobs = res.json()

        for job in jobs:
            st.markdown(f"""
            <div class="card">
                <h3>💼 {job['title']}</h3>
                <p>🏢 {job['company']}</p>
                <p>📍 {job['location']}</p>
                <a href="{job['link']}" target="_blank">Apply</a>
            </div>
            """, unsafe_allow_html=True)

# =========================
# ✍️ COVER LETTER
# =========================
else:

    st.markdown("## ✍️ Cover Letter AI")

    job = st.text_input("Job Title")
    skills = st.text_area("Skills")

    if st.button("Generate"):

        res = requests.post(
            f"{backend}/cover/",
            params={"job": job, "skills": skills}
        )

        output = res.json()["cover_letter"]

        st.markdown(f"""
        <div class="card">
            {output}
        </div>
        """, unsafe_allow_html=True)