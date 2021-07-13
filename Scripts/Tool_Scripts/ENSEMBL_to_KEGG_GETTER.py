import subprocess  as sp


# Are all genes equal in pathway,
infile = "../../Resources/Base_Data/Gene_Prevalences.csv"
outfile = "../../Resources/Base_Data/Raw_Gene_to_Pathways.csv"
column_with_names = "2"

retcode = sp.call("Rscript R_Scripts/BiomaRt_ENSEMBL_to_KEGG_ID.R "
                  + infile + " " + outfile + " " + column_with_names
                  , shell=True)

