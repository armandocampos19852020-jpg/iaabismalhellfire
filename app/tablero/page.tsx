"use client";
import { useEffect, useState } from "react";
export default function Tablero(){
  const [time,setTime]=useState(new Date());
  useEffect(()=>{
    const i=setInterval(()=>setTime(new Date()),1000);
    const s=document.createElement("script");
    s.src="/aerocore-engine.js";
    document.body.appendChild(s);
    // Pone el celular en negro total
    document.documentElement.style.background="#000";
    document.body.style.background="#000";
    return ()=>clearInterval(i);
  },[]);
  return (
    <div style={{minHeight:"100vh", background:"#000", color:"#fff", display:"flex", flexDirection:"column", padding:"20px", fontFamily:"monospace"}}>
      {/* RELOJ ABISMAL */}
      <div style={{textAlign:"center", marginTop:"30px"}}>
        <div style={{fontSize:"64px", fontWeight:900, letterSpacing:"-3px"}}>{time.toLocaleTimeString('es-MX',{hour12:false})}</div>
        <div style={{fontSize:"14px", opacity:0.4}}>{time.toLocaleDateString('es-MX',{weekday:'long', day:'numeric', month:'long'})}</div>
      </div>

      {/* TABLERO NEGRO */}
      <div style={{marginTop:"40px", display:"grid", gridTemplateColumns:"1fr 1fr", gap:"15px"}}>
        <div style={{background:"#0a0a0a", border:"1px solid #1a1a1a", borderRadius:"20px", padding:"20px"}}>
          <div style={{fontSize:"10px", opacity:0.4}}>AEROCORE</div>
          <div style={{fontSize:"18px", fontWeight:900, marginTop:"10px"}}>V3 ACTIVO</div>
          <button onClick={()=>(window as any).AerocoreNative?.playHeavy()} style={{marginTop:"15px", width:"100%", padding:"12px", background:"#ff0000", color:"#fff", border:"none", borderRadius:"12px", fontWeight:900}}>🔊 BOOM</button>
        </div>
        <div style={{background:"#0a0a0a", border:"1px solid #1a1a1a", borderRadius:"20px", padding:"20px"}}>
          <div style={{fontSize:"10px", opacity:0.4}}>SISTEMA</div>
          <div style={{fontSize:"18px", fontWeight:900, marginTop:"10px"}}>NEGRO PURO</div>
          <div style={{fontSize:"12px", opacity:0.5, marginTop:"15px"}}>#000000 OLED</div>
        </div>
        <div style={{background:"#0a0a0a", border:"1px solid #1a1a1a", borderRadius:"20px", padding:"20px"}}>
          <div style={{fontSize:"10px", opacity:0.4}}>FEED</div>
          <a href="/feed/metal" style={{display:"block", fontSize:"16px", fontWeight:900, marginTop:"10px", color:"#ff0000", textDecoration:"none"}}>METAL →</a>
        </div>
        <div style={{background:"#0a0a0a", border:"1px solid #1a1a1a", borderRadius:"20px", padding:"20px"}}>
          <div style={{fontSize:"10px", opacity:0.4}}>MUSICA</div>
          <a href="/" style={{display:"block", fontSize:"16px", fontWeight:900, marginTop:"10px", color:"#fff", textDecoration:"none"}}>PLAYER →</a>
        </div>
      </div>

      {/* FONDO NEGRO TOTAL */}
      <div style={{marginTop:"auto", textAlign:"center", padding:"30px", opacity:0.2, fontSize:"10px"}}>IA ABISMAL HELLFIRE // TODO NEGRO</div>
    </div>
  );
}
