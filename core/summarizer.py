import os
from dotenv import load_dotenv

from google import genai

load_dotenv()

def summarize_with_model(text: str) -> str:
    prompt = (
        "Summarize the following news article in 3-5 sentences, keeping it neutral and concise:\n\n"
        f"{text}"
    )
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        return response.text.strip()
    except Exception as e:
        print(f"[summarizer] Error {e}")
        return