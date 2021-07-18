import pandas as pd

# Here we read the gene prevalence file
all_mutations_df = pd.read_csv('../../Resources/Data/Base_Data/Somatic_Gene_Prevalences.csv', sep=',')
print(all_mutations_df.columns)
case_above_17 = all_mutations_df['num_mutations_case'] == 17
control_above_18 = all_mutations_df['num_mutations_control'] == 18
both_all_mutated = [a and b for a, b in zip(case_above_17, control_above_18)]

all_shared_mutations_df = all_mutations_df[both_all_mutated]
all_shared_mutations_df.to_csv('Resources/Intermediary_Data/Somatic_Mutations_Shared_All_Patients.csv', sep=',')

# common_all_df = all_mutations_df.loc[[  all_mutations_df && ]]

# df = df[['GENE','GENE_ID']]
# df = df.drop_duplicates()
# df.to_csv("Resources/Base_Data/All_names.csv")
