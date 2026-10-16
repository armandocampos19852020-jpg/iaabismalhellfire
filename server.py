import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health_check():
    return jsonify({"status": "healthy", "service": "abyssal-engine", "engine": "active"})

@app.route("/")
def index():
    return "🔥 Abyssal Engine - Operativo 24/7 con FastAPI/Flask y C++ SIMD!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
