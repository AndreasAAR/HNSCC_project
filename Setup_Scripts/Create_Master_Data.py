import pandas as pd
name_df = pd.read_csv('../Resources/Base_Data/All_names.csv')
name_dict = name_df.set_index('GENE_ID').to_dict()['GENE']

prevalence_df = pd.read_csv('../Resources/Base_Data/Gene_Prevalences.csv')
