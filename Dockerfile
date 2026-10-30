FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y clang cmake libomp-dev
WORKDIR /app
COPY server.py ./
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 python3-pip libgomp1 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY --from=builder /app/server.py .
RUN pip3 install --no-cache-dir fastapi uvicorn stripe
EXPOSE 8080
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "4"]
