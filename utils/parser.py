import re

def extract_skills(text):
    skills = []

    keywords = [
        "python","sql","machine learning",
        "deep learning","nlp","fastapi",
        "pandas","tensorflow","pytorch"
    ]

    text = text.lower()

    for skill in keywords:
        if skill in text:
            skills.append(skill)

    return skills