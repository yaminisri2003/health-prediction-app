import os

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def fallback_prediction(
    glucose,
    haemoglobin,
    cholesterol
):
    if glucose > 125:
        return "High risk of Diabetes"

    elif cholesterol > 240:
        return "High Cholesterol Risk"

    elif haemoglobin < 12:
        return "Possible Anaemia Risk"

    else:
        return "Healthy"


def predict_health(
    glucose,
    haemoglobin,
    cholesterol
):

    try:

        prompt = f"""
You are a healthcare assistant.

Patient Blood Test Results:

Glucose: {glucose}
Haemoglobin: {haemoglobin}
Cholesterol: {cholesterol}

Provide:
1. Short health assessment
2. Possible risks
3. Recommendation

Keep the response under 40 words.
Return only a concise health remark.
Do not use headings such as Health Assessment, Risks, or Recommendation.
Write as a single short paragraph.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print(f"Gemini Error: {e}")

        return fallback_prediction(
            glucose,
            haemoglobin,
            cholesterol
        )