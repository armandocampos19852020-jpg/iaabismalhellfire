	mport os
import subprocess
from flask import Flask, jsonify, request
from qdrant_client import QdrantClient
import stripe

app = Flask(__name__)
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_live_dummy")

# Inicialización cliente vectorial Qdrant (Soporta Qdrant Cloud o Local)
qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
qdrant = QdrantClient(url=qdrant_url)

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "status": "online",
        "engine": "ABYSSAL-ENGINE-CORE",
        "stack": ["C++20 SIMD", "Qdrant", "Stripe", "Cloudflare Zero Trust"]
    }), 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Ejecuta el binario compilado en C++ con -O3
        res = subprocess.run(["./abyssal_engine"], capture_output=True, text=True, timeout=5)
        return jsonify({
            "success": True,
            "telemetry": res.stdout.strip()
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/webhook/stripe", methods=["POST"])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')
    webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET", "whsec_dummy")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(f"[STRIPE] Pago completado con éxito para sesión: {session.get('id')}")
        # Aquí puedes activar el acceso a la app / créditos CCC del usuario

    return jsonify({"received": True}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
import os, subprocess, stripe
from fastapi import FastAPI, HTTPException, Request

app = FastAPI(title="ABYSSAL-ENGINE-ENTERPRISE", version="5.0.0")
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_live_dummy")

@app.get("/health")
def health_check():
    return {"status": "healthy", "engine": "active", "accelerator": "SIMD / CUDA"}

@app.post("/infer")
async def run_inference(payload: dict):
    query = payload.get("query", "")
    if not query:
        raise HTTPException(status_code=400, detail="Query vacía.")
    try:
        res = subprocess.run(["./abyssal_engine", query], capture_output=True, text=True, timeout=5)
        telemetry = res.stdout.strip()
    except Exception as e:
        telemetry = f"Fallback Python: {str(e)}"
    return {"status": "success", "query": query, "telemetry": telemetry}

@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("Stripe-Signature")
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, os.getenv("STRIPE_WEBHOOK_SECRET", ""))
        if event["type"] == "checkout.session.completed":
            session = event["data"]["object"]
            print(f"[STRIPE] Pago completado: {session.get('id')}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"received": True}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("server:app", host="0.0.0.0", port=port, workers=4)
import os, subprocess, stripe
from fastapi import FastAPI, HTTPException, Request

app = FastAPI(title="ABYSSAL-ENGINE", version="5.0.0")
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_live_dummy")

@app.get("/health")
def health():
    return {"status": "healthy", "engine": "active", "accelerator": "SIMD"}

@app.post("/infer")
async def infer(payload: dict):
    q = payload.get("query", "")
    if not q: raise HTTPException(status_code=400, detail="Query vacía")
    try:
        res = subprocess.run(["./abyssal_engine", q], capture_output=True, text=True, timeout=5)
        out = res.stdout.strip()
    except Exception as e:
        out = f"Fallback: {str(e)}"
    return {"status": "success", "query": q, "telemetry": out}

@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig = request.headers.get("Stripe-Signature")
    try:
        event = stripe.Webhook.construct_event(payload, sig, os.getenv("STRIPE_WEBHOOK_SECRET", ""))
        if event["type"] == "checkout.session.completed":
            print(f"[STRIPE] Pago completado: {event['data']['object']['id']}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"received": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), workers=4)
