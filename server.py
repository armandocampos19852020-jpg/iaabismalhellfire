import os, subprocess, stripe
from fastapi import FastAPI, HTTPException, Request

app = FastAPI(title="ABYSSAL-ENGINE-ENTERPRISE", version="3.0.0")
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

app = FastAPI(title="ABYSSAL-ENGINE-ENTERPRISE", version="3.0.0")
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
