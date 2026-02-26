#!/usr/bin/env python3
"""Lightweight Flask server that uses spaCy NER to extract person names from text."""

import os
import re
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import spacy

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
CORS(app)

nlp = spacy.load("en_core_web_sm")

TITLES = {
    "mr", "mrs", "ms", "dr", "prof", "sir", "dame", "lord", "lady",
    "rev", "sgt", "cpl", "lt", "capt", "maj", "col", "gen", "cmdr",
    "supt", "det", "insp", "judge", "justice", "baron", "baroness",
    "prince", "princess", "king", "queen", "president", "senator",
    "governor", "mayor", "councillor", "minister", "secretary",
    "cardinal", "archbishop", "bishop", "father", "sister", "brother",
    "sheikh", "imam", "rabbi", "ayatollah",
}


def preceding_word(text, start):
    """Get the word immediately before position `start` in text."""
    before = text[:start].rstrip()
    m = re.search(r'(\S+)$', before)
    return m.group(1).rstrip(".,;:") if m else ""


def has_possessive(ent_text, text, end):
    """Check if the entity contains or is followed by 's (possessive)."""
    # Possessive may be inside the entity span (spaCy sometimes includes it)
    if re.search(r"['\u2019]s$", ent_text):
        return True
    # Or immediately after
    rest = text[end:]
    return rest.startswith("\u2019s") or rest.startswith("'s")


def is_likely_person(ent, text):
    """Heuristics for non-PERSON entities that may actually be people."""
    # Already labelled PERSON
    if ent.label_ == "PERSON":
        return True

    name = ent.text.strip()
    if not name:
        return False

    # Preceded by a personal title (e.g. "Prince Philip")
    prev = preceding_word(text, ent.start_char).lower()
    if prev in TITLES:
        return True

    # Possessive usage ("Mountbatten-Windsor's life") — strong person signal
    # for entities that aren't obviously organisations/places
    if has_possessive(ent.text, text, ent.end_char) and ent.label_ not in ("ORG", "GPE", "FAC", "NORP", "EVENT"):
        return True

    return False


def expand_with_title(text, start):
    """If the word before `start` is a title, return the expanded start position."""
    prev = preceding_word(text, start)
    if prev.lower() in TITLES:
        # Find where this title actually starts in the text
        before = text[:start].rstrip()
        return before.rfind(prev)
    return start


@app.route("/extract-names", methods=["POST"])
def extract_names():
    data = request.get_json()
    text = data.get("text", "")
    if not text.strip():
        return jsonify({"names": []})

    doc = nlp(text)

    by_name = {}
    for ent in doc.ents:
        if not is_likely_person(ent, text):
            continue

        # Expand span to include preceding title if present
        start = expand_with_title(text, ent.start_char)
        end = ent.end_char
        name = text[start:end].strip()

        # Clean up trailing possessives that spaCy may have included
        name = re.sub(r"['\u2019]s$", "", name).strip()

        if not name:
            continue
        if name not in by_name:
            by_name[name] = {"name": name, "positions": []}
        by_name[name]["positions"].append({"start": start, "end": end})

    return jsonify({"names": list(by_name.values())})


@app.route("/")
def serve_index():
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/style_guide_data.js")
def serve_style_data():
    return send_from_directory(BASE_DIR, "style_guide_data.js")


@app.route("/guardian_style_guide.md")
def serve_style_guide():
    return send_from_directory(BASE_DIR, "guardian_style_guide.md")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    print(f"Name extraction server running on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port)
