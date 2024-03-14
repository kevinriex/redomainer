import os
import json
import re

certs = str(open("/storage/certs.txt").read())

mail = str(open("/storage/config/mail.txt").read())
os.system(f"certbot run -i nginx --reuse-key -n --agree-tos -m {mail} --nginx -v {certs}")


#os.system(f"certbot -i nginx --reuse-key -n --agree-tos -m {mail} --test-cert {certs}")

# with open("/storage/config/sites.json") as sites_file:
#     sites = json.load(sites_file)

# for site in sites:
#     from_domain = list(filter(None, re.split(r"(?:.*:\/\/)(?P<domain>.*)(?:\/.*)?", site["from"])))[0]
#     to_domain = list(filter(None, re.split(r"(?:.*:\/\/)(?P<domain>.*)(?:\/.*)?", site["to"])))[0]
#     content = open(f"/etc/nginx/sites-available/{from_domain.replace('.','-')}_{to_domain.replace('.','-')}.conf", "r").read()
#     with open(f"/etc/nginx/sites-available/{from_domain.replace('.','-')}_{to_domain.replace('.','-')}.conf", "w+") as siteconfig:
#         print(content)
#         siteconfig.writelines(content.replace("#~#", ""))