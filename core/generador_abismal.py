import json
import random
from pathlib import Path

def generar():
    tracks = []
    for i in range(1000):
        tracks.append({
            "id": f"track_{i:04d}",
            "title": f"Abyssal Execution {i}",
            "tier": "free" if i < 200 else "pro"
        })
    
    out_path = Path("public/data/metal-tracks.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({"version": "5.0", "tracks": tracks}, ensure_ascii=False, indent=2), encoding="utf-8")
    print("✅ Catálogo estructurado generado con éxito.")

if __name__ == "__main__":
    generar()
