#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="$HOME/iaabismalhellfire"
mkdir -p "$WORKSPACE"
cd "$WORKSPACE"

echo "🔥 [ABYSSAL-CORE] Generando archivos fuente..."

# Generar C++
cat << 'EOF' > main.cpp
#include <iostream>
int main() { std::cout << "🔥 Engine C++20 SIMD Operativo" << std::endl; return 0; }
EOF

# Compilar motor local
g++ -O3 -std=c++20 main.cpp -o abyssal_engine || clang++ -O3 -std=c++20 main.cpp -o abyssal_engine

# Levantar API en segundo plano
pkill -f "uvicorn" 2>/dev/null || true
pip install -q fastapi uvicorn stripe

nohup python3 -m uvicorn server_stripe:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &

sleep 2
curl -s http://localhost:8000/health
echo ""
echo "✅ [SISTEMA EN LÍNEA] API corriendo en http://localhost:8000"

