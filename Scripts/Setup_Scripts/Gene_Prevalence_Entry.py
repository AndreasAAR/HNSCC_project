patient_number_cases = 17
patient_number_controls = 18
import numpy as np

class Gene_Prevalence_Entry:
  def __init__(self, id, name ,number_case, number_control):
    self.id = id
    self.number_case = number_case if number_case != None else 0
    self.number_control = number_control if number_control != None else 0
    self.name = name
    if number_case == None:
      number_case = 0
    if number_control == None:
      number_control = 0

    total = (number_case+number_control)
    self.case_fold = number_case/total
    self.control_fold = -number_control/ total
    self.case_percentage = (number_case/patient_number_cases)*100
    self.control_percentage = (number_control/patient_number_controls)*100
    self.absolute_overrepresentation = np.absolute(self.case_percentage-self.control_percentage)

def print_entries(entries,file_name):
  textfile = open(file_name, "w")
  textfile.write("id,name,num_mutations_case,num_mutations_control,case_fold, control_fold,"+
                 "case_percentage,control_percentage, absolute_overrepresentation"+"\n")
  for name, entry in entries.items():
    textfile.write(str(entry.id) + ","
                   + str(entry.name) + ","
                   + str(entry.number_case) + ","
                   + str(entry.number_control) + ","
                   + str(round(entry.case_fold,2)) + ","
                   + str(round(entry.control_fold, 2)) + ","
                   + str(round(entry.case_percentage, 2)) + ","
                   + str(round(entry.control_percentage, 2)) + ","
                   + str(round(entry.absolute_overrepresentation, 2))
                   + "\n")
  textfile.close()



