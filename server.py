import os, stripe
from flask import Flask, jsonify, request

app = Flask(__name__)
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': 'Abismal Engine Pro - Acceso Vitalicio'},
                    'unit_amount': 4900, # $49.00 USD
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://iaabismalhellfire.net/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://iaabismalhellfire.net/cancel',
        )
        return jsonify({"checkout_url": session.url})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
