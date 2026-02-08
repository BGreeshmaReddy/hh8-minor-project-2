from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

from core.encryptor import encrypt_file
from core.shredder import overwrite_file
from core.hasher import file_hash

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

STATE = {
    "path": None,
    "encrypted": None,
    "hash": None
}

# ================= LOGGING =================

def write_log(message):
    with open("deletion_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {message}\n")

# ================= HELPERS =================

def get_passes(level):
    return {"low": 1, "medium": 7, "high": 35}.get(level, 7)

# ================= PAGES =================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/demo")
def demo():
    return render_template("demo.html")

@app.route("/test")
def test():
    return render_template("test_delete.html")

# ================= REAL SECURE DELETE =================

@app.route("/delete", methods=["POST"])
def delete():
    file = request.files.get("file")
    level = request.form.get("level", "medium")

    if not file:
        return "No file received", 400

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    passes = get_passes(level)

    # Hash before deletion
    h = file_hash(path)
    write_log(f"REAL DELETE | {file.filename} | HASH {h}")

    # Encrypt file
    encrypted_path = encrypt_file(path)
    write_log("REAL DELETE | ENCRYPTED")

    # Secure overwrite
    overwrite_file(path, passes)
    overwrite_file(encrypted_path, passes)
    write_log(f"REAL DELETE | SECURE | {passes} PASSES")

    return render_template(
        "result.html",
        filename=file.filename,
        level=level.upper(),
        passes=passes
    )

# ================= DEMO STEPS =================

@app.route("/step/upload", methods=["POST"])
def step_upload():
    file = request.files.get("file")
    if not file:
        return jsonify(error="No file"), 400

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    h = file_hash(path)
    STATE["path"] = path
    STATE["hash"] = h

    write_log(f"DEMO UPLOAD | {file.filename} | HASH {h}")
    return jsonify(message="File uploaded", hash=h)

@app.route("/step/normal-delete", methods=["POST"])
def step_normal_delete():
    if STATE["path"] and os.path.exists(STATE["path"]):
        os.remove(STATE["path"])
        write_log("DEMO | NORMAL DELETE | RECOVERABLE")
        return jsonify(message="Normal delete done", status="RECOVERABLE")
    return jsonify(error="File missing"), 400

@app.route("/step/encrypt", methods=["POST"])
def step_encrypt():
    if not STATE["path"] or not os.path.exists(STATE["path"]):
        return jsonify(error="File missing"), 400

    encrypted = encrypt_file(STATE["path"])
    STATE["encrypted"] = encrypted

    with open(encrypted, "rb") as f:
        preview = f.read(48).hex()

    write_log("DEMO | ENCRYPTION")
    return jsonify(message="Encrypted", preview=preview)

@app.route("/step/overwrite", methods=["POST"])
def step_overwrite():
    level = request.json.get("level", "medium")
    passes = get_passes(level)

    for p in [STATE["path"], STATE["encrypted"]]:
        if p and os.path.exists(p):
            overwrite_file(p, passes)

    write_log(f"DEMO | SECURE OVERWRITE | {passes} PASSES")
    return jsonify(message="Overwrite complete", passes=passes)

@app.route("/step/audit")
def step_audit():
    return jsonify(message="Check deletion_log.txt for proof")

# ================= RUN =================

if __name__ == "__main__":
    app.run(debug=True)
