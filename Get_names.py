import pandas as pd
from collections import Counter
from Cutoff import *
from Gene_Entry import *
import Name_getter  as ng

df = pd.read_csv('Resources/Base_Data/all_genes.csv', sep=';')

#def write_cutoff_list(data_frame,cutoff,list_name):
all_freq = write_cutoff_list(df,0, 'white_list_all.csv')

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
