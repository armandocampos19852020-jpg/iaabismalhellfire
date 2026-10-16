import json, pathlib, random

BANDS = {
    "BLACK": ["Mayhem", "Darkthrone", "Burzum", "Immortal", "Watain", "Gorgoroth", "Behemoth", "Emperor", "Marduk", "Satyricon"],
    "DEATH": ["Morbid Angel", "Cannibal Corpse", "Bloodbath", "Deicide", "Obituary", "Death", "Dying Fetus", "Suffocation", "Nile"],
    "THRASH": ["Slayer", "Kreator", "Sodom", "Exodus", "Destruction", "Overkill", "Testament", "Sepultura"],
    "DOOM": ["Opeth", "Candlemass", "Paradise Lost", "Katatonia", "My Dying Bride"]
}

TITLES = [
    "Freezing Moon", "Dunkelheit", "Tornekratt", "Raining Blood", "Pleasure to Kill", 
    "Agent Orange", "Altars of Madness", "Left Hand Path", "Demigod", "Evangelion"
]

tracks = []
used = set()

while len(tracks) < 1000:
    sub = random.choice(list(BANDS.keys()))
    band = random.choice(BANDS[sub])
    base = random.choice(TITLES)
    title = base if f"{band}-{base}" not in used else f"{base} Ritual {len(tracks)}"
    key = f"{band}-{title}"
    if key in used:
        continue
    used.add(key)
    tracks.append({
        "id": f"track_{len(tracks):04d}",
        "band": band,
        "title": title,
        "sub": sub,
        "year": random.randint(1985, 2026),
        "yt": "J5yta7KG4Rg",
        "tier": "free" if len(tracks) < 200 else "pro"
    })

pathlib.Path("public/data/metal-tracks.json").write_text(
    json.dumps({"version": "5.0", "engine": "AeroCore-X", "total": len(tracks), "tracks": tracks}, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
print(f"🔥 {len(tracks)} Rolas generadas en public/data/metal-tracks.json")
