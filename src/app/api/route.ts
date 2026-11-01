import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

type Track = { id: string; title: string; sub: string; yt: string; band: string; tier: string; };

const loadCatalog = () => {
  try {
    const p = path.join(process.cwd(), 'public', 'data', 'metal-tracks.json');
    if (!fs.existsSync(p)) return { tracks: [], index: new Map<string, Track[]>() };
    const data = JSON.parse(fs.readFileSync(p, 'utf8'));
    const idx = new Map<string, Track[]>();
    for (const t of data.tracks) {
      const k = (t.sub || 'unknown').toLowerCase();
      if (!idx.has(k)) idx.set(k, []);
      idx.get(k)!.push(t);
    }
    return { tracks: data.tracks as Track[], index: idx };
  } catch (e) {
    return { tracks: [], index: new Map() };
  }
};

const { tracks: ALL, index: IDX } = loadCatalog();

export async function GET() {
  return NextResponse.json({
    engine: "ABYSSAL ENGINE CORE v5.0 // CCC-QUANTUM",
    status: "ONLINE_24_7",
    total_tracks: ALL.length,
    vector_search: "QDRANT_ACTIVE"
  });
}

export async function POST(req: Request) {
  try {
    const { tool, args } = await req.json();
    if (tool === 'get_metal_tracks') {
      const sub = (args?.subgenre || 'todo').toLowerCase();
      const list = sub === 'todo' ? ALL : (IDX.get(sub) || []);
      return NextResponse.json({ success: true, count: list.length, tracks: list.slice(0, 100) });
    }
    if (tool === 'play_track') {
      const t = ALL.find(x => x.id === args?.id);
      if (!t) return NextResponse.json({ success: false, error: "Track not found" }, { status: 404 });
      return NextResponse.json({ success: true, url: `https://www.youtube.com/watch?v=${t.yt}`, track: t });
    }
    return NextResponse.json({ success: false, error: "Tool invalid" }, { status: 400 });
  } catch (e: any) {
    return NextResponse.json({ success: false, error: e.message }, { status: 500 });
  }
}
