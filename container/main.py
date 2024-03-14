import json
import re
import os

with open("/storage/config/sites.json") as sites_file:
    sites = json.load(sites_file)

with open("/storage/site.conf", "r") as site_file:
    site_conf = site_file.read()

certs = ""

for site in sites:
    from_domain = list(filter(None, re.split(r"(?:.*:\/\/)(?P<domain>.*)(?:\/.*)?", site["from"])))[0]
    to_domain = list(filter(None, re.split(r"(?:.*:\/\/)(?P<domain>.*)(?:\/.*)?", site["to"])))[0]
    siteconfigstr = site_conf.replace("~~FROM~~", from_domain).replace("~~TO~~", to_domain).replace("~~TO_URL~~", site["to"])
    print(siteconfigstr)
    with open(f"/storage/nginx/sites-available/{from_domain.replace('.','-')}_{to_domain.replace('.','-')}.conf", "w+") as siteconfig:
        siteconfig.writelines(siteconfigstr)

    with open(f"/var/log/nginx/{from_domain}_{to_domain}_access.log", "w+"):
        print(f"/var/log/nginx/{from_domain}_{to_domain}_access.log ### created")
    with open(f"/var/log/nginx/{from_domain}_{to_domain}_error.log", "w+"):
        print(f"/var/log/nginx/{from_domain}_{to_domain}_error.log ### created")

    certs = f"-d {from_domain} {certs}"

print(certs)

mail = str(open("/storage/config/mail.txt").read())
os.system(f"certbot certonly --reuse-key -n --agree-tos -m {mail} --test-cert --nginx {certs}")