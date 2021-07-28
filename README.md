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
  * Frequent itemset mining to investigate possible related genes, cluster these, make them an additional non binary row.
    
