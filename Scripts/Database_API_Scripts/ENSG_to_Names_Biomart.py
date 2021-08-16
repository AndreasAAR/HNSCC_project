import requests
from pybiomart import Server
from biomart import BiomartServer
import json
import tsv

def get_ensembl_name(gene_id, ver_count = -1):
    gene_name = "name not found"
    versions = [35,36,37,38,39]
    max = len(versions)-1
    print("run number {}".format(ver_count))
    ver_count += 1
    if ver_count >= max:
        return "name not found"
    try:
        if versions[ver_count] == 38:
            server = BiomartServer("http://ensembl.org/biomart/martservice")
        else:
            server = BiomartServer( "http://grch" + str(versions[ver_count]) + ".ensembl.org/biomart/martservice" )

        #http://grch37.ensembl.org/biomart/martservice
        #UHRF1 ENSG00000034063
        ensmbl_hg = server.datasets['hsapiens_gene_ensembl']
        response = ensmbl_hg.search({
          'filters': {
              'ensembl_gene_id': [gene_id]  # ID-list specified accessions
          },
        'attributes': [
               'external_gene_name'
          ]
        }, header = 1 )

        response_tokens = str(response).split(" ")
        if len(response_tokens) >= 3:
            URL = response_tokens[2].replace(",","")
            r = requests.get(URL)
            result_tokens = r.text.split("\n")
            if len(result_tokens) > 1 and len(result_tokens[1]) > 1:
                gene_name = result_tokens[1]
                return gene_name
    except requests.exceptions.HTTPError:
        print("Server down")
    if (not (ver_count >= max)) and (gene_name == "name not found"):
        return get_ensembl_name(gene_id,ver_count)
    return gene_name

print(get_ensembl_name("ENSG00000215298"))

