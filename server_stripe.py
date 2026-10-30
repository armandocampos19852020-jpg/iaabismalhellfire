import os
from fastapi import FastAPI, Request, HTTPException
import stripe

app = FastAPI(title="IAabismal Hellfire Billing Core")
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_live_tu_llave")
ENDPOINT_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "whsec_tu_secret")

@app.get("/health")
def health():
    return {"status": "ONLINE", "engine": "AeroCore-X", "mode": "24/7/365"}

@app.post("/create-checkout-session")
async def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
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
        raise HTTPException(status_code=400, detail=f"Webhook error: {str(e)}")

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(f"🔥 [STRIPE] Pago completado con éxito para sesión: {session.id}")

    return {"status": "success"}
