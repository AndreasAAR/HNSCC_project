import pandas as pd
import Scripts.Tool_Scripts.ENSEMBL38_37_KEGG_Name_Getter as gg

df = pd.read_csv("common-genes-all-KEGG.csv", sep = ";")
df.columns=['Gene_id','Pathway_id','Gene_name','Pathway_name']
df_na = df.loc[df['Gene_name'].isna()]
Gene_ids =  df_na['Gene_id']
print("num gene ids {}",len(Gene_ids))
print(df_na.head())

results = []
for gene in Gene_ids:
    print(gene)
    try:
       res = gg.get_gene_name_or_desc(gene)
    except ConnectionResetError:
        res = "name_not_found"
    results.append(res)
    print(res)

print(results)

df_Gene_names = pd.DataFrame(results, columns=["Gene_name"])
df_Gene_names.to_csv('Gene_names.csv', index=False)
print("finished")