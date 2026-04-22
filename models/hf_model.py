from transformers import pipeline
from sentence_transformers import SentenceTransformer

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-large"
)

embedder = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

