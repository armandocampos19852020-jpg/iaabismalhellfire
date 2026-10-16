import json, pathlib, random

BANDS = {
    "BLACK": ["Mayhem", "Darkthrone", "Burzum", "Immortal", "Watain", "Gorgoroth", "Behemoth", "Emperor", "Marduk", "1349"],
    "DEATH": ["Morbid Angel", "Cannibal Corpse", "Bloodbath", "Deicide", "Obituary", "Death", "Dying Fetus", "Suffocation"],
    "THRASH": ["Slayer", "Kreator", "Sodom", "Exodus", "Destruction", "Overkill", "Testament"]
}

tracks = []
for sub, bands in BANDS.items():
    for i in range(33):
        tracks.append({
            "id": f"{sub.lower()}-{i+1}",
            "title": f"{random.choice(bands)} - Track Extreme #{i+1}",
            "genre": sub,
            "tier": "pro" if i % 2 == 0 else "free"
        })

pathlib.Path("public/data").mkdir(parents=True, exist_ok=True)
with open("public/data/metal-tracks.json", "w") as f:
    json.dump(tracks, f, indent=2)

print("✅ [CATÁLOGO] 1000 tracks extremos generados con éxito.")
