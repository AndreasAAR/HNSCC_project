import os
import pandas as pd

from Scripts.Tool_Scripts.ENSEMBL38_37_KEGG_Name_Getter import get_gene_name_or_desc

file_folder = "../../../Resources/Data/Source_Data/genes-to-variants/"
files = os.listdir("../../../Resources/Data/Source_Data/genes-to-variants/")
df1 = pd.DataFrame()
gids = set()
for file in files:
    if ("variant" not in file) and ("all" in file):
        patient_df = pd.read_csv(file_folder + file,
                                 sep="\t")
        gids.update(patient_df['GENE_ID'])

name_id_Dict = {gid: get_gene_name_or_desc(gid) for gid in gids}
id_df = pd.DataFrame(name_id_Dict.items(), columns=['GENE_NAME','GENE_ID'])
id_df.to_csv("../../Resources/Data/Intermediary_Data/AllPatient_Mutation_Level_Names.csv")



print("DONE")