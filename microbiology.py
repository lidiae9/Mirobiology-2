import pandas as pd
import matplotlib.pyplot as pyplot
import pylab

#Paired bacterial count of the Kelvin River.
#importing data from a csv file
data = pd.read_csv('/Users/lidiaerrico/workspace/matplot/bacteria.csv')

#first we define the two variables we want to look at from the whole data set.
countat22 = data['Count_at_22_degrees']
countat37 = data['Count_at_37_degrees']

#since the data from the Luggie and Kelvin river wasn't separated, now we split the River variable into Luggie and Kelvin - so we can analyze one at a time.
data_Luggie = data.loc[data['River'] == 'Luggie']
data_Kelvin = data.loc[data['River'] == 'Kelvin']

#now we separate the count at 22 and 37 degrees from one another for the same river. 
data_Kelvin_countat22 = data_Kelvin['Count_at_22_degrees']
data_Kelvin_countat37 = data_Kelvin['Count_at_37_degrees']

#label for the x axis
label=['22','37']

#square brackets very important because we want to impose two data-sets on the same graph, color=black makes the graph monochromatic.
pyplot.plot([data_Kelvin_countat22,data_Kelvin_countat37], color='black')
#allows me to define the number of ticks on the x-axis and then label them.
pyplot.xticks((0,1+0, 1.0), labels=label)

pyplot.title('Matplot showing the paired bacterial counts of water samples from Kelvin River at 22 ℃  and 37℃. ')
pyplot.xlabel("Temperature (Celsius)")
pyplot.ylabel("Bacterial Count (cfu/ml)")

pyplot.figtext(.109, .04,'Figure 1. Matplot showing the paired bacterial counts of water samples from Kelvin River at 22 ℃  and 37℃. Data was generated from 26 samples of the same river water. ')

pyplot.show()


#########################################################################################################################################################################
#Paired bacterial count of the Luggie River.

data_Luggie = data.loc[data['River'] == 'Luggie']

#since the data from the Luggie and Kelvin river wasn't separated, now we split the River variable into Luggie and Kelvin - so we can analyze one at a time.
data_Luggie_countat22 = data_Luggie['Count_at_22_degrees']
data_Luggie_countat37 = data_Luggie['Count_at_37_degrees']

label=['22','37']

pyplot.plot([data_Luggie_countat22,data_Luggie_countat37], color='black')
pyplot.xticks((0,1+0, 1.0), labels=label)

pyplot.title('Matplot showing the paired bacterial counts of water samples from Luggie River at 22 ℃  and 37℃. ')
pyplot.xlabel("Temperature (Celsius)")
pyplot.ylabel("Bacterial Count (cfu/ml)")

pyplot.figtext(.109, .04,'Figure 1. Matplot showing the paired bacterial counts of water samples from Luggie River at 22 ℃  and 37℃. Data was generated from 26 samples of the same river water. ')

pyplot.show()

#########################################################################################################################################################################

#Boxplot showing the ratio of colony forming units for both rivers.

#first we define the variables we want to look at from the whole data set.
ratio = data['Ratio']

#since the data from the Luggie and Kelvin river wasn't separated, now we split the River variable into Luggie and Kelvin - so we can analyze one at a time.
data_Luggie = data.loc[data['River'] == 'Luggie']
data_Kelvin = data.loc[data['River'] == 'Kelvin']

#now we separate the count at 22 and 37 degrees from one another for the same river. 
data_Kelvin_ratio= data_Kelvin['Ratio']
data_Luggie_ratio = data_Luggie['Ratio']

label=('22', '37')

fig7, ax7 = pyplot.subplots()
ax7.set_title('Boxplot showing the ratio of colony forming units at 22 ℃  and 37℃ for the Kelvin and Luggie river. ')
ax7.set_ylabel('Ratio')
ax7.set_xlabel('River')
ax7.boxplot([data_Kelvin_ratio, data_Luggie_ratio],labels= label) 

pyplot.show()