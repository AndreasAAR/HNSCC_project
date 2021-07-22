import pandas as pd
from Scripts.Database_API_Scripts import KEGG_Pathway_Description_Getter as kge

df = pd.read_csv("../../Resources/Data/Assisting_Data/AllPatient_Mutation_Level_Names.csv",index_col = 0)

df['KEGG'] = [ kge.get(x) for x in df['GENE_NAME']]