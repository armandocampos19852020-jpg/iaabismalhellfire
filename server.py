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
