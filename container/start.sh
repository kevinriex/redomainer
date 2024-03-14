#!/bin/bash

python3 -u /storage/main.py
ln -sr /storage/nginx/nginxconfig.io /etc/nginx
ln -sr /storage/nginx/sites-available/*.conf /etc/nginx/sites-enabled

#(crontab -l ; echo "0 12 * * * /usr/bin/certbot renew --quiet")| crontab -
cat /var/log/letsencrypt/letsencrypt.log
/usr/sbin/nginx -g "daemon off;"