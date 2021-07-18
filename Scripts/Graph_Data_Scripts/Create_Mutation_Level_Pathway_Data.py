import pandas as pd
import os
import sys

#Makes a mutation level table for each patient data file
def make_Patient_Mutation_Level_Table(folder_path,file):
    patient_df = pd.read_csv(folder_path+file,
                             sep="\t")
    df_patient = patient_df.loc[:,['GENE_ID','IMPACT']]
    df_patient =  df_patient.pivot_table(values='IMPACT', index=df_patient.index, columns='GENE_ID', aggfunc='first')
    df_patient = df_patient.apply(lambda x: pd.Series(x.dropna().to_numpy())).iloc[[0]]
    patient_group_and_id = file.split(".")[0]
    patient_group, patient_id = patient_group_and_id.split("-")
    df_patient.insert(0, "Patient_Id", patient_id, True)
    df_patient.insert(0, "Patient_group", patient_group, True)
    return df_patient

#Write a file with mutation levels for all patients
def write_patient_mutation_level_file():
    file_folder = "../../../Resources/Data/Source_Data/genes-to-variants/"
    files = os.listdir("../../../Resources/Data/Source_Data/genes-to-variants/")
    df1 = pd.DataFrame()
    for file in files:
        if ("variant" not in file) and ("all" in file):
            print(file)
            df_row = make_Patient_Mutation_Level_Table(file_folder,file)
            df1 = pd.concat([df1,df_row], axis=0, ignore_index=True)
    df1.rename(columns={"GENE_ID": "index"},inplace = True)
    return df1

df1 = pd.DataFrame()
# df1 = write_patient_mutation_level_file()

# Add pathways to prep for heatmap.

# Read in pathways
pathway_df = pd.read_csv("../../../Resources/Data/Intermediary_Data/GENE_names_to_Pathways_raw.csv")
# Need to extract all gene names instead of ENSG codes, then find most common pathways in each group.

# Need to update the name list v37 first so that it contains description
# and related gene first.


#

print(pathway_df.head())
#df1.to_csv("../../../Resources/Data/Base_Data/AllPatient_Mutation_Level.csv")
print("Wrote to file")
sys.exit()