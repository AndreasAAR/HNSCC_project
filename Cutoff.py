from collections import Counter

def write_cutoff_list(data_frame, cutoff, list_name):
    gene_list = data_frame.values.flatten().tolist()
    genes_count = Counter(gene_list)
    print(len(genes_count))
    interesting_genes = {}
    for name, number in genes_count.items():
        if number > cutoff:
            interesting_genes[name] = number

    print(len(interesting_genes))

    textfile = open(list_name, "w")
    for name, number in interesting_genes.items():
        textfile.write(str(name) + "," + str(number) + "\n")
    textfile.close()
    return interesting_genes

