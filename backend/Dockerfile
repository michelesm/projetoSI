# Stage 1: Build the backend
FROM python:3.11 AS builder
WORKDIR /app
RUN apt update && apt install -y \
    curl \
    git \
    unzip \
    mariadb-client \
&& rm -rf /var/cache/apt/*
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /app/

# Stage 2: Run the backend
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app /app
EXPOSE 8080
CMD ["bash", "/app/entrypoint.sh"]

