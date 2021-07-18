import pandas as pd
from Scripts.Database_API_Scripts import Get_ENSEMBL_API_names as gean
from Scripts.Database_API_Scripts import ENSEMBL37_Names_From_KEGG_MySQL as ksql
name_df = pd.read_csv("../../Resources/Data/Assisting_Data/name_list_v37_ensembl.csv")


def get_gene_name_or_desc(gene_id):
    name = gean.get_ensembl_name(gene_id)
    if name == "name not found":
        name = ksql.get_kegg_v37_name(gene_id)
    return name


#Set to true when need new list
if False:
    new_names = [gene if gene != 'name not found' else get_gene_name_or_desc(id) for gene, id in zip(name_df.GENE,name_df.GENE_ID)]
    name_df['GENE'] = new_names
    name_df.to_csv("../../Resources/Data/Assisting_Data/name_list_v2.csv")

result_df = pd.read_csv("../../Resources/Data/Assisting_Data/name_list_v2.csv")

result_df = result_df[(result_df['GENE'] == "name not found")]
print(result_df.head())

