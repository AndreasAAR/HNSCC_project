from ssl import SSLError

import pandas as pd
from Scripts.Database_API_Scripts import Get_ENSEMBL_API_names as gean
from Scripts.Database_API_Scripts import ENSEMBL37_Names_From_KEGG_MySQL as ksql
from Scripts.Database_API_Scripts import ENSG_to_Names_Biomart as bimrt
from Scripts.Database_API_Scripts import HGNC_API as hgnc
import signal

def signal_handler(signum, frame):
    raise Exception("Timed out!")


def get_gene_name_or_desc(gene_id):
    print(gene_id)
    name = "name not found"
    #signal.signal(signal.SIGALRM, signal_handler)
    #signal.alarm(60)  # Sixty seconds
    try:
        if name == "name not found":
            print("Trying gean.get_ensembl_name")
            # print("checking ensembl REST API")
            name = gean.get_ensembl_name(gene_id)
            if name == "name not found":
                print("Trying ksql.get_KEGG_name")
                #print("checking KEGG mysql")
                name = ksql.get_kegg_v37_name(gene_id)
                if name == "name not found":
                    print("Trying bimrt.get_ensembl_name")
                    #print("checking biommart mysql")
                    name = bimrt.get_ensembl_name(gene_id)
                    if name == "name not found":
                        print("checking HGNC mysql")
                        name = hgnc.get_HGNC_ensembl_name(gene_id)
    except SSLError:
         print("connection timed out")
    except Exception:
        print("Function calls too slow")
    except UnboundLocalError:
        print("ref error")
    #insert description calls to all here
    print(name)
    return name

print(get_gene_name_or_desc("ENST00000369748"))
print("done")

