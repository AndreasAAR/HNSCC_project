import requests, sys

server = "https://rest.ensembl.org"
prefix = "/lookup/id/"
postfix ="?"


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
            print("test")
            print(decoded)
            new_name = decoded.get("display_name")
            if not new_name:
                description =  decoded.get("description")
                descriptions = description.split(",")
                name = descriptions[1] if len(descriptions) > 1\
                                          and len(descriptions[1]) >1 else descriptions[0]
            if name:
                name = name.replace(","," ")
            name = new_name if new_name else name
            return name
        except requests.exceptions.HTTPError:
            name = "name not found"
            return name


print(get_ensembl_name("ENSG00000034063"))

