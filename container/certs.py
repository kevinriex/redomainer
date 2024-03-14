import os

certs = str(open("/storage/certs.txt").read())

mail = str(open("/storage/config/mail.txt").read())
os.system(f"certbot run -i nginx --reuse-key -n --agree-tos --expand -m {mail} --nginx -v {certs}")