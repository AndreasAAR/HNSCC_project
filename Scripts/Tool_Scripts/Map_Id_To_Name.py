import pandas as pd

name_df = pd.read_csv("../../Resources/Base_Data/All_names.csv")
name_rev = name_df.loc[::,name_df.columns[::-1]]

name_dict = name_df.loc[:,['GENE_ID','GENE']].set_index('GENE_ID')['GENE'].to_dict()
print(name_dict)
Gene_prevalences_df = pd.read_csv("../../Resources/Base_Data/Gene_Prevalences.csv")


id_to_update = Gene_prevalences_df.loc[Gene_prevalences_df['name']=='name not found',:].id
print(len(id_to_update))
if False:
    for gene_id in id_to_update:
        print(gene_id)
        name = name_dict.get(gene_id)
        if name:
            Gene_prevalences_df.loc[Gene_prevalences_df['id'] == gene_id, :].name = name


Gene_prevalences_df.loc[Gene_prevalences_df['name']=='name not found',:].id.to_csv("Missing_Names.csv")