import { NextResponse } from 'next/server';
import Stripe from 'stripe';
export async function POST(req: Request) {
  try {
    const key = process.env.STRIPE_SECRET_KEY;
    if (!key) return NextResponse.json({ error: 'STRIPE_SECRET_KEY no configurada' }, { status: 500 });
    const stripe = new Stripe(key);
    const { customerEmail } = await req.json().catch(() => ({}));
    const price = process.env.STRIPE_PRICE_PRO;
    if (!price) return NextResponse.json({ error: 'STRIPE_PRICE_PRO no configurado' }, { status: 500 });
    const site = process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000';
    const s = await stripe.checkout.sessions.create({
      mode: 'subscription',
      customer_email: customerEmail || undefined,
      line_items: [{ price, quantity: 1 }],
      success_url: `${site}/success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${site}/cancel`,
    });
    return NextResponse.json({ url: s.url });
  } catch (e: any) { return NextResponse.json({ error: e.message }, { status: 500 }); }
}
