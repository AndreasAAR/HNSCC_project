
import requests, sys

server = "https://rest.genenames.org/"
prefix = "search/ensembl_gene_id/"


#Gets name from ensembl
def get_HGNC_ensembl_name(gene_id):
    if True: #change to true to download new names
        try:
            r = requests.get(server + prefix+str(gene_id), headers={"Accept":"application/json"})
            if not r.ok:
                r.raise_for_status()
                sys.exit()
            decoded = r.json()
            if decoded.get("response").get("numFound") >= 1:
                doc_list = decoded.get("response").get("docs")[0]
                new_name = dict(doc_list).get("symbol")
                return new_name
            else:
                return "name not found"
        except requests.exceptions.HTTPError:
            return "name not found"


print(get_HGNC_ensembl_name("ENSG00000185554"))
#UHRF1 ENSG00000034063
#ENSG00000259714