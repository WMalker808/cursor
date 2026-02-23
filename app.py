import os
import mimetypes
import stat
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, request, send_file, abort, render_template

app = Flask(__name__)

DEFAULT_ROOT = os.path.expanduser("~")
ALLOWED_ROOT = os.environ.get("FILE_BROWSER_ROOT", DEFAULT_ROOT)


def _safe_resolve(requested_path: str) -> Path:
    """Resolve *requested_path* and ensure it stays within ALLOWED_ROOT."""
    root = Path(ALLOWED_ROOT).resolve()
    target = (root / requested_path).resolve()
    if not str(target).startswith(str(root)):
        abort(403, description="Access denied: path is outside the allowed root.")
    return target


def _file_info(path: Path) -> dict:
    """Return metadata dict for a single filesystem entry."""
    try:
        st = path.stat()
    except (PermissionError, OSError):
        return {
            "name": path.name,
            "path": str(path),
            "type": "unknown",
            "error": "Permission denied",
        }

    is_dir = stat.S_ISDIR(st.st_mode)
    is_link = path.is_symlink()

    info = {
        "name": path.name,
        "path": str(path),
        "relative_path": str(path.relative_to(Path(ALLOWED_ROOT).resolve())),
        "type": "directory" if is_dir else "file",
        "size": st.st_size,
        "size_human": _human_size(st.st_size),
        "modified": datetime.fromtimestamp(st.st_mtime).isoformat(),
        "is_symlink": is_link,
    }

    if not is_dir:
        mime, _ = mimetypes.guess_type(path.name)
        info["mime_type"] = mime or "application/octet-stream"
        info["extension"] = path.suffix.lower()

    return info


def _human_size(nbytes: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if abs(nbytes) < 1024:
            return f"{nbytes:.1f} {unit}"
        nbytes /= 1024
    return f"{nbytes:.1f} PB"


TEXT_EXTENSIONS = {
    ".txt", ".md", ".py", ".js", ".ts", ".tsx", ".jsx", ".html", ".css",
    ".json", ".xml", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf",
    ".sh", ".bash", ".zsh", ".fish", ".bat", ".cmd", ".ps1",
    ".c", ".cpp", ".h", ".hpp", ".java", ".go", ".rs", ".rb", ".php",
    ".sql", ".r", ".m", ".swift", ".kt", ".scala", ".lua", ".pl",
    ".csv", ".tsv", ".log", ".env", ".gitignore", ".dockerignore",
    ".makefile", ".cmake", ".dockerfile",
    "", # extensionless files like Makefile, Dockerfile
}

MAX_PREVIEW_SIZE = 1_000_000  # 1 MB


def _is_text_file(path: Path) -> bool:
    if path.suffix.lower() in TEXT_EXTENSIONS:
        return True
    if path.name.lower() in {"makefile", "dockerfile", "vagrantfile", "gemfile", "rakefile", "license"}:
        return True
    mime, _ = mimetypes.guess_type(path.name)
    return mime is not None and mime.startswith("text/")


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/browse")
def browse():
    """List directory contents. Query param: ?path=relative/path"""
    rel = request.args.get("path", ".")
    target = _safe_resolve(rel)

    if not target.exists():
        abort(404, description="Path not found.")
    if not target.is_dir():
        abort(400, description="Path is not a directory.")

    try:
        entries = sorted(target.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except PermissionError:
        abort(403, description="Permission denied.")

    items = [_file_info(e) for e in entries]

    parent = None
    root = Path(ALLOWED_ROOT).resolve()
    if target != root:
        parent = str(target.parent.relative_to(root))

    return jsonify({
        "current": str(target),
        "relative": str(target.relative_to(root)),
        "parent": parent,
        "root": str(root),
        "items": items,
    })


@app.route("/api/file")
def file_content():
    """Return file contents. Query param: ?path=relative/path"""
    rel = request.args.get("path", "")
    if not rel:
        abort(400, description="path parameter is required.")

    target = _safe_resolve(rel)

    if not target.exists():
        abort(404, description="File not found.")
    if not target.is_file():
        abort(400, description="Path is not a file.")

    info = _file_info(target)

    if _is_text_file(target) and target.stat().st_size <= MAX_PREVIEW_SIZE:
        try:
            content = target.read_text(errors="replace")
        except PermissionError:
            abort(403, description="Permission denied.")
        info["content"] = content
        info["preview_type"] = "text"
    else:
        info["preview_type"] = "binary"

    return jsonify(info)


@app.route("/api/download")
def download():
    """Download a file. Query param: ?path=relative/path"""
    rel = request.args.get("path", "")
    if not rel:
        abort(400, description="path parameter is required.")

    target = _safe_resolve(rel)

    if not target.exists():
        abort(404, description="File not found.")
    if not target.is_file():
        abort(400, description="Path is not a file.")

    return send_file(target, as_attachment=True)


@app.route("/api/search")
def search():
    """Search for files by name. Query params: ?q=query&path=relative/start"""
    query = request.args.get("q", "").lower()
    if not query:
        abort(400, description="q parameter is required.")

    rel = request.args.get("path", ".")
    target = _safe_resolve(rel)
    limit = min(int(request.args.get("limit", 100)), 500)

    results = []
    try:
        for item in target.rglob("*"):
            if query in item.name.lower():
                results.append(_file_info(item))
                if len(results) >= limit:
                    break
    except PermissionError:
        pass

    return jsonify({"query": query, "count": len(results), "results": results})


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    print(f"Starting file browser on http://localhost:{port}")
    print(f"Browsing root: {ALLOWED_ROOT}")
    app.run(host="0.0.0.0", port=port, debug=debug)
