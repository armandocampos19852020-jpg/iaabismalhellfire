import { NextResponse } from 'next/server';
import Stripe from 'stripe';
export async function POST(req: Request) {
  const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || '');
  const sig = req.headers.get('stripe-signature') || '';
  const body = await req.text();
  try {
    const ev = stripe.webhooks.constructEvent(body, sig, process.env.STRIPE_WEBHOOK_SECRET || '');
    if (ev.type === 'checkout.session.completed') {
      console.log('PRO activado:', (ev.data.object as any).customer_email);
    }
    return NextResponse.json({ received: true });
  } catch (e: any) { return NextResponse.json({ error: e.message }, { status: 400 }); }
}
