import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_issue(description):

    prompt = f"""
You are an AI assistant for a civic issue reporting platform.

Analyze the civic issue described below.

Issue:
{description}

Your task:
1. Identify the issue category.
2. Estimate the severity.
3. Suggest the responsible government department.
4. Estimate your confidence.

IMPORTANT:
- Return ONLY a valid JSON object.
- Do NOT use markdown.
- Do NOT write ```json.
- Do NOT write explanations.
- Do NOT add extra text.

Format:

{{
  "category": "Pothole",
  "severity": "High",
  "department": "PWD",
  "confidence": "96%"
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()