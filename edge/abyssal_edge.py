import os, subprocess
from flask import Flask, jsonify
app = Flask(__name__)
ENGINE = os.path.join(os.path.dirname(__file__), "..", "core", "abyssal_engine")

@app.get("/")
def health():
    return jsonify(status="online", engine="ABYSSAL-CORE")

@app.post("/predict")
def predict():
    try:
        r = subprocess.run([ENGINE], capture_output=True, text=True, timeout=5)
        return jsonify(success=True, output=r.stdout.strip())
    except Exception as e:
        return jsonify(success=False, error=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
