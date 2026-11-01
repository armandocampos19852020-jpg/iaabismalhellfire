FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y clang cmake libomp-dev
WORKDIR /app
COPY main.cpp .
RUN clang++ -O3 -std=c++20 -march=x86-64-v3 -ffast-math -fopenmp main.cpp -o abyssal_engine

FROM node:20-alpine AS web-builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npx next build --webpack

FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
RUN apk add --no-cache dumb-init libgomp python3 py3-pip
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001

COPY --from=builder /app/abyssal_engine ./abyssal_engine
COPY --from=web-builder /app/public ./public
COPY --from=web-builder /app/.next ./.next
COPY --from=web-builder /app/node_modules ./node_modules
COPY --from=web-builder /app/package.json ./package.json
COPY --from=web-builder /app/next.config.js ./next.config.js

USER nodejs
EXPOSE 8080
ENTRYPOINT ["dumb-init", "--"]
CMD ["npm", "start"]
