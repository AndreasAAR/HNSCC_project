from multiprocessing.pool import ThreadPool

import numpy as np
import pandas as pd
from collections import Counter
import scipy.stats as stats
import matplotlib.pyplot as plt

from scipy.stats import chi2_contingency
import Scripts.Tool_Scripts.ENSEMBL38_37_KEGG_Name_Getter as ng
import multiprocessing
import time

df = pd.read_csv("../../../Resources/Data/Source_Data/all_genes.csv",sep=";")


def get_on_col(df, pattern):
    control_idx = [i for i in df.columns if pattern in i]
    return df[control_idx]

df_controls = get_on_col(df,"Control")
df_cases = get_on_col(df,"Case")

def get_counts(df):
    case_list = df.values.tolist()
    case_list = [val for sublist in case_list for val in sublist]
    return Counter(case_list)


# Only run if the df file needs to be recreated from scratch!
if False:
    case_list = get_counts(df_cases)
    control_list = get_counts(df_controls)
    meta_df = pd.read_csv("Metastasis_Genes.csv", sep=";")
    case_df = pd.DataFrame.from_dict(case_list, orient='index')
    control_df =pd.DataFrame.from_dict(control_list, orient='index')
    count_df = pd.merge(case_df,control_df,how="outer",right_index=True,left_index =True)
    count_df.columns =["Case","Control"]
    count_df['Case'].replace(np.nan, 0, inplace=True)
    count_df['Control'].replace(np.nan, 0, inplace=True)

#count_df['ENSG'] = count_df.index
#count_df.merge(df[['GENE', 'GENE_id']], left_on='ENSG', right_on='GENE_id')
    print(count_df.head())
    cpu_count = multiprocessing.cpu_count()
    print("CPU COUNT IS: " + str(cpu_count-1))
    pool = ThreadPool(cpu_count)
    names = pool.map(ng.get_gene_name_or_desc, count_df.index)
# TODO Potential fix https://stackoverflow.com/questions/25976350/timeout-for-each-thread-in-threadpool-in-python
    count_df['names'] = names
    count_df.to_csv("count_df.csv")


meta_df = pd.read_csv("Metastasis_Genes.csv",sep=";")
relap_df = pd.read_csv("Relapse_Genes.csv",sep=";")
count_df = pd.read_csv("count_df.csv")
name_df = pd.read_csv("../../../Resources/Data/Assisting_Data/AllPatient_Mutation_Level_Names.csv")
name_df.columns = ["Row_num","GENE_ID","GENE_NAME"]
count_df.columns = ["GENE_ID",     "Case",  "Control", "GENE_NAME"]
print(count_df.head())

def apply_name_list(df, name_df):
    df = pd.merge(df,name_df,how="outer",right_on="GENE_ID",left_on="GENE_ID")
    df['GENE_NAME_x'] = [name_x if name_x != 'name not found' else name_y  for name_x,name_y in zip(df['GENE_NAME_x'],df['GENE_NAME_y']) ]
    return df

count_df = apply_name_list(count_df, name_df)
count_df = count_df[['GENE_ID','Case','Control','GENE_NAME_x']]
count_df.columns = ['GENE_ID','Case','Control','GENE_NAME']
meta_df.columns = ['GENE_NAME','Meta_Case']
relap_df.columns = ['GENE_NAME','Relap_Case']

relap_df = relap_df[relap_df['GENE_NAME'].notna()]
meta_df = meta_df[meta_df['GENE_NAME'].notna()]
count_df = count_df[count_df['GENE_ID'].notna()]

relap_df = relap_df[ relap_df['GENE_NAME'].isin(count_df['GENE_NAME'])]
meta_df = meta_df[meta_df['GENE_NAME'].isin(count_df['GENE_NAME'])]



count_df = pd.merge(count_df,meta_df,how="outer",right_on="GENE_NAME",left_on="GENE_NAME")
count_df = pd.merge(count_df,relap_df,how="outer",right_on="GENE_NAME",left_on="GENE_NAME")

num_meta = 5
num_relap = 5
num_reme = num_meta+num_relap


count_df['Meta_Case'] = count_df['Meta_Case'].fillna(0)
count_df['Relap_Case'] = count_df['Relap_Case'].fillna(0)

count_df = count_df[ [ (co > 4 or ca > 4 ) for co,ca in zip(count_df['Control'] , count_df['Case'])]]

print(count_df.head())
case  =  count_df['Case']
control  =  count_df['Control']
meta_case  =  count_df['Meta_Case']
relap_case  =  count_df['Relap_Case']


if False:
    # High meta and rep
    high_meta = count_df
    high_meta["interest_value"] = [((met+rep)/num_reme)  for ca,co,met,rep in zip(case,control,meta_case,relap_case)]
    high_meta =  high_meta.sort_values('interest_value', ascending=False)
    high_meta.to_csv("high_meta.csv")
    print(high_meta.head())

    # High case and control together
    high_case_control_freq = count_df
    high_case_control_freq["interest_value"] = [(co/17 + ca/18)/2  for ca,co,met,rep in zip(case,control,meta_case,relap_case)]
    high_case_control_freq =  high_case_control_freq.sort_values('interest_value', ascending=False)
    high_case_control_freq.to_csv("high_case_control_freq.csv")
    print(high_case_control_freq.head())

    # High difference case and control
    high_diff_case_control = count_df
    high_diff_case_control["interest_value"] = [ np.abs(co/17 - ca/18)  for ca,co,met,rep in zip(case,control,meta_case,relap_case)]
    high_diff_case_control =  high_diff_case_control.sort_values('interest_value', ascending=False)
    high_diff_case_control.to_csv("high_diff_case_control.csv")
    print(high_diff_case_control.head())


# For chi-square table use example below
# https://www.geeksforgeeks.org/python-pearsons-chi-square-test/

if False:
    chi2_diff_case_control = count_df
    chi2_diff_case_control["p_value"] = [str(round(chi2_contingency([[ca+meta],[co]])[1],3)) if (int(ca+meta) != 0 and co != 0) else "invalid size"  for ca,co,meta,rep in zip(case,control,meta_case,relap_case)]
    chi2_diff_case_control =  chi2_diff_case_control.sort_values('p_value', ascending=True)
    chi2_diff_case_control.to_csv("chi2_diff_case_control.csv")
    print(chi2_diff_case_control.head())

    fish_diff_case_control = count_df
    fish_diff_case_control["p_value"] = [str(round(stats.fisher_exact([[ca+meta,17-ca],[co,18-co]])[1],3)) if (int(ca+meta) != 0 and co != 0) else "invalid size"  for ca,co,meta,rep in zip(case,control,meta_case,relap_case)]
    fish_diff_case_control.sort_values('p_value', ascending=True,inplace=True)
    fish_diff_case_control.to_csv("fish_diff_case_control.csv")
    print(fish_diff_case_control.head())

fish_diff_case_control = pd.read_csv("fish_diff_case_control.csv")
fish_diff_case_control = fish_diff_case_control[fish_diff_case_control['GENE_NAME'] != "nan"]
print(fish_diff_case_control.head())

# Numbers of pairs of bars you want
N = 10
# Data on X-axis
green_bar = list(fish_diff_case_control['p_value'][1:11].tolist())
ind = np.arange(N)
# Figure size
plt.figure(figsize=(10,10))
# Width of a bar
width = 0.50
# Plotting
plt.bar(ind, green_bar, width, label='Cases',color=(0.2, 0.4, 0.6, 0.6))
plt.xlabel('Gene name')
plt.title('Ten lowest Fisher-Test P-values for Case vs Control Changed Gene frequency')
plt.xticks(ind, fish_diff_case_control['GENE_NAME'][1:11].tolist(),rotation=30)
plt.savefig("Top_Fishers.jpg")
plt.show()

