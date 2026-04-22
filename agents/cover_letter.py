from models.hf_model import generator


def generate_cover(job, skills):
    prompt = f"""
Write a professional cover letter.

RULES:
- Do NOT invent jobs, companies, or experience
- Do NOT add fake history
- Only use provided skills
- Keep it realistic for a fresher
- Must be 3 paragraphs only

INPUT:
Job Title: {job}
Skills: {skills}

FORMAT:

Dear Hiring Manager,

I am excited to apply for the position of {job}.I am eager to begin my professional journey in this field and contribute my knowledge to your organization.

I have hands-on knowledge of {skills}. Through academic learning and self-projects, I have developed problem-solving ability and technical understanding relevant to this role.

I am eager to contribute and learn in a professional environment. Thank you for considering my application.

Return only the cover letter.
"""

    result = generator(
    prompt,
    max_new_tokens=200,
    do_sample=False,   # 🔥 VERY IMPORTANT (remove hallucination)
    num_beams=5,       # better structure
    early_stopping=True,
    repetition_penalty=2.0,
)

    text = result[0]["generated_text"]

    return post_process(text)


def post_process(text):
    text = text.strip()

    # remove prompt leakage if any
    if "Dear Hiring Manager" in text:
        text = text.split("Dear Hiring Manager")[-1]
        text = "Dear Hiring Manager" + text

    # word limit safety
    words = text.split()
    if len(words) < 80:
        text += "\n\nI am eager to contribute to your team with dedication and consistency."

    return text
    

'''
from models.hf_model import generator

def generate_cover(job, skills):

    prompt = f"""
Write professional cover letter for fresher.

Job Title: {job}
Skills: {skills}

3 paragraph only.
"""

    result = generator(
        prompt,
        max_new_tokens=220,
        do_sample=False
    )

    return result[0]["generated_text"]

'''