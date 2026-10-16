import csv, json, sys, re
from youtube_transcript_api import YouTubeTranscriptApi
HILOS = ["poder","elite","control","dinero","ia","blockchain","chip","religion",
         "inmortalidad","gen","cuantico","guerra","energia"]
def transcript(vid):
    try:
        f = YouTubeTranscriptApi().fetch(vid, languages=["es","en"])
        return " ".join(s.text for s in f)
    except Exception:
        t = YouTubeTranscriptApi.get_transcript(vid, languages=["es","en"])
        return " ".join(s["text"] for s in t)
def hilos(txt):
    low = txt.lower()
    return {h: len(re.findall(r"\b"+h+r"\b", low)) for h in HILOS if h in low}
def main(ids):
    rows = []
    for v in ids:
        try:
            h = hilos(transcript(v))
            top = sorted(h, key=h.get, reverse=True)[:3]
            rows.append({"video_id": v, "hilos": ",".join(top), "conteos": json.dumps(h),
                         "oportunidad": f"Pieza de autoridad sobre {' + '.join(top)} aplicada a música extrema + IA" if top else ""})
            print("OK", v, top)
        except Exception as e:
            print("FAIL", v, e)
    if rows:
        with open("cerebro_ecos.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
        json.dump(rows, open("cerebro_ecos.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
if __name__ == "__main__":
    ids = sys.argv[1:] or [l.strip() for l in open("video_ids.txt") if l.strip()]
    main(ids)
