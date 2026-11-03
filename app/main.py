import os
import json
import sqlite3
import time
from pathlib import Path
import stripe
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware

BASE = Path(__file__).resolve().parent.parent
DB_PATH = BASE / "abyssal.db"
TRACKS_JSON = BASE / "public" / "data" / "metal-tracks.json"

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")
stripe.api_key = STRIPE_SECRET_KEY

app = FastAPI(title="IAabismal Hellfire Core API", version="5.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ONLINE", "core": "ABISMAL", "stripe_configured": bool(STRIPE_SECRET_KEY)}

@app.get("/tracks")
def list_tracks(limit: int = 50, offset: int = 0):
    if TRACKS_JSON.exists():
        data = json.loads(TRACKS_JSON.read_text(encoding="utf-8"))
        return {"items": data["tracks"][offset:offset+limit]}
    return {"items": []}

@app.post("/api/checkout")
def checkout():
    if not STRIPE_SECRET_KEY:
        raise HTTPException(status_code=503, detail="Pagos no configurados")
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "Hellfire Pro - Acceso Vitalicio"},
                    "unit_amount": 2000,
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url="https://iaabismalhellfire.net/success.html",
            cancel_url="https://iaabismalhellfire.net/cancel.html",
        )
        return {"url": session.url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
