import mysql.connector as mysql

#ENSG Codes: DATABASE: hg38  TABLE: wgEncodeGencodeAttrsV20
    #-geneId	ENSG00000223972.5	varchar(255)	values
    #-geneName	DDX11L1	varchar(255)	values
    #-geneType	transcribed_unprocessed_pse...	varchar(255)	values
    #-geneStatus	KNOWN	varchar(255)	values
    #-transcriptId	ENST00000456328.2	varchar(255)	values

#Could be used to get name for old ensembl IDs!!!

db = mysql.connect(
    host = "genome-euro-mysql.soe.ucsc.edu",
    user = "genome",
    database = "hg38"
)

print(db)
## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

## defining the Query
#query = "SHOW columns FROM knownGene"
#query = "SHOW columns FROM kgXref"
#query = "SELECT kgID FROM knownGene, kgXref WHERE kgXref.kgId=knownGene.name LIMIT 10;"
query = "SELECT  geneName  FROM wgEncodeGencodeAttrsV37 LIMIT 10;"
###query = "SELECT kgID FROM Genes LIMIT 10;"
## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)

