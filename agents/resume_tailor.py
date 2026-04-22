from models.hf_model import generator

def tailor_resume(job_desc,resume):

    prompt = f"""
    Improve this resume according to job:

    Job:
    {job_desc}

    Resume:
    {resume}
    """

    output = generator(prompt,max_length=300)

    return output[0]["generated_text"]