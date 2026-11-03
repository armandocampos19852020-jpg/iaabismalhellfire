from flask import Flask, jsonify, request
import os, subprocess, stripe

app = Flask(__name__)
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_live_dummy")

@app.get("/")
def home():
    return jsonify({"engine": "AeroCore-X", "status": "online", "mode": "24-7"})

@app.post("/predict")
def predict():
    return jsonify({"telemetria": "SIMD C++20 OK"})

@app.post("/webhook/stripe")
def stripe_webhook():
    return jsonify({"received": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
