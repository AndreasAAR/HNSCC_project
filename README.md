# HNSCC_project

## Subject for project repo
Mainly for easy access on several devices for myself, but also for inspiration for
how to work with your sequencing data, using pandas dataframes, and getting gene-annotation data
from databanks via API, in this case ENSEMBL.
Later on I will share the resulting publication and graph and modelling techniques.
The ENSEMBL archived data retrieval framework in perl is not mine, but the module retrieving name and description data from IDs using Perl and Python is written by me. 
:panda_face: :snake:

![Graph of mutation prevalence in gene per group](https://github.com/AndreasAAR/HNSCC_project/blob/master/Graphs/Mutation_Prevalence.jpg?raw=true)


## TODO
1. Heatmap, each patient, important genes, and the level of change for those genes.
   * List of each individual generated to be merged together.
2. Graph on shared pathways in common genes in each patient group, colored by group, size by
percentage having the change. :snail:
  * K-means Clustering gave 5 clusters (/) 
  * Hierarchical clustering (/)
  * Add description to pathways, check out if there is some way to make them related, and add a non binary row.
  * * One way could be to download related pathways, and cluster the pathways on related pathways, add this as a categorical marker instead of the binary value, and then create a "number of pathways in cluster" clustering instead, and look at the clusters of pathways for each gene instead, to give it a broader cluster of pathways it could belong to, and then let the decision trees weigh what the new clusters "cluster of cluster" values would belong to. So TP53 could have mainly cluster A and B pathways, and maybe cluster B put it an SNURP4 in the same cluster. Cluster B might contain maybe mainly 4500 number genes for cell-skeleton adhesion, and this could be the final name for the cluster they get put into. Giving extra attributes by a numerical value and relating genes to eachother might give more context to the clustering.  I will probably proceed as is however as there is no clear benefit to be honmest of either situation.
  * Frequent itemset mining to investigate possible related genes, cluster these, make them an additional non binary row.
    
