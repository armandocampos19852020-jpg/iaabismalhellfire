"use client";
import { useEffect } from "react";
export default function Page(){
  useEffect(()=>{
    const s=document.createElement("script");
    s.src="/aerocore-engine.js";
    document.body.appendChild(s);
  },[]);
  return (
    <main style={{minHeight:"100vh", background:"#000", color:"#fff", display:"flex", flexDirection:"column", alignItems:"center", justifyContent:"center", padding:"20px"}}>
      <h1 style={{fontSize:"48px", fontWeight:900, letterSpacing:"-2px", textShadow:"0 0 20px #ff0000"}}>IA ABISMAL</h1>
      <h2 style={{fontSize:"18px", opacity:0.6, marginTop:"10px"}}>TODO NEGRO // HELLFIRE</h2>
      
      <button onClick={()=> (window as any).AerocoreNative?.playHeavy()}
        style={{marginTop:"40px", padding:"20px 40px", background:"#ff0000", color:"#fff", border:"none", borderRadius:"100px", fontWeight:900, fontSize:"22px", boxShadow:"0 0 40px #ff0000", cursor:"pointer"}}>
        🔊 REVIENTA AEROCORE 🔊
      </button>

      <div style={{marginTop:"60px", display:"flex", gap:"15px"}}>
        <a href="/feed/metal" style={{color:"#ff0000", textDecoration:"none", fontSize:"14px", border:"1px solid #ff0000", padding:"8px 16px", borderRadius:"20px"}}>FEED METAL</a>
        <a href="/reproductor" style={{color:"#fff", textDecoration:"none", fontSize:"14px", border:"1px solid #333", padding:"8px 16px", borderRadius:"20px"}}>REPRODUCTOR</a>
      </div>
    </main>
  );
}
