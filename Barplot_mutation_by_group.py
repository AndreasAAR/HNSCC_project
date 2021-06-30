import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# https://opensource.com/article/20/4/plot-data-
# Create plotly diagram to show off too!

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


# Numbers of pairs of bars you want
N = 10

# Data on X-axis

# Specify the values of blue bars (height)

green_bar = list(case_percentage)
# Specify the values of orange bars (height)
dark_green_bar = list(control_percentage)


# Position of bars on x-axis
ind = np.arange(N)

# Figure size
plt.figure(figsize=(10,5))

# Width of a bar
width = 0.20



# Plotting
plt.bar(ind, green_bar, width, label='Cases',color=(0.2, 0.4, 0.6, 0.6))
plt.bar(ind + (width), dark_green_bar , width, label='Controls',color=(0.2, 0.7, 0.6, 0.6))

plt.xlabel('Gene name')
plt.ylabel('Percentage mutated')
plt.title('Percentage carrying gene mutation')

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations


plt.xticks(ind + width / 2, top_number_control.name)
plt.rcParams['axes.edgecolor']='#333F4B'
plt.rcParams['axes.linewidth']=0.8
plt.rcParams['xtick.color']='#333F4B'
plt.rcParams['ytick.color']='#333F4B'

#Styling
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Helvetica'




# Finding the best position for legends and putting it
plt.legend(loc='best')
plt.savefig('Graphs/Mutation_Prevalence.jpg', dpi = 100)
plt.show()



if False:


    ax = fig.add_subplot(111)
    rects1 = ax.bar(ind, menMeans, width, color='royalblue', yerr=menStd)

    womenMeans = (25, 32, 34, 20, 25)
    womenStd =   (3, 5, 2, 3, 3)
    rects2 = ax.bar(ind+width, womenMeans, width, color='seagreen', yerr=womenStd)

    # add some
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )

    ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )

    plt.show()