import os

certs = str(open("/storage/certs.txt").read())

mail = str(open("/storage/config/mail.txt").read())
os.system(f"certbot --reuse-key -n --agree-tos -m {mail} --test-cert --nginx {certs}")