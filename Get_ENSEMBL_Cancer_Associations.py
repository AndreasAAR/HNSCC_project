import requests, sys

server = "https://rest.ensembl.org"
ext = "/phenotype/gene/homo_sapiens/ENSG00000003393?include_associated=1"

r = requests.get(server + ext, headers={"Content-Type": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()
print(repr(decoded))

if False:
    prevalence_df = pd.read_csv('Resources/Base_Data/Gene_Prevalences.csv')
    prevalence_df.columns=prevalence_df.columns.str.strip()
    graph_df = prevalence_df.sort_values(by=['absolute_overrepresentation'], ascending= False).iloc[1:6,:]
    print(graph_df.columns)
