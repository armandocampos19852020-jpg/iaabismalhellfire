FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y clang cmake libomp-dev build-essential
WORKDIR /app
COPY core/ ./core/
RUN clang++ -O3 -std=c++20 -march=x86-64-v3 -ffast-math -fopenmp core/main.cpp -o abyssal_engine

FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 python3-pip libgomp1 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY --from=builder /app/core/abyssal_engine .
COPY server.py requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8080", "server:app"]
