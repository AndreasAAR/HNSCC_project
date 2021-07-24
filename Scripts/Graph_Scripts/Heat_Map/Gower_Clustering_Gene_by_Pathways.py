import pandas as pd
import numpy as np
from sklearn.neighbors import DistanceMetric
import gower
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import ClusterWarning
from warnings import simplefilter
simplefilter("ignore", ClusterWarning)

# Article used
# https://medium.com/analytics-vidhya/concept-of-gowers-distance-and-it-s-application-using-python-b08cf6139ac2
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html


# *TODO: might be worth thinking if patients should be grouped on "all clusters for patient",
#   TODO:cont. this could give interesting information.
# Uses gowers on the pathways for each gene to cluster them by pathway.
if False:
    pw_df = pd.read_csv("../../../Resources/Data/Intermediary_Data/GENE_names_to_Pathways_raw.csv")

    # First we need to make them unique for each collumn, so they can be properly sorted out.
    pw_set = set()
    pw_set.update(pw_df.values.tolist()[0])

    # We set up the structure we want in our dataset:
    pw_bool_df = pd.DataFrame(columns = pw_df.columns,index= pw_set)

    #Function to return 0 or 1 for yes or no
    def has_gene(row):
        new_row = []
        for gene in row.index:
            #print("row.name {}",row.name)
            #print("gene{}", gene)
            #print(pw_df[gene])
            row[gene] = row.name in list(pw_df[gene])
            #new_row.append(row.name in list(pw_df[gene]))

        return row

    pw_bool_df.apply(has_gene,axis = 1)
    print(pw_bool_df.head())
    pw_bool_df.to_csv("gene_pathway_boolean.csv")

# A true/false dataframe for each pathway
pw_df = pd.read_csv("gene_pathway_boolean.csv",index_col=0)
print(pw_df.head())
pw_df = pw_df.transpose()
print(pw_df.head())

cluster_data = pw_df.astype(float)
print(cluster_data.head())
print(cluster_data.dtypes.head())

dist_df = gower.gower_matrix(cluster_data)

Z = linkage(dist_df, 'ward')
print(Z)
fig = plt.figure(figsize=(25, 10))
dn = dendrogram(Z)
plt.show()