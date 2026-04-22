from sklearn.metrics.pairwise import cosine_similarity
from models.hf_model import embedder

def match_score(resume_text, job_text):

    emb1 = embedder.encode([resume_text])
    emb2 = embedder.encode([job_text])

    score = cosine_similarity(emb1, emb2)[0][0]

    return round(score*100,2)