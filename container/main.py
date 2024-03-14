import json
import re

with open("/storage/config/sites.json") as sites_file:
    sites = json.load(sites_file)

with open("/storage/site.conf", "r") as site_file:
    site_conf = site_file.read()

for site in sites:
    from_domain = list(filter(None, re.split(r"(?:.*:\/\/)(?P<domain>.*)(?:\/.*)?", site["from"])))[0]
    to_domain = list(filter(None, re.split(r"(?:.*:\/\/)(?P<domain>.*)(?:\/.*)?", site["to"])))[0]
    siteconfigstr = site_conf.replace("~~FROM~~", from_domain).replace("~~TO~~", to_domain).replace("~~TO_URL~~", site["to"])
    print(siteconfigstr)
    with open(f"/storage/nginx/sites-available/{from_domain.replace('.','-')}_{to_domain.replace('.','-')}.conf", "x") as siteconfig:
        siteconfig.writelines(siteconfigstr)