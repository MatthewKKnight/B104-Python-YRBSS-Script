# Programmers: Matthew Knight, Nate Gosdin
# Course: B104
# Assignment: Final Project

# What is the relationship between Physical Altercations and Alcohol Use?

import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from pandas import *

# This def was created to clean up our code so we wouldn't have so many dashes throughout our script.
def NumLine():
    print('\n---------------------------------------------------------------------------------------')
        
# This variable was created so that we could input our data into Python.
data = pd.read_csv('Datasheet.csv')

# This variable was created for the from pandas import * so that our for loop would execute.
df = read_csv('Datasheet.csv')

# This is our def we created for the dashes in our console.
NumLine()

# Our crosstable helped in making sure our numbers from our data set were correct.
print('Crosstable:\n')
Crosstable = pd.crosstab(data.q41, data.q17, margins=True,
                            rownames=["Q41"], 
                            colnames=["Q17"])
print(Crosstable)

# This variable was made to grab certain questions from our data file.
data2 = data[['q1','q2','q3','q4','q6','q7','q17','q41']]

# This variable was made so that the heatmap could find our correlation.
corr = data2.corr()

# Heatmap X and Y Labels.
x_axis_labels = ['Age', 'Sex', 'Grade', 'Latino', 'Height', 'Weight', 'Physical Altercations', 'Alcohol Consumed']
y_axis_labels = ['Age', 'Sex', 'Grade', 'Latino', 'Height', 'Weight', 'Physical Altercations', 'Alcohol Consumed']

# Heatmap of the Relationship between Alcohol Use and Physical Altercations.
fig, ax = plt.subplots()
fig.set_size_inches(11, 7)
sns.heatmap(corr, annot=True, fmt = ".1f", cmap = "RdBu", center=0,ax=ax, xticklabels=x_axis_labels, yticklabels=y_axis_labels\
            , vmin=-1, vmax=1).set(title='Relationship between Alcohol Use and Physical Altercations')
plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------

# These variables are for each possible answer on the YRBS Survey for Question 17.
oneCounter = 0
twoCounter = 0
threeCounter = 0
fourCounter = 0
fiveCounter = 0
sixCounter = 0
sevenCounter = 0
eightCounter = 0
nanCounter = 0

# This variable grabs only Question 17 from our data file.
quest17 = data['q17']

# This for loop was made so that Question 17 has all of its answers from the survey put into different variables so that we could have our data 
# easily accesible for our charts and graph. Each variable starts at 0, then the for loop reads through each answer in our data file and
# will add +1 to it so that the code will output the correct amount of answered questions for each possible answer.
for answer in quest17:
    if(answer == 1):
        oneCounter = oneCounter + 1
    elif(answer == 2):
        twoCounter = twoCounter + 1
    elif(answer == 3):
            threeCounter = threeCounter + 1
    elif(answer == 4):
            fourCounter = fourCounter + 1
    elif(answer == 5):
            fiveCounter = fiveCounter + 1
    elif(answer == 6):
            sixCounter = sixCounter + 1
    elif(answer == 7):
            sevenCounter = sevenCounter + 1
    elif(answer == 8):
            eightCounter = eightCounter + 1
    else:
        nanCounter = nanCounter + 1

#----------------------------------------------------------------------------------------------------------------------------------------  

not_fought = oneCounter
fought = twoCounter+threeCounter+fourCounter+fiveCounter+sixCounter+sevenCounter+eightCounter
no_answer = nanCounter

NumLine()

print('People who have, have not, and did not answer to being in Physical Altercations:')

print(f'\nThe sum of people who have not been in a physical altercation is {not_fought}.')

print(f'\nThe sum of people who have been in a physical altercation is {fought}.')

print(f'\nThe sum of people who did not answer {no_answer}.')

#----------------------------------------------------------------------------------------------------------------------------------------  

# The x variable is the sum of people who have been in physical altercations.
x = twoCounter+threeCounter+fourCounter+fiveCounter+sixCounter+sevenCounter+eightCounter

# The y variable is the sum of people who haven't been in physical altercations.
y = oneCounter

# The nan variable is the sum of people who did not answer Question 17.
nan = nanCounter

# Chart variable is an array of our previous variables to put into our chart.
chart = np.array([x, y, nan])

