import requests, sys

server = "https://rest.ensembl.org"
prefix = "/lookup/id/"
postfix ="?"
import requests, sys

server = "https://rest.ensembl.org"
ext = '/lookup/id/'
postfix=  "?"

#Gets name from ensembl
def get_ensembl_name(gene_id):
    name = "name not found"
    if True: #change to true to download new names
        try:
            r = requests.get(server + prefix+str(gene_id)+postfix, headers={"Content-Type": "application/json", "Species":"Human"})
            if not r.ok:
                r.raise_for_status()
                sys.exit()
            decoded = r.json()
            new_name = decoded.get("display_name")
            name = new_name if new_name else decoded.get("description")
            if name:
                name = name.replace(",","_")
                name = name.replace(" ", "_")
            name = new_name if new_name else name
            return name
        except requests.exceptions.HTTPError:
            name = "name not found"
            return name
    else:
     return name

