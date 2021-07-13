#if (!requireNamespace("BiocManager", quietly = TRUE))
#    install.packages("BiocManager")

#BiocManager::install("org.Hs.eg.db")
library(org.Hs.eg.db)

args = commandArgs(trailingOnly=TRUE)
sym = c(args)

input_file = sym[1]
output_file = sym[2]
name_col = sym[3]
name_col = strtoi(name_col)

in_df = read.csv(input_file)
print(head(in_df))

name_exists = in_df[,c('name')] != 'name not found'
name_df = in_df[ name_exists , c(name_col)]
print(name_df)


sym = as.vector(name_df)
##Get the Entrez gene IDs associated with those symbols
EG_IDs = mget(sym, revmap(org.Hs.egSYMBOL),ifnotfound=NA)
print(EG_IDs)

##Then get the KEGG IDs associated with those entrez genes.
KEGG_IDs = mget(as.character(EG_IDs), org.Hs.egPATH,ifnotfound=NA)
print(KEGG_IDs)
