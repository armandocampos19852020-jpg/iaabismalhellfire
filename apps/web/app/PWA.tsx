'use client';
import { useEffect, useState } from 'react';
export default function PWA() {
  const [evt, setEvt] = useState<any>(null);
  useEffect(() => {
    if ('serviceWorker' in navigator) navigator.serviceWorker.register('/sw.js').catch(() => {});
    const h = (e: any) => { e.preventDefault(); setEvt(e); };
    window.addEventListener('beforeinstallprompt', h);
    return () => window.removeEventListener('beforeinstallprompt', h);
  }, []);
  if (!evt) return null;
  return <button onClick={() => evt.prompt()} style={{position:'fixed',bottom:16,right:16,padding:'12px 18px',background:'#b91c1c',color:'#fff',border:0,borderRadius:8,fontWeight:700}}>Instalar app</button>;
}
