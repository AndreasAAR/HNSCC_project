# Title     : TODO
# Objective : TODO
# Created by: anahrl
# Created on: 2021-07-13

#if (!requireNamespace("BiocManager", quietly = TRUE))
#    install.packages("BiocManager")
#if (!requireNamespace("plyr", quietly = TRUE))
#install.packages("plyr")
#BiocManager::install("org.Hs.eg.db")
library(org.Hs.eg.db)
library(plyr)

args = commandArgs(trailingOnly=TRUE)
sym = c(args)

input_file = sym[1]
output_file = sym[2]
name_col = sym[3]
name_col = strtoi(name_col)

in_df = read.csv(input_file)

name_exists = in_df[,c('name')] != 'name not found'
name_df = in_df[ name_exists , c(name_col)]
#print(name_df)

sym = as.vector(name_df)
##Get the Entrez gene IDs associated with those symbols
EG_IDs = mget(sym, revmap(org.Hs.egSYMBOL),ifnotfound=NA)
#print(EG_IDs)

##Then get the KEGG IDs associated with those entrez genes.
#Hs.egPATH for PATH information!
KEGG_IDs = mget(as.character(EG_IDs), org.Hs.egPATH,ifnotfound=NA)
#Switching names from KeggID to Gene_name
names(KEGG_IDs) = sym
PATHWAY_ENTRIES = KEGG_IDs[ KEGG_IDs != 'NA' ]
NA_df = data.frame(lapply(PATHWAY_ENTRIES, "length<-", max(lengths(PATHWAY_ENTRIES))))
colnames(NA_df) = names(PATHWAY_ENTRIES)
#df_name_KEGG_ID = data.frame(KEGG_IDs)
#colnames(df_name_KEGG_ID) = c("Gene_Names","KEGG_IDs")
print(head(NA_df))

write.csv( NA_df,output_file, row.names = FALSE)
