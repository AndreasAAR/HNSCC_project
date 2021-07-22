import pandas as pd
from Scripts.Database_API_Scripts import Get_ENSEMBL_API_names as ge


class Name_getter():
    # API calls for gene name list moved
    def __init__(self):
        df = pd.read_csv('../../Resources/Data/Base_Data/All_names.csv', sep=',')
        df_2 = pd.read_csv('../../Resources/Data/Deprecated_data/downloaded_names.csv', sep=",")
        df_3 = pd.read_csv('../../Resources/Data/Deprecated_data/downloaded_names.csv', sep=",")

        dict1 = dict(zip(df.GENE_ID,df.GENE))
        dict2 = dict(zip(df_2.GENE_ID,df_2.GENE))
        dict3 = dict(zip(df_3.GENE_ID,df_3.GENE))
        dict1.update(dict2)
        dict1.update(dict3)
        self.name_list = dict1

    def get_name(self, gene_id):
        name = self.name_list.get(gene_id)
        name = name if name else ge.get_ensembl_name(gene_id)
        name = name if name else "name not found"
        return name



