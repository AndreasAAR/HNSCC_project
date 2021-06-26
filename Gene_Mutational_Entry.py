import Name_getter as ng
patient_number_cases = 17
patient_number_controls = 18
import numpy as np

class Gene_Mutational_Entry:
  def __init__(self, chromosome, dp, type, effect,impact,):
      self.id = id
      self.chromosome
      self.type
      self.effect
      self.impact
      self.gene
      self.gene_id
      self.Feature
      self.transcript_ID
      self.Biotype
    #CHR
    #START
    #END
    #DP
    #TYPE
    #EFFECT
    #IMPACT
    #GENE
    #GENE_ID
    #FEATURE
    #TRANSCRIPT_ID
    #BIOTYPE

def print_entries(entries,file_name):
  textfile = open(file_name, "w")
  textfile.write("id,name,number_case,number_control,case_fold, control_fold,"+
                 "case_percentage,control_percentage, absolute_overrepresentation"+"\n")
  for name, entry in entries.items():
    textfile.write(str(entry.id) + "," + "\n")
  textfile.close()

