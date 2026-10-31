FROM python:3.12-slim AS build

RUN apt-get update && apt-get install -y --no-install-recommends g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src
COPY . .
RUN SRC=$(ls core/main.cpp main.cpp 2>/dev/null | head -n1) \
    && test -n "$SRC" \
    && g++ -O3 -std=c++20 -fopenmp "$SRC" -o /abyssal_engine

FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY --from=build /abyssal_engine /app/abyssal_engine

ENV PORT=8080
EXPOSE 8080

CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT} server:app"]
