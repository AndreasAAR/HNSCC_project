import pandas as pd
import numpy as np
from sklearn.neighbors import DistanceMetric
import gower
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import ClusterWarning
from warnings import simplefilter

from sklearn.preprocessing import StandardScaler

simplefilter("ignore", ClusterWarning)
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Article used
# https://medium.com/analytics-vidhya/concept-of-gowers-distance-and-it-s-application-using-python-b08cf6139ac2
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

# *TODO: might be worth thinking if patients should be grouped on "all clusters for patient",
#   TODO:cont. this could give interesting information.
# Uses gowers on the pathways for each gene to cluster them by pathway.

pw_df = pd.read_csv("../../../Resources/Data/Intermediary_Data/GENE_names_to_Pathways_raw.csv", dtype = str)
def create_boolean_data():

    # First we need to make them unique for each collumn, so they can be properly sorted out.
    pw_set = set()
    pw_set.update(pw_df.values.tolist()[0])
    # We set up the structure we want in our dataset:
    pw_bool_df = pd.DataFrame(columns = pw_df.columns, index= pw_set, dtype=str)
    pw_bool_df.apply(has_gene, axis=1)
    pw_bool_df = pw_bool_df.astype(str)
    pw_bool_df.index = ["hsa" + str(pw) for pw in pw_bool_df.index]
    pw_bool_df.to_csv("gene_pathway_boolean.csv")

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

# create_boolean_data()
# A true/false dataframe for each pathway
boolean_df = pd.read_csv("gene_pathway_boolean.csv",
                         index_col=0)

boolean_df = boolean_df.transpose()
cluster_data = boolean_df.astype(float)

# TODO Try to use value of string instead of 1,
# To make values more non-binary.
# Try to

# We have to find the optimal clustering of k-means to
# Figure out the desired level of clusters.

def find_cluster_silhouette(cluster_data):
    sil = []
    kmax = 35 #If we assume every person is its own cluster
    # dissimilarity would not be defined for a single cluster, thus, minimum number of clusters should be 2
    for k in range(2, kmax+1):
      kmeans = KMeans(n_clusters = k).fit(cluster_data)
      labels = kmeans.labels_
      print(labels)
      sil.append(silhouette_score(cluster_data, labels, metric = 'euclidean'))
    #5 Seems to be superior
    plt.plot(sil)
    plt.show()
    plt.savefig("Sillhouette_Scores_Clusters")

find_cluster_silhouette(cluster_data)

def find_hierarchical_clusters(cluster_data):
    dist_df = gower.gower_matrix(cluster_data)
    Z = linkage(dist_df, 'ward')
    #print(Z)
    fig = plt.figure(figsize=(30, 15))
    dn = dendrogram(Z)
    plt.show()
    plt.savefig("Hierarchical_Clusters")

find_hierarchical_clusters(cluster_data)


# We will in the long run give average clusters to the groups,
# By randomizing the collumns!
def get_clustering(cluster_data,k):

    cluster_list = [[] for _ in range(len(cluster_data.index))]
    for i in range(k):
        cluster_data = cluster_data[np.random.permutation(cluster_data.columns)]
        cluster = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')
        cluster.fit_predict(cluster_data)
        for a,b in zip(cluster_list, cluster.labels_):
            a.append(b)



    cluster_list = [max(set(a), key = a.count) for a in cluster_list]
    print(len(set(cluster_list)))
    return cluster_list


clusters = get_clustering(cluster_data,6)

def plot_important_features():
    X_train, X_test, y_train, y_test = train_test_split(
        cluster_data, clusters, stratify=clusters, random_state=42)

    forest = RandomForestClassifier(random_state=0)
    forest.fit(X_train, y_train)

    result = permutation_importance(
    forest, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2)

    forest_importances = pd.Series(result.importances_mean, index=cluster_data.columns)

    forest_importances = forest_importances.nlargest(n=5, keep='first')
    #need to cut out five most important
    fig, ax = plt.subplots()
    forest_importances.plot.bar(ax=ax)
    ax.set_title("Feature importances using permutation on full model")
    ax.set_ylabel("Mean accuracy decrease")
    fig.tight_layout()
    plt.show()
    plt.savefig("Most_differentiating_pathways")
    return forest_importances, forest


forest_importances, forest = plot_important_features()
forest_importances = [x+1 for x in forest_importances]

print("hello")

clustered_data = cluster_data
clustered_data["clusters"] = clusters
print(cluster_data.head())

#print("importances")
#print(forest_importances)


cluster_counts = clustered_data.groupby(['clusters']).sum()
cluster_counts["amount_members"] = clustered_data.groupby(['clusters']).size()
print(cluster_counts.head())
print(cluster_counts.div(cluster_counts.amount_members, axis=0).head())



# TODO PCA on variables for which cluster we got first time from k-means cluster
# PCA to cluster variables
# acc to : https://www.ibm.com/support/pages/clustering-binary-data-k-means-should-be-avoided

#Standardizing with our cluster from the k-means:


values = StandardScaler().fit_transform(cluster_data)
pca_cluster_data = pd.DataFrame(values, columns=cluster_data.columns, index=cluster_data.index)

print("cluster data")
cluster_data.drop('clusters',axis = 1)
print(cluster_data)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(pca_cluster_data)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])



# TODO: Cluster again
#THen we will cluster again, using the principle component scores we got out!

clusters = get_clustering(principalDf,6)
cluster_data["clusters"] = clusters
print(cluster_data.head())

#print("importances")
#print(forest_importances)


cluster_counts = cluster_data.groupby(['clusters']).sum()
cluster_counts["amount_members"] = cluster_data.groupby(['clusters']).size()
print(cluster_counts.head())
print(cluster_counts.div(cluster_counts.amount_members, axis=0).head())