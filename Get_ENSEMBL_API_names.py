import pandas as pd
from collections import Counter
from Cutoff import *
from Gene_Prevalence_Entry import *
import Name_getter  as ng
import requests, sys
import json
import numpy as np
server = "https://rest.ensembl.org"
prefix = "/lookup/id/"
postfix ="?"

df = pd.read_csv('Resources/Secret_Data/all_genes.csv', sep=';')

#def write_cutoff_list(data_frame,cutoff,list_name):
all_freq = write_cutoff_list(df,0, 'Resources/white_list_all.csv')

id_name = {}
for id in all_freq.keys():
    name = ng.get_ensembl_name(id)
    id_name[id] = name

textfile = open("Resources/Base_Data/All_names.csv", "w")
textfile.write("id,name"+"\n")
for id, name in id_name.items():
    textfile.write(str(id) + ","
                   + str(name)
                   + "\n")
textfile.close()

#Gets name from ensembl
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



