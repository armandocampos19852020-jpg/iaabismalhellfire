FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y clang cmake libomp-dev build-essential
WORKDIR /app
COPY server.py requirements.txt ./
EXPOSE 8080
CMD ["gunicorn", "-w", "4", "-k", "gthread", "--threads", "8", "-b", "0.0.0.0:8080", "server:app"]
