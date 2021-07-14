import subprocess  as sp


# Are all genes equal in pathway,
infile = "../../Resources/Base_Data/Gene_Prevalences.csv"
outfile = "../../Resources/Intermediary_Data/GENE_names_to_Pathways_raw.csv"
column_with_names = "2"

retcode = sp.call("Rscript R_Scripts/BiomaRt_GENE_names_to_Pathways.R "
                  + infile + " " + outfile + " " + column_with_names
                  , shell=True)

