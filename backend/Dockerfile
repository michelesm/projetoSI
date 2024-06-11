FROM python:3.11

WORKDIR /app

RUN apt update && apt install -y \
    curl \
    git \
    unzip \
    mariadb-client \
&& rm -rf /var/cache/apt/*

COPY . /app/

RUN pip3 install -r requirements.txt

CMD ["bash", "/app/entrypoint.sh"]
