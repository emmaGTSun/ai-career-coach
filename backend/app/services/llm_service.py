import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
base_url = os.getenv("DEEPSEEK_BASE_URL", "").strip()
MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat").strip()

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)


def analyze_resume(resume_text: str) -> str:
    prompt = f"""
You are an AI career coach for software engineering job seekers.

Analyze the following resume text and return a concise career analysis.

Please include:
1. Candidate summary
2. Technical skills
3. Strengths
4. Missing skills
5. Career improvement suggestions

Resume text:
{resume_text}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a professional AI career coach."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content