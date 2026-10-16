#!/usr/bin/env bash
set -e

echo "🔥 [ABYSSAL-CORE] Iniciando secuencia de despliegue maestro..."

# 1. Asegurar directorios
mkdir -p public/data core

# 2. Control de versiones Enterprise
git add .
git commit -m "feat: actualización total autónoma core abismal $(date +%F_%H-%M)" || echo "Sin cambios pendientes en git"
git push origin main

# 3. Despliegue en Vercel
npx vercel --prod --force --yes

echo "✅ [SISTEMA EN LÍNEA] IAabismal Hellfire operando 24/7/365 mundialmente."
