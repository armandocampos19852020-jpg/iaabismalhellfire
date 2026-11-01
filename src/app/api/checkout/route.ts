import { NextResponse } from 'next/server';
import Stripe from 'stripe';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || 'sk_test_placeholder', {
  apiVersion: '2023-10-16' as any,
});

export async function POST(req: Request) {
  try {
    const { priceId, tier } = await req.json();
    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      line_items: [
        {
          price: priceId || 'price_1TYJ8zIvemfuYiaoT5Q7ec4w',
          quantity: 1,
        },
      ],
      mode: 'subscription',
      success_url: `https://iaabismalhellfire.vercel.app/success?session_id={CHECKOUT_SESSION_ID}&tier=${tier}`,
      cancel_url: 'https://iaabismalhellfire.vercel.app/cancel',
    });

    return NextResponse.json({ url: session.url });
  } catch (err: any) {
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
