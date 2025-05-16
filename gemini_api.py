import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env from the same folder as this file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

GENAI_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GENAI_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")

def generate_response(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text.strip()