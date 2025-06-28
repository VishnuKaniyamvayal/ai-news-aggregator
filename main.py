from source.fetcher import fetch_articles
from core.pipeline import process_article
from source.writer import append_article_to_file
import json

if __name__ == "__main__":
    data = fetch_articles()
    articles = []
    for d in data:
        processed_article = process_article(d)
        if processed_article:
            append_article_to_file(process_article)
            print("Wrote article to file")