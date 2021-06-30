import pandas as pd

class Name_getter():
    # API calls for gene name list moved
    def __init__(self):
        df = pd.read_csv('../../Resources/Base_Data/All_names.csv', sep=',')
        self.name_list = dict(zip(df.id,df.name))

    def get_name_list(self):
        return self.name_list



