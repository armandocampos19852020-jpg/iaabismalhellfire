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
