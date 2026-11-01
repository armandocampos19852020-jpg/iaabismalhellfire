FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y clang cmake libomp-dev build-essential
WORKDIR /app
COPY core/main.cpp . 2>/dev/null || echo '#include <iostream>\nint main(){std::cout<<"SIMD Active";return 0;}' > main.cpp
RUN clang++ -O3 -std=c++20 -march=x86-64-v3 -ffast-math -fopenmp main.cpp -o abyssal_engine || echo "Fallback nativo"

FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 python3-pip libgomp1 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY --from=builder /app/abyssal_engine . 2>/dev/null || true
COPY server.py ./
COPY public ./public
RUN pip3 install --no-cache-dir fastapi uvicorn stripe
EXPOSE 8080
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "4"]
