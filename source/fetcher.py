# core/fetcher.py

import feedparser
from typing import List, Dict
import json

# Path to your source config
SOURCE_PATH = "data/sources.json"

def load_sources() -> List[str]:
    """Load RSS source URLs from the sources.json file."""
    try:
        with open(SOURCE_PATH, "r") as f:
            sources = json.load(f)
        return sources.get("rss", [])
    except Exception as e:
        print(f"[fetcher] Error loading sources: {e}")
        return []

def fetch_articles() -> List[Dict]:
    """Fetch and parse articles from RSS sources."""
    articles = []
    sources = load_sources()

    for url in sources:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                articles.append({
                    "title": entry.get("title"),
                    "link": entry.get("link"),
                    "published": entry.get("published", ""),
                    "summary": entry.get("summary", ""),  # fallback if no full content
                    "content": entry.get("content", [{"value": entry.get("summary", "")}])[0]["value"]
                })
        except Exception as e:
            print(f"[fetcher] Failed to parse {url}: {e}")
    
    return articles
