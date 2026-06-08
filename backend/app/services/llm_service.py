import json
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


def analyze_resume(resume_text: str) -> dict:
    prompt = f"""
You are an AI career coach for software engineering job seekers.

Analyze the resume text and return ONLY valid JSON.
Do not include markdown.
Do not include explanations outside JSON.

JSON format:
{{
  "candidate_summary": "...",
  "technical_skills": ["..."],
  "strengths": ["..."],
  "missing_skills": ["..."],
  "career_suggestions": ["..."]
}}

Resume text:
{resume_text}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a professional AI career coach. Return only valid JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "raw_analysis": content,
            "warning": "The LLM response was not valid JSON."
        }