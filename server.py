from fastapi import FastAPI, Request, HTTPException
import subprocess, os, stripe

app = FastAPI(title="Abismal Engine API Enterprise")
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_dummy")

@app.get("/health")
def health_check():
    return {"status": "healthy", "engine": "AeroCore-X", "mode": "24/7/365"}

@app.post("/predict")
def run_inference():
    try:
        result = subprocess.run(["./abyssal_engine"], capture_output=True, text=True, timeout=5)
        return {"telemetry": result.stdout.strip(), "status": 200}
    except Exception as e:
        return {"error": str(e)}, 500

@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig = request.headers.get("Stripe-Signature")
    endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET", "")
    
    if not endpoint_secret:
        return {"received": True, "warning": "No webhook secret configured"}
    
    try:
        event = stripe.Webhook.construct_event(payload, sig, endpoint_secret)
        if event["type"] == "checkout.session.completed":
            print(f"💰 PAGO EXITOSO - Session ID: {event['data']['object']['id']}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return {"received": True}
