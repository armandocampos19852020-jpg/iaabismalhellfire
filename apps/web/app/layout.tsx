import PWA from './PWA';
export const metadata = { title: 'Hellfire · IA Abismal', manifest: '/manifest.webmanifest' };
export const viewport = { themeColor: '#b91c1c' };
export default function Root({ children }: { children: React.ReactNode }) {
  return (<html lang="es"><body style={{margin:0,background:'#0a0a0a',color:'#eee',fontFamily:'system-ui,sans-serif'}}>{children}<PWA /></body></html>);
}
