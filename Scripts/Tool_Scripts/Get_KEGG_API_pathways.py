import requests, sys

#Hsa = human KEGG_ID
#
server = "http://rest.kegg.jp/link/pathway/hsa:"

#human genes linked from each of the KEGG pathways
#link/pathway/hsa:10458+ece:Z5100
# KEGG pathways linked from a human gene and an E. coli O157 gene

#Experimental KgID ENST00000000233.10

#Gets name from ensembl
def get_KEGG_pathway(gene_id):
    name = "name not found"
    if True: #change to true to download new names
        try:
            r = requests.get(server+gene_id)
            print(r.text)
            if not r.ok:
                r.raise_for_status()
                sys.exit()

            #new_name = decoded.get("display_name")
            #name = new_name if new_name else decoded.get("description")
            #if name:
            #    name = name.replace(",","_")
            #    name = name.replace(" ", "_")
            #name = new_name if new_name else name
            #return name
        except requests.exceptions.HTTPError:
            print("not found")
            #name = "name not found"
            #return name
    else:
     return name

get_KEGG_pathway("160287")