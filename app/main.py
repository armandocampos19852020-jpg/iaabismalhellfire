from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Abismal Core API", version="2.1.0")

class CheckoutRequest(BaseModel):
    tier: str
    user_id: str

@app.get("/")
def read_root():
    return {"status": "online", "engine": "AeroCore-X", "author": "Armando Adan Campos Velazquez"}

@app.post("/api/checkout")
def create_checkout(req: CheckoutRequest):
    if req.tier not in ["pro", "enterprise"]:
        raise HTTPException(status_code=400, detail="Invalid tier specified")
    return {"success": True, "checkout_url": f"https://checkout.stripe.com/pay/abismal_{req.tier}"}
