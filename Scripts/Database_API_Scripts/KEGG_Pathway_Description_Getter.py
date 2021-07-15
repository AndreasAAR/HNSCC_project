from json import JSONDecodeError

import requests, sys
server = "http://rest.kegg.jp/get/map"
option = ""
#/json does not seem to be available

#Gets name from ensembl
def get_ensembl_name(patway_id):
    name = "name not found"
    if True: #change to true to download new names
        try:
            print(patway_id)
            r = requests.get(server +str(patway_id)+option )
            print(r)
            text_lines = r.text.split("\n")
            name = text_lines[1].replace("NAME","").strip()
            if not r.ok:
                r.raise_for_status()
                sys.exit()
            return name
        except requests.exceptions.HTTPError:
            name = "pathway not found"
            return name
    else:
     return name

#print("Hi")
#get_ensembl_name("map00510")

#map00510
#"hsa:10458"