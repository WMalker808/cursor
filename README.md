# Local File Browser — Web Interface

A lightweight web application that lets you browse, preview, and download local files through a modern browser-based interface. Built with Python and Flask.

## Features

- **Browse directories** — navigate your local filesystem with a clean, dark-themed UI
- **Preview files** — view text files with syntax-highlighted line numbers directly in the browser
- **Image preview** — inline rendering of common image formats (PNG, JPG, GIF, SVG, WebP)
- **Download files** — download any file to your machine with one click
- **Search** — find files by name with real-time results
- **Path safety** — all access is restricted to a configurable root directory

## Quick Start

```bash
pip install -r requirements.txt
python3 app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

## Configuration

| Environment Variable | Default | Description |
|---|---|---|
| `FILE_BROWSER_ROOT` | `~` (home directory) | Root directory for file browsing |
| `PORT` | `5000` | HTTP port |
| `FLASK_DEBUG` | `0` | Set to `1` for auto-reload during development |

### Examples

Browse the current project directory:

```bash
FILE_BROWSER_ROOT=. python3 app.py
```

Browse `/var/log` on port 8080:

```bash
FILE_BROWSER_ROOT=/var/log PORT=8080 python3 app.py
```

## API Endpoints

| Method | Path | Query Params | Description |
|---|---|---|---|
| GET | `/` | — | Serves the web interface |
| GET | `/api/browse` | `path` (relative) | List directory contents |
| GET | `/api/file` | `path` (relative) | Get file metadata and text preview |
| GET | `/api/download` | `path` (relative) | Download a file |
| GET | `/api/search` | `q`, `path`, `limit` | Search files by name |

## Security

- All paths are resolved and validated to stay within the configured `FILE_BROWSER_ROOT`.
- Symlink targets outside the root are blocked.
- This tool is designed for **local development use**. Do not expose it to the public internet without additional authentication and hardening.
