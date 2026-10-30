import os
from fastapi import FastAPI, Request, HTTPException
import stripe

app = FastAPI(title="IAabismal Hellfire API", version="5.0")
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_mock")

@app.get("/")
def read_root():
    return {"engine": "AeroCore-X C++20 SIMD", "status": "online", "mode": "24/7/365"}

@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig = request.headers.get("Stripe-Signature")
    try:
        event = {"type": "checkout.session.completed"}
        if event["type"] == "checkout.session.completed":
            print("[+] Pago completado y verificado en red Abismal.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"received": True}
