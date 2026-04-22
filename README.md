# 🚀 AI Job Hunter Pro

An AI-powered full-stack career assistant that helps users analyze resumes, match jobs, and generate cover letters using Machine Learning and NLP.

---

## ✨ Features

### 📄 Resume Intelligence
- ATS Score calculation
- Skill extraction from resume
- Missing skill detection
- AI improvement suggestions

### 🔎 Smart Job Matching
- Real-time job search using API
- AI-based job ranking system
- Semantic matching using embeddings
- Personalized job recommendations

### ✍️ Cover Letter Generator
- AI-generated professional cover letters
- Context-aware writing
- Clean and structured output

### 📊 AI Ranking Engine
- Hybrid scoring (keyword + semantic similarity)
- Smart filtering of irrelevant jobs
- Resume-job alignment score

---

## 🧠 Tech Stack

### Backend
- FastAPI
- Python
- HuggingFace Transformers
- SentenceTransformers
- Scikit-learn

### Frontend
- Streamlit
- Custom CSS (SaaS UI)

### APIs
- JSearch API (RapidAPI)

---

## 🏗️ Architecture

Resume Upload → FastAPI Backend → AI Processing Engine  
↓  
ATS Scoring + NLP Matching  
↓  
Job API + Ranking System  
↓  
Streamlit Frontend Dashboard  

---

## 📂 Project Structure

AI_JOB_HUNTER/
│
├── app.py
├── frontend.py
├── database.py
├── requirements.txt
│
├── agents/
│   ├── ats_agent.py
│   ├── job_search.py
│   ├── cover_letter.py
│   ├── recommender.py
│   ├── resume_tailor.py
│   ├── alert_agent.py
│
├── models/
│   ├── hf_model.py
│
├── utils/
│   ├── matcher.py
│   ├── parser.py

---

## 🚀 How to Run

### 1. Clone Repository
git clone https://github.com/YOUR_USERNAME/AI-Job-Hunter.git
cd AI-Job-Hunter

---

### 2. Install Dependencies
pip install -r requirements.txt

---

### 3. Run Backend
uvicorn app:app --reload

---

### 4. Run Frontend
streamlit run frontend.py

---

## 🔐 Environment Variables

Create a .env file:

RAPIDAPI_KEY=your_api_key_here

---

## 💡 Key Highlights

- AI Resume Analyzer with ATS scoring
- Smart Job Recommendation system
- NLP-based matching engine
- Cover Letter Generator
- Full-stack AI project

---

## 📈 Future Improvements

- AI Interview Bot
- Resume Builder
- LinkedIn Optimizer
- Email job alerts
- Authentication system

---

## 👨‍💻 Author

Feeza Khan  
AI/ML Engineer | GenAI Developer | Full Stack AI Projects

---

## ⭐ Support

If you like this project, give it a star ⭐ on GitHub
