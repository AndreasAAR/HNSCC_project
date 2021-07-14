import pandas as pd

case_df = pd.read_csv('../../Resources/Base_Data/case.unique-gene-variants-all.tsv', sep='\t')
control_df = pd.read_csv('../../Resources/Base_Data/control.unique-gene-variants-all.tsv', sep='\t')

df = case_df + control_df
df = df[['GENE','GENE_ID']]
df = df.drop_duplicates()

df.to_csv("Resources/Base_Data/All_names.csv")