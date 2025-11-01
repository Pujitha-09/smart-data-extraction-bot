import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# =========================================================
# STEP 1 — SMART SCRAPER
# =========================================================
def scrape_data(url):
    """
    Extracts readable paragraph content from a given URL.
    Handles both static and JavaScript-rendered pages.
    """
    html = None

    try:
        # Try JS-render for dynamic sites
        session = HTMLSession()
        r = session.get(url)
        r.html.render(timeout=25, sleep=3)
        html = r.html.html
        session.close()
        print("✅ Dynamic render success")
    except Exception as e:
        print(f"[⚠️ Dynamic render failed] {e}")

    if not html:
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            html = requests.get(url, headers=headers, timeout=20).text
            print("✅ Fallback static fetch success")
        except Exception as e:
            print(f"[❌ Fetch error] {e}")
            return pd.DataFrame([{"text": "Failed to fetch page.", "link": url}])

    soup = BeautifulSoup(html, "html.parser")
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
    clean_text = " ".join(paragraphs).replace("\n", " ").strip()

    if not clean_text:
        clean_text = "No meaningful content extracted — site may be protected or empty."

    return pd.DataFrame([{"text": clean_text[:12000], "link": url}])


# =========================================================
# STEP 2 — SUMMARIZER (Professional + Concise)
# =========================================================
def generate_summary(df, style="Professional"):
    """
    Generates an AI-powered summary using Hugging Face hosted models.
    Supports 'Professional' and 'Concise' styles only.
    """
    token = os.getenv("HF_API_TOKEN")
    if not token:
        return "⚠️ Missing Hugging Face API token. Add HF_API_TOKEN in your .env file."

    # Model selection
    if style == "Concise":
        model_name = "facebook/bart-large-cnn"
    else:
        model_name = "facebook/bart-large-xsum"

    client = InferenceClient(model=model_name, token=token)

    text = "\n".join(df["text"].tolist()).replace("\n", " ").strip()
    if not text or len(text) < 200:
        return "⚠️ Extracted text too short to summarize."

    # --- Auto-chunking for long text ---
    max_chunk_size = 3500
    chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    summaries = []

    print(f"🧠 Summarizing with {model_name} ({len(chunks)} chunk{'s' if len(chunks) > 1 else ''})")

    try:
        for chunk in chunks:
            response = client.summarization(
                chunk,
                parameters={
                    "max_new_tokens": 180,
                    "min_length": 40,
                    "temperature": 0.7,
                    "do_sample": False,
                },
            )

            if isinstance(response, list):
                summary_text = response[0].get("summary_text", "")
            elif isinstance(response, dict):
                summary_text = response.get("summary_text", "")
            else:
                summary_text = str(response)

            summaries.append(summary_text.strip())

        final_summary = " ".join(summaries).strip()
        return final_summary or "⚠️ Model returned empty summary."

    except Exception as e:
        return f"⚠️ Hugging Face API error: {e}"
