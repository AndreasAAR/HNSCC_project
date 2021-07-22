# Title     : TODO
# Objective : TODO
# Created by: anahrl
# Created on: 2021-07-18

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


library('biomaRt')
mart <- useDataset("hsapiens_gene_ensembl", useMart("ensembl"))
genes <- #my in-data
G_list <- getBM(filters= "ensembl_gene_id", attributes= c("ensembl_gene_id" ,  "hgnc_symbol"),values=genes,mart= mart)