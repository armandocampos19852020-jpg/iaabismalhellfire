export type UserTier = 'free' | 'pro' | 'enterprise';
export interface Track { id: string; title: string; tier: 'free' | 'pro'; }
export function canAccessContent(userTier: UserTier, track: Track): boolean {
  if (track.tier === 'free') return true;
  return userTier === 'pro' || userTier === 'enterprise';
}
