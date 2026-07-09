import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_issue(description):
    try:
        prompt = f"""
You are an AI assistant for a civic issue reporting platform.

Analyze the civic issue described below.

Issue:
{description}

Return ONLY valid JSON.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"ERROR: {str(e)}"