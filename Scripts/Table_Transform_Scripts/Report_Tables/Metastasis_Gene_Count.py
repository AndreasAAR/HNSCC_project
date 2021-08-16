from os import listdir
from os.path import isfile, join
import pandas as pd
import re
from collections import Counter



mypath = "../../../Resources/Data/Source_Data/Metastasis_Data"
metasfiles = [mypath + "/" + f for f in listdir(mypath) if (isfile(join(mypath, f)) and "metastas-all" in f and (not "high" in f ))]
relapfiles = [mypath + "/" + f for f in listdir(mypath) if (isfile(join(mypath, f)) and "relapse-all" in f  and (not "high" in f ))]

print(metasfiles)
print(relapfiles)

def get_metastasis_counts(pattern,files):
    patient_genes = {}
    only_genes = []
    for case in files:
        df = pd.read_csv(case,sep="\t")
        p = re.compile(pattern + "-(\d{1,2})")
        result = p.search(case)
        case_name = result.group(0)
        genes =  list(set(df['GENE']))
        #ENSG_dict = pd.Series(df['GENE'].values,index = df['GENE']).to_dict()
        patient_genes[case_name] = [x for x in genes]
        only_genes.append(genes)
        #ensg_names.update(ENSG_dict)

    res_df = pd.DataFrame()
    for patient in patient_genes.items():
        item_ls = list(patient)
        res_df[item_ls[0]] = pd.Series(item_ls[1])

    case_list = res_df.values.tolist()
    case_list = [val for sublist in case_list for val in sublist]
    return Counter(case_list)

relap_dict = get_metastasis_counts("Case",relapfiles)
metas_dict = get_metastasis_counts("Case",metasfiles)




metas_df = pd.DataFrame.from_dict(metas_dict,orient = "index")
relap_df = pd.DataFrame.from_dict(relap_dict,orient = "index")
metas_df.to_csv("Metastasis_Genes.csv",sep= ";")
relap_df.to_csv("Relapse_Genes.csv",sep= ";")

# Load in ENSG and Gene name from original data
# Merge onto the gene name in the counts/requency mestastas table


