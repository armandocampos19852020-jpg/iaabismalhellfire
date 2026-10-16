export type UserTier = 'free' | 'pro' | 'enterprise';

export interface Track {
  id: string;
  title: string;
  band: string;
  sub: string;
  tier: 'free' | 'pro';
  yt: string;
}

export function canAccessContent(userTier: UserTier, track: Track): boolean {
  if (track.tier === 'free') return true;
  return userTier === 'pro' || userTier === 'enterprise';
}
