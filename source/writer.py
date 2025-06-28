# core/utils.py

import json
import os

def append_article_to_file(article: dict, path: str = "data/news_store.json"):
    try:
        # Ensure the directory exists
        dir_path = os.path.dirname(path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        data = []

        # Try reading existing data
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        data = json.loads(content)
                        if not isinstance(data, list):
                            print(f"[writer] Warning: Expected a list, got {type(data)}. Resetting.")
                            data = []
            except json.JSONDecodeError:
                print(f"[writer] Warning: {path} contains invalid JSON. Resetting.")
                data = []
            except Exception as read_err:
                print(f"[writer] Error reading {path}: {read_err}")
                data = []

        # Append the new article
        data.append(article)

        # Write the updated list back to file
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"[writer] Appended article: {article.get('title', 'Untitled')}")

    except Exception as e:
        print(f"[writer] Error appending to {path}: {e}")
