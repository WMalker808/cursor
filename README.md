# Guardian Style Guide

A searchable web application for the Guardian newspaper's style guide, featuring full-text search, alphabetical browsing, style-check functionality, and person-name verification powered by spaCy NER and Wikipedia.

## Features

- **Search**: Full-text search across all style guide entries
- **Browse**: Alphabetical navigation through entries
- **Style Check**: Paste text to find matching style guide entries
- **Name Check**: Extract person names from text using NLP and verify spelling via Wikipedia

## Setup

### Requirements

- Python 3.11+
- pip

### Installation

```bash
pip install -r requirements.txt
```

### Running Locally

```bash
python name_server.py
```

The app will be available at `http://localhost:5001`.

## Deployment

Configured for Render deployment via `render.yaml`. Uses gunicorn as the WSGI server.

## Project Structure

- `index.html` — Frontend single-page application
- `name_server.py` — Flask backend with spaCy NER for name extraction
- `style_guide_data.js` — Pre-processed style guide data for the frontend
- `guardian_style_guide.md` — Full Guardian style guide in Markdown
- `render.yaml` — Render deployment configuration
- `requirements.txt` — Python dependencies
