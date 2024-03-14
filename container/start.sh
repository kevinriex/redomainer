#!/bin/bash

#certbot show_account
#rm -rf /etc/nginx/sites-enabled/default
ln -sr /storage/nginx/nginxconfig.io /etc/nginx
python3 -u /storage/main.py
ln -sr /etc/nginx/sites-available/*.conf /etc/nginx/sites-enabled

#(crontab -l ; echo "0 12 * * * /usr/bin/certbot renew --quiet")| crontab -

/etc/init.d/nginx start

#cat /etc/nginx/sites-enabled/jasper-moechte-reinindiefutterluke-de_jasper-claus-com.conf
chmod 777 /etc/nginx
nginx -t
#fuser -k 80/tcp

python3 -u /storage/certs.py
#cat /var/log/letsencrypt/letsencrypt.log
#cat /etc/nginx/sites-enabled/jasper-moechte-reinindiefutterluke-de_jasper-claus-com.conf
/etc/init.d/nginx stop
#/etc/init.d/nginx start -g "daemon off;"
echo "Starting nginx deamon off;"
usr/sbin/nginx -g "daemon off;"