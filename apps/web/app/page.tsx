import Link from 'next/link';
export default function Home() {
  return (<main style={{padding:24,maxWidth:720,margin:'0 auto'}}>
    <h1 style={{color:'#b91c1c'}}>HELLFIRE</h1>
    <p>1.000 pistas · 10 subgéneros · 3 niveles. Motor AeroCore-X.</p>
    <Link href="/feed/metal" style={{color:'#fff'}}>Entrar al Feed Metal →</Link>
  </main>);
}
