import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

prevalence_df = pd.read_csv('Resources/Base_Data/Gene_Prevalences.csv')
prevalence_df.columns=prevalence_df.columns.str.strip()
graph_df = prevalence_df.sort_values(by=['absolute_overrepresentation'], ascending= False).iloc[1:11,:]
print(graph_df[['name','case_percentage','id']])
print(graph_df.columns)
top_case = graph_df[['name','case_percentage']]
top_control = graph_df[['name','control_percentage']]
top_number_case = graph_df[['name','num_mutations_case']]
top_number_control = graph_df[['name','num_mutations_control']]

#Adding case values
case_percentage = top_case['case_percentage'].to_list()
print(case_percentage)
case_number = list(top_number_case['num_mutations_case'].to_list())

#Adding control values
control_percentage = top_control['control_percentage'].to_list()
control_number = top_number_control['num_mutations_control'].to_list()


sns.set()
plt.figure()

# This is where the actual plot gets made
ax = sns.barplot(data=graph_df, x="year", y="seats", hue="party", palette=['Green', 'Dark Green'], saturation=0.6)

# Customise some display properties
ax.set_title('UK election results')
ax.grid(color='#cccccc')
ax.set_ylabel('Seats')
ax.set_xlabel(None)
ax.set_xticklabels(df["year"].unique().astype(str), rotation='vertical')

# Ask Matplotlib to show it
plt.show()