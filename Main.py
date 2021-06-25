import pandas as pd
from collections import Counter
from Cutoff import *
from Gene_Entry import *
import ice

df = pd.read_csv('/Users/anahrl/Desktop/ProjectGeneExpr/all_genes.csv', sep=';')
case_df = df.iloc[:,:17]
control_df = df.iloc[:,17:]


#def write_cutoff_list(data_frame,cutoff,list_name):
all_freq = write_cutoff_list(df,3, 'white_list_all.csv')
case_freq = write_cutoff_list(case_df,0,"white_list_cases.csv")
control_freq = write_cutoff_list(control_df,0,"white_list_controls.csv")

print("all genes:" + str(len(all_freq)))

gene_entries = {}
for index,value in all_freq.items():
        if case_freq.get(index) is not None or control_freq.get(index) is not None:
                gene_entries[index] = Gene_Entry(index,case_freq.get(index),control_freq.get(index))

print_entries(gene_entries, "Resources/fold_changes.csv")

