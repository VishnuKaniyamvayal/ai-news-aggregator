import os
from dotenv import load_dotenv
import json

from google import genai
import re as re

load_dotenv()

def extract_entities(summary: str) -> str:
    prompt = (
        "Extract the named entities from the following news summary. "
        "Return them as a JSON object with the keys: people, organizations, locations, dates, and events. "
        "Only include relevant values. Do NOT include any explanation or comments.\n\n"
        f"Summary:\n{summary}"
    )
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        json_match = re.search(r'\{[\s\S]*\}', response.text.strip())
        if json_match:
            return json.loads(json_match.group())
        print(f"[ner] Unexpected response format:\n{response.text.strip()}")
        return {
            "people": [],
            "organizations": [],
            "locations": [],
            "dates": [],
            "events": []
        }
    except Exception as e:
        print(f"[entity] Error {e}")
        return {
            "people": [],
            "organizations": [],
            "locations": [],
            "dates": [],
            "events": []
        }
    