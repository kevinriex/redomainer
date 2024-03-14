#!/bin/bash

rm -rf /etc/nginx/sites-enabled/default
ln -sr /storage/nginx/nginxconfig.io /etc/nginx
python3 -u /storage/main.py
ln -sr /etc/nginx/sites-available/*.conf /etc/nginx/sites-enabled

#(crontab -l ; echo "0 12 * * * /usr/bin/certbot renew --quiet")| crontab -

/etc/init.d/nginx start

chmod 777 /etc/nginx
nginx -t

python3 -u /storage/certs.py
/etc/init.d/nginx stop
echo "Starting nginx deamon off;"
usr/sbin/nginx -g "daemon off;"