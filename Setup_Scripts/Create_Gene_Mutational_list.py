import pandas as pd
from collections import Counter
from Cutoff import *
from Gene_Prevalence_Entry import *
from collections import Counter
import numpy as np


case_df = pd.read_csv('../Resources/Base_Data/case.unique-gene-variants-all.tsv', sep='\t')
control_df = pd.read_csv('../Resources/Base_Data/control.unique-gene-variants-all.tsv', sep='\t')
impacts = set(list(control_df.IMPACT.unique()))

def ratio(target,total):
    total = sum(total.values)
    return np.round(target/total,2)

def print_impact_counts(dataframe,type,file_name,):
    dataframe = pd.crosstab(dataframe['GENE_ID'], dataframe['IMPACT'])
    ratio_df = dataframe.copy()
    for impact in impacts:
        ratio_df[impact+"_ratio_"+type] = dataframe.apply(lambda x: ratio(x[impact],x[impacts]), axis = 1)
    ratio_df.to_csv("Resources/Intermediary_Data/"+ file_name)

#print_impact_counts(case_df,'case',"case_gene_mutations.csv")
#print_impact_counts(control_df,'control',"control_gene_mutations.csv")

case_df = pd.read_csv('../Resources/Intermediary_Data/case_gene_mutations.csv')
control_df = pd.read_csv('../Resources/Intermediary_Data/control_gene_mutations.csv')


