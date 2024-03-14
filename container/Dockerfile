FROM debian:latest

RUN apt update && apt upgrade -y

# Installation
RUN apt install python3 nginx python3-certbot-nginx -y

RUN mkdir /storage

# NGINX
EXPOSE 80/tcp
EXPOSE 443/tcp
ADD nginx/ /storage/nginx/

# Script
ADD start.sh /storage/start.sh
ADD main.py /storage/main.py
ADD certs.py /storage/certs.py
ADD site.conf /storage/site.conf

RUN chmod +x /storage/start.sh
CMD ["./storage/start.sh"]