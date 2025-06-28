import os
from dotenv import load_dotenv

from google import genai

load_dotenv()

CATEGORIES = ["Politics", "Technology", "Health", "Business", "Sports", "Entertainment", "Science", "World", "Other"]

def categorize_with_model(summary: str) -> str:
    prompt = (
        "Given the following news summary, classify it into one of the following categories:\n"
        f"{', '.join(CATEGORIES)}.\n\n"
        f"Summary:\n{summary}\n\n"
        "Respond with only the category name."
    )
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        category = response.text.strip()

        # Normalize and validate
        if category not in CATEGORIES:
            return "Other"
        return category

    except Exception as e:
        print(f"[categorizer] Error {e}")
    return "Other"
