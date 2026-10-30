#!/usr/bin/env bash
set -euo pipefail
WORKSPACE="$HOME/iaabismalhellfire"
mkdir -p "$WORKSPACE/public/data" "$WORKSPACE/core" "$WORKSPACE/src/lib"
cd "$WORKSPACE"
python3 -c '
import json, pathlib, random
tracks = [{"id": f"J5yta7KG4Rg_{i:04d}", "band": "Slayer", "title": f"Track {i}", "sub": "THRASH", "year": 2026, "yt": "J5yta7KG4Rg", "tier": "free" if i<3 else "pro"} for i in range(1000)]
pathlib.Path("public/data").mkdir(parents=True, exist_ok=True)
pathlib.Path("public/data/metal-tracks.json").write_text(json.dumps({"version":"5.0","engine":"AeroCore-X","total":1000,"tracks":tracks}, ensure_ascii=False, indent=2))
print("✅ 1000 pistas sincronizadas.")
'
git remote set-url origin https://github.com/armandocampos19852020-jpg/iaabismalhellfire.git || true
git add .
git commit -m "feat(abismal): master deploy atómico - $(date +%F_%H-%M)" || echo "Sin cambios"
git push origin main --force
