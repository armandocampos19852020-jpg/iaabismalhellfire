import os
import stripe
from fastapi import FastAPI, Request, HTTPException

app = FastAPI(title="ABYSSAL-ENGINE-PROD", version="3.0.0")
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
ENDPOINT_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")

@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("Stripe-Signature")
    
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, ENDPOINT_SECRET)
    except ValueError:
        raise HTTPException(status_code=400, detail="Payload inválido")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Firma de Stripe inválida")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        customer_email = session.get("customer_details", {}).get("email")
        print(f"[STRIPE_SUCCESS] Acceso Pro activado para: {customer_email}")
        # Aquí disparas la base de datos o Redis para subir el tier del usuario

    return {"status": "success", "received": True}
import os, subprocess
from fastapi import FastAPI, HTTPException

app = FastAPI(title="ABYSSAL-ENGINE-ENTERPRISE", version="3.0.0")

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

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("server:app", host="0.0.0.0", port=port, workers=4)
