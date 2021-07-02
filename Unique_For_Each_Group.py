import pandas as pd


#Here we read the gene prevalence file
all_mutations_df = pd.read_csv('Resources/Base_Data/Gene_Prevalences.csv', sep=',')
#print(all_mutations_df.columns)
no_cases =  all_mutations_df['num_mutations_case']==0
no_control =  all_mutations_df['num_mutations_control']==0
in_case =  all_mutations_df['num_mutations_case']>0
in_control =  all_mutations_df['num_mutations_control']>0

only_control_mutated =  [a and b for a, b in zip(no_cases, in_control)]
only_case_mutated =  [a and b for a, b in zip(no_control, in_case)]

only_control_df = all_mutations_df[only_control_mutated]
only_control_df.to_csv('Resources/Intermediary_Data/Mutations_only_in_control.csv', sep=',')

only_case_df = all_mutations_df[only_case_mutated]
only_case_df.to_csv('Resources/Intermediary_Data/Mutations_only_in_case.csv', sep=',')

#common_all_df = all_mutations_df.loc[[  all_mutations_df && ]]

#df = df[['GENE','GENE_ID']]
#df = df.drop_duplicates()
#df.to_csv("Resources/Base_Data/All_names.csv")