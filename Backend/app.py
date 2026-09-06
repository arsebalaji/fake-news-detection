import json
import os
import re
from pathlib import Path

import requests
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS


ROOT_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = ROOT_DIR / "Frontend"


def load_local_env():
    """Load simple KEY=VALUE entries without requiring a dotenv package."""
    env_file = ROOT_DIR / ".env"
    if not env_file.exists():
        return

    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"\''))


load_local_env()

app = Flask(__name__)
CORS(app)


def local_detection(text):
    """Provide a useful local result when no external model is configured."""
    normalized_text = text.lower()
    suspicious_terms = (
        "shocking",
        "you won't believe",
        "miracle cure",
        "secret they don't want you to know",
        "100% guaranteed",
        "breaking!!!",
    )
    matches = [term for term in suspicious_terms if term in normalized_text]
    exclamation_count = text.count("!")
    sensational_score = min(100, len(matches) * 24 + max(0, exclamation_count - 1) * 8)
    prediction = "FAKE" if sensational_score >= 50 else "REAL"
    credibility_signals = sum(
        indicator in normalized_text
        for indicator in ("according to", "official", "report", "data", "study", "research")
    )
    has_date_or_number = bool(re.search(r"\b(?:19|20)\d{2}\b|\b\d+(?:\.\d+)?%?\b", text))
    evidence_score = min(25, credibility_signals * 5 + (5 if has_date_or_number else 0))
    if prediction == "FAKE":
        confidence = max(51, min(98, 50 + sensational_score // 2))
    else:
        confidence = max(55, min(92, 55 + evidence_score + min(10, len(text) // 120)))

    if prediction == "FAKE":
        reason = "The text uses sensational language or unsupported certainty. Verify it against reputable sources before sharing."
    elif credibility_signals or has_date_or_number:
        reason = "The article uses measured wording and includes attribution or specific details, which are positive credibility signals."
    else:
        reason = "No sensational-language signals were detected, but the source should still be checked before sharing."

    return {
        "prediction": prediction,
        "confidence": confidence,
        "reason": reason,
    }


def openrouter_detection(text, api_key):
    prompt = (
        "Classify the following news text as FAKE or REAL based on the writing and "
        "evidence signals in the text. Use REAL for neutral, specific, attributed, "
        "and plausibly reported text, even when the text cannot be independently "
        "fact-checked. Use FAKE only when the text contains clear sensationalism, "
        "unsupported certainty, fabricated-looking claims, or strong contradiction "
        "inside the article. Do not label a neutral article FAKE merely because it "
        "mentions a date, number, future event, or a topic you cannot verify. Return "
        "only valid JSON with exactly these keys: prediction (FAKE or REAL), "
        "confidence (integer 0-100), reason (one concise sentence). Confidence must describe how certain you are "
        "about the prediction you selected. Do not claim certainty. Do not use your "
        "training-data date or an assumed current date to decide whether a claim is "
        "real; judge only the text and its evidence, and acknowledge when it cannot "
        "be verified from the text alone.\n\nNews text:\n" + text
    )
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:5000",
            "X-Title": "TruthGuard AI",
        },
        json={
            "model": os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini"),
            "temperature": 0,
            "messages": [
                {"role": "system", "content": "You are a careful news-literacy assistant."},
                {"role": "user", "content": prompt},
            ],
        },
        timeout=30,
    )
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"]
    content = re.sub(r"^```(?:json)?\s*|\s*```$", "", content.strip())
    result = json.loads(content)
    prediction = str(result.get("prediction", "")).upper()
    if prediction not in {"FAKE", "REAL"}:
        raise ValueError("Model returned an invalid prediction")
    model_confidence = max(0, min(100, int(result.get("confidence", 0))))
    confidence = max(51, min(98, model_confidence))
    return {
        "prediction": prediction,
        "confidence": confidence,
        "reason": str(result.get("reason", "No explanation was returned.")),
    }


@app.get("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.get("/<path:filename>")
def frontend_file(filename):
    return send_from_directory(FRONTEND_DIR, filename)


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "provider": "openrouter" if configured_api_key() else "local"})


def configured_api_key():
    api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
    return api_key if api_key and api_key != "YOUR_NEW_API_KEY" else None


@app.post("/api/detect")
def detect():
    payload = request.get_json(silent=True) or {}
    text = str(payload.get("news", "")).strip()
    if len(text) < 10:
        return jsonify({"error": "Please enter at least 10 characters of news text."}), 400

    api_key = configured_api_key()
    try:
        result = openrouter_detection(text, api_key) if api_key else local_detection(text)
        return jsonify(result)
    except (requests.RequestException, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        app.logger.warning("External detection failed: %s", error)
        return jsonify({"error": "The AI service could not analyze this article. Please try again."}), 502


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=True)