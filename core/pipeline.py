# pipeline 

# core functions
from core.cleaner import clean_article
from core.summarizer import summarize_with_model
from core.categorizer import categorize_with_model
from core.entity import extract_entities

import uuid
from datetime import datetime


def process_article(raw_article: dict) -> dict:
    """
        GEMINI BASED PIPELINE
    """
    try:
        # step 1 - clean text
        cleaned_text = clean_article(raw_article["content"])
        # step 2 - summarize
        summary = summarize_with_model(cleaned_text)
        # step 3 - categorize
        category = categorize_with_model(summary)
        # step 4 - entities
        entities = extract_entities(summary)

        return {
            "id": str(uuid.uuid4()),
            "title": raw_article["title"],
            "url": raw_article["url"],
            "published_at": raw_article.get("published_at", datetime.utcnow().isoformat()),
            "summary": summary,
            "category": category,
            "entities": entities,
            "source": raw_article.get("source"),
        }

    except Exception as e:
        print(f"[pipeline] error processing article {e}")
        return None