# Chart Labels
mylabels = ["Fought", "Not Fought","No answer"]

# Chart Colors
mycolors = ["#6495ED", "#D3D3D3", "#00008B"]

# Fought vs Not Fought vs No answer Pie Chart.
plt.pie(chart,labels=mylabels,autopct='%1.1f%%')
plt.pie(chart, labels = mylabels, colors=mycolors)
plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------

# These variables are for each possible answer on the YRBS Survey for Question 41.
oneCounter = 0
twoCounter = 0
threeCounter = 0
fourCounter = 0
fiveCounter = 0
sixCounter = 0
sevenCounter = 0
nanCounter = 0
quest41 = data['q41']

# This is the same layout as our previous for loop, this one was used for Question 41 from the 2019 YRBS Survey.
for row in quest41:
    if(row == 1):
        oneCounter = oneCounter + 1
    elif(row == 2):
        twoCounter = twoCounter + 1
    elif(row == 3):
            threeCounter = threeCounter + 1
    elif(row == 4):
            fourCounter = fourCounter + 1
    elif(row == 5):
            fiveCounter = fiveCounter + 1
    elif(row == 6):
            sixCounter = sixCounter + 1
    elif(row == 7):
            sevenCounter = sevenCounter + 1
    else:
        nanCounter = nanCounter + 1
        
#----------------------------------------------------------------------------------------------------------------------------------------   
    
alcohol = twoCounter+threeCounter+fourCounter+fiveCounter+sixCounter+sevenCounter
no_alcohol = oneCounter

NumLine()

print('People who have and have not consumed alcohol:')

print(f'\nThe sum of people who have not drank alcohol in the past 30 days is {no_alcohol}.')

print(f'\nThe sum of people who have drank alcohol in the past 30 days is {alcohol}.')

#----------------------------------------------------------------------------------------------------------------------------------------  

x1 = twoCounter+threeCounter+fourCounter+fiveCounter+sixCounter+sevenCounter+eightCounter
y1 = oneCounter
chart1 = np.array([x1, y1])
mylabels1 = ["Consumed", "Not Consumed"]
mycolors1 = ["#6495ED", "#D3D3D3"]

# Consumed vs Not Consumed Alcohol Pie Chart.
plt.pie(chart1,labels=mylabels1,autopct='%1.1f%%')
plt.pie(chart1, labels = mylabels1, colors=mycolors1)
plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------

# These variables are for each possible answer on the YRBS Survey for Question 3.
oneCounter = 0
twoCounter = 0
threeCounter = 0
fourCounter = 0
fiveCounter = 0
nanCounter = 0
quest3 = data['q3']

# This is the same layout as our previous for loops, this one was used for Question 3 from the 2019 YRBS Survey.
for row in quest3 :
    if(row == 1):
        oneCounter = oneCounter + 1
    elif(row == 2):
        twoCounter = twoCounter + 1
    elif(row == 3):
            threeCounter = threeCounter + 1
    elif(row == 4):
            fourCounter = fourCounter + 1
    elif(row == 5):
            fiveCounter = fiveCounter + 1
    else:
        nanCounter = nanCounter + 1
        
#----------------------------------------------------------------------------------------------------------------------------------------      
         
NumLine()

print('Grade Of Survey Takers:')

print(f'\nThe sum of people who are in 9th grade is {oneCounter}.')

print(f'\nThe sum of people who are in 10th grade is {twoCounter}.')

print(f'\nThe sum of people who are in 11th grade is {threeCounter}.')

print(f'\nThe sum of people who are in 12th grade is {fourCounter}.')

print(f'\nThe sum of people who are ungraded or in another grade is {fiveCounter}.')

#----------------------------------------------------------------------------------------------------------------------------------------

# Bar Graph of the Grade of Survey Takers.
Grade = ['9th Grade','10th Grade','11th Grade','12th Grade','Ungraded']

# The Bar variable is an array of our previous variables from our for loop, that are put into our chart.
Bar = np.array([oneCounter, twoCounter, threeCounter, fourCounter, fiveCounter])

# Grade of Survey Takers Bar Graph.
plt.bar(Grade, Bar)
plt.title('Grade of Survey Takers')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.show()

NumLine()
#----------------------------------------------------------------------------------------------------------------------------------------