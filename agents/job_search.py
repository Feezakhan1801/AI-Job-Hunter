'''import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def search_jobs(keyword):
    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
        "query": keyword,
        "page": "1",
        "num_pages": "1",
        "date_posted": "today"
    }

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        data = response.json()

        jobs = []

        for job in data.get("data", []):
            jobs.append({
                "title": job.get("job_title", "N/A"),
                "company": job.get("employer_name", "N/A"),
                "location": job.get("job_city", "Remote"),
                "link": job.get("job_apply_link", "#"),
                "type": job.get("job_employment_type", "N/A")
            })

        return jobs

    except Exception as e:
        return [{
            "title": "Error",
            "company": str(e),
            "location": "",
            "link": "#",
            "type": ""
        }]
'''
import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def search_jobs(keyword):

    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
        "query": keyword,
        "page": "1",
        "num_pages": "2"
    }

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        data = response.json()

        jobs = []

        for job in data.get("data", []):

            jobs.append({
                "title": job.get("job_title", "N/A"),
                "company": job.get("employer_name", "N/A"),
                "location": job.get("job_city", "Remote"),
                "link": job.get("job_apply_link", "#"),
                "type": job.get("job_employment_type", "N/A"),
                "description": job.get("job_description", "")[:500]
            })

        return jobs

    except Exception as e:
        return []