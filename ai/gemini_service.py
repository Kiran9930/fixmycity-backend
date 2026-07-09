import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key="AQ.Ab8RN6JMTkYxCWl0Zf0DngIcdJCVFmt1H-fFgaa1j7GCQ1Dfww")
model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_issue(description):

    prompt = f"""
You are an AI assistant for a civic issue reporting platform.

Analyze the civic issue described below.

Issue:
{description}

Return ONLY valid JSON.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"ERROR: {e}"