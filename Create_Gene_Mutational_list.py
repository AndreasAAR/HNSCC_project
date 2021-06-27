import pandas as pd
from collections import Counter
from Cutoff import *
from Gene_Prevalence_Entry import *
from collections import Counter
import numpy as np


case_df = pd.read_csv('case.unique-gene-variants-all.tsv', sep='\t')
normal_df = pd.read_csv('case.unique-gene-variants-all.tsv', sep='\t')
impacts = set(list(normal_df.IMPACT.unique()))

def ratio(target,total):
    total = sum(total.values)
    return np.round(target/total,2)

def print_impact_counts(dataframe,name):
    dataframe = pd.crosstab(dataframe['GENE_ID'], dataframe['IMPACT'])
    ratio_df = dataframe.copy()
    for impact in impacts:
        ratio_df[impact+"_ratio"] = dataframe.apply(lambda x: ratio(x[impact],x[impacts]), axis = 1)
    ratio_df.to_csv("Resources/Base_Data/"+ name)

print_impact_counts(case_df,"case_gene_mutations.csv")
print_impact_counts(normal_df,"normal_gene_mutations.csv")