import pandas as pd
import  numpy as np
from Scripts.Database_API_Scripts import KEGG_Pathway_Description_Getter as kpdg
eng_pathway_df = pd.read_csv("../../Resources/Intermediary_Data/GENE_names_to_Pathways_raw.csv",dtype=str)

print(eng_pathway_df.head())
id_name_df = pd.DataFrame(columns =['Pathway_Id'])
print(id_name_df)
value_list = eng_pathway_df.values.tolist()[0]
unique_pathways = np.unique(value_list)
id_name_df['Pathway_Id'] = unique_pathways

id_name_df['Pathway_Name'] = [kpdg.get_ensembl_name(pid) for pid in id_name_df["Pathway_Id"]]
#print(id_name_df['Pathway_Name'])
id_name_df.to_csv("../../Resources/Assisting_Data/PathId_to_PathName.csv", index = True)

