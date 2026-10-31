from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn, os

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def root(): return {"engine":"ONLINE"}
@app.get("/health")
def health(): return {"status":"healthy","engine":"active","core":"ABISMAL"}

@app.get("/api/webhook/meta")
async def meta_verify(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")
    if mode == "subscribe" and token == "abismal123":
        return int(challenge) if challenge else 0
    return {"status":"meta webhook ready"}

@app.post("/api/webhook/meta")
async def meta_post(request: Request):
    data = await request.json()
    print(f"[META] {data}")
    return {"status":"ok"}

@app.post("/api/v1/roi/update")
async def roi(request: Request):
    data = await request.json()
    return {"status":"ROI_UPDATE_SUCCESS"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=int(os.environ.get("PORT",8082)))
