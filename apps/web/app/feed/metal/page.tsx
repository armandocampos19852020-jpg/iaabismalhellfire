'use client';
import { useState } from 'react';
const TRACKS = [
  { t: 'Freezing Moon', a: 'Mayhem', g: 'Black', tier: 'Free' },
  { t: 'Altars of Madness', a: 'Morbid Angel', g: 'Death', tier: 'Free' },
  { t: 'Raining Blood', a: 'Slayer', g: 'Thrash', tier: 'Free' },
  { t: 'In the Nightside Eclipse', a: 'Emperor', g: 'Black', tier: 'Pro' },
  { t: 'Solitude', a: 'Candlemass', g: 'Doom', tier: 'Pro' },
  { t: 'Blackwater Park', a: 'Opeth', g: 'Doom', tier: 'Pro' },
];
export default function Feed() {
  const [pro, setPro] = useState(false);
  const [busy, setBusy] = useState(false);
  async function checkout() {
    setBusy(true);
    const r = await fetch('/api/checkout', { method: 'POST', headers: {'Content-Type':'application/json'}, body: '{}' });
    const d = await r.json();
    if (d.url) location.href = d.url; else { alert(d.error || 'Error'); setBusy(false); }
  }
  return (<main style={{padding:24,maxWidth:720,margin:'0 auto'}}>
    <h1>Feed Metal</h1>
    <button onClick={checkout} disabled={busy} style={{background:'#b91c1c',color:'#fff',border:0,padding:'10px 16px',borderRadius:8,fontWeight:700}}>Pasar a Pro · $16/mes</button>
    <label style={{marginLeft:12}}><input type="checkbox" checked={pro} onChange={e=>setPro(e.target.checked)} /> (demo) ver como Pro</label>
    <ul style={{listStyle:'none',padding:0}}>
      {TRACKS.map(x => { const locked = x.tier==='Pro' && !pro; return (
        <li key={x.t} style={{padding:12,borderBottom:'1px solid #222',opacity:locked?.4:1}}>
          <b>{x.t}</b> — {x.a} · {x.g} <span style={{float:'right',color:'#b91c1c'}}>{locked?'🔒 Pro':x.tier}</span>
        </li>);})}
    </ul>
  </main>);
}
