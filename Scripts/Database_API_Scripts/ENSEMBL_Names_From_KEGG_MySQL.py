import mysql.connector as mysql
import pandas as pd

name_table = pd.read_csv("../../Resources/Base_Data/name_list.csv")

id_name= name_table[["GENE_ID","GENE"]]
#print (id_name.head())
no_name= id_name[id_name.GENE=="name not found"]
#print (no_name.head())

just_id= no_name["GENE_ID"].to_list()
print (just_id[0:5])

# Query_id= str(just_id).replace("[","(")
# Query_id= Query_id.replace("]",")")
# print (Query_id)

print(len(just_id))

db = mysql.connect(
    host="genome-euro-mysql.soe.ucsc.edu",
    user="genome",
    database="hg19"
)

def get_kegg_v37_name(ensembl_id):
    ensembl_id = str(ensembl_id)
    cursor = db.cursor()
    query = "SELECT  geneId,geneName  FROM wgEncodeGencodeAttrsV37lift37 WHERE geneId LIKE " + "'" +ensembl_id + '%\'' + ";"
    cursor.execute(query)
    # fetching all records from the 'cursor' object
    records = cursor.fetchall()

    if(len(records) == 1):
        record_list = list(records[0])
        print(record_list)
        return record_list[1]
    else:
        return "name not found"

new_names = [get_kegg_v37_name(id) if gene == 'name not found' else gene for gene, id in zip(id_name.GENE,id_name.GENE_ID)]
id_name.loc[:,'GENE'] = new_names
id_name.to_csv("../../Resources/Assisting_Data/name_list_v37_ensembl.csv")

# This will use old ENSEMBL IDs to find the gene names!
# We will use version GRCh37 of ENSEMBL from KEGG to find the names.

# print(db)
# creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'


# defining the Query

# query = "SELECT kgID FROM Genes LIMIT 10;"
# getting records from the table

