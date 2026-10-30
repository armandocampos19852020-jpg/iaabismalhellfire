import os
import subprocess
from fastapi import FastAPI, Request, HTTPException
import stripe

app = FastAPI(title="IAabismal Hellfire Core API")

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_placeholder")
ENDPOINT_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "whsec_placeholder")

@app.get("/health")
def health_check():
    return {"status": "ONLINE", "core": "ABYSSAL-ENGINE", "mode": "24/7/365"}

@app.post("/predict")
def run_inference():
    try:
        res = subprocess.run(["./abyssal_engine"], capture_output=True, text=True, check=True)
        return {"telemetry": res.stdout.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/create-checkout-session")
async def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': 'Hellfire Pro - Acceso Vitalicio & 1000 Tracks O(1)'},
                    'unit_amount': 2000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://iaabismalhellfire.net/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://iaabismalhellfire.net/cancel',
        )
        return {"url": session.url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, ENDPOINT_SECRET)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Webhook Error: {str(e)}")

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(f"🔥 [STRIPE] Pago completado: {session.id}")

    return {"status": "success"}
import os
from fastapi import FastAPI, Request, HTTPException
import stripe

app = FastAPI(title="IAabismal Hellfire Billing Core")
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_live_tu_llave")
ENDPOINT_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "whsec_tu_secret")

@app.post("/create-checkout-session")
async def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': 'Hellfire Pro - Acceso Vitalicio & 1000 Pistas O(1)'},
                    'unit_amount': 2000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://iaabismalhellfire.net/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://iaabismalhellfire.net/cancel',
        )
        return {"url": checkout_session.url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, ENDPOINT_SECRET)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Webhook error: {str(e)}")

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(f"🔥 [STRIPE] Pago completado con éxito para sesión: {session.id}")
        # Registro automático de licencia Pro en base de datos local / Redis

    return {"status": "success"}
import os
from fastapi import FastAPI, Request, HTTPException
import stripe

app = FastAPI(title="IAabismal Hellfire Billing Core")
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_live_tu_llave")
ENDPOINT_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "whsec_tu_secret")

@app.post("/create-checkout-session")
async def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': 'Hellfire Pro - Acceso Vitalicio & 1000 Pistas O(1)'},
                    'unit_amount': 2000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://iaabismalhellfire.net/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://iaabismalhellfire.net/cancel',
        )
        return {"url": checkout_session.url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, ENDPOINT_SECRET)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Webhook error: {str(e)}")

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(f"🔥 [STRIPE] Pago completado con éxito para sesión: {session.id}")
        # Aquí puedes activar automáticamente la licencia PRO en base de datos o Redis

    return {"status": "success"}
