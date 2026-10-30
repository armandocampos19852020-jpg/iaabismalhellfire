import os
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="IAabismal Hellfire Core API", version="5.0")

@app.get("/")
def health():
    return {"engine": "AeroCore-X C++20 SIMD", "status": "ONLINE", "mode": "24/7/365"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=port,
        workers=4,
        loop="uvloop",
        http="h11"
    )
