import pandas as pd
from Scripts.Tool_Scripts.Cutoff import *
from Gene_Prevalence_Entry import *
from Scripts.Tool_Scripts import Name_getter

df = pd.read_csv('../../Resources/Source_Data/somatic_genes.csv', sep=';')
case_df = df.iloc[:,:17]
control_df = df.iloc[:,17:]

#def write_cutoff_list(data_frame,cutoff,list_name):
all_freq = write_cutoff_list(df,0, '../../Resources/Intermediary_Data/somatic_white_list_all.csv')
case_freq = write_cutoff_list(case_df,0,"../../Resources/Intermediary_Data/somatic_white_list_cases.csv")
control_freq = write_cutoff_list(control_df,0,"../../Resources/Intermediary_Data/somatic_white_list_controls.csv")

print("all genes:" + str(len(all_freq)))

gene_entries = {}
name_getter = Name_getter.Name_getter()

for index,value in all_freq.items():
        if "ENSG" in str(index) and (case_freq.get(index) is not None or control_freq.get(index) is not None ) :
                name = name_getter.get_name(index)
                gene_entries[index] = Gene_Prevalence_Entry(id = index, name = name, number_case = case_freq.get(index), number_control = control_freq.get(index))

print_entries(gene_entries, "../../Resources/Base_Data/Somatic_Gene_Prevalences.csv")

