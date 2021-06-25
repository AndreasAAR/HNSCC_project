import requests, sys
import json

server = "https://rest.ensembl.org"
prefix = "/lookup/id/"
postfix ="?"

def get_ensembl_name(id):
    name = "name not found"
    if True: #change to true to download new names
        try:
            r = requests.get(server + prefix+str(id)+postfix, headers={"Content-Type": "application/json"})
            if not r.ok:
                r.raise_for_status()
                sys.exit()
            decoded = r.json()
            new_name = decoded.get("display_name")
            name = new_name if new_name else name
            print(name)
            return name
        except requests.exceptions.HTTPError:
            name = "name not found"
            return name
    else:
     return name

