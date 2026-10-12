import "./globals.css";
export const metadata = { title: "IA ABISMAL HELLFIRE", description: "Todo Negro - Aerocore V3" };
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <body style={{background:"#000", color:"#fff"}}>{children}</body>
    </html>
  );
}
