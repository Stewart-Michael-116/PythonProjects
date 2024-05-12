# Week 6 Bayes Analysis Stewart
# Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.

''' INSTRUCTIONS:

Run The Python Script. 
Notice how the script analyzes a sample dataset and presents tables based on it.
Enter your own test case according to the script's requests.
The script will guess if your lawn will be yellow or green based on your test information.

'''

from sklearn.naive_bayes import GaussianNB
import numpy as np
from tabulate import tabulate
from collections import Counter

# Dataset of how many times someone waters their lawns per week in the summer, and how many times they water in the winter. The two possible classifications are if their lawns are green or not.
# 1 being a yellow lawn, 2 being a green lawn.
X = np.array([[4, 2],[4, 1], [5, 3], [1, 1], [2, 2], [1, 0], [2, 0]])
Y = np.array([2, 2, 2, 1, 1, 1, 1])

# Get sets of data for summer and winter days
First_Spots = X[:,0]
Second_Spots = X[:,1]

# Count frequencies
First_Spots_Frequency = Counter(First_Spots)
Second_Spots_Frequency = Counter(Second_Spots)

# likelihood table
# use laplacian with alpha = 1 and if there are 0s make it 1
if not(0 in First_Spots):
    First_Spots_Frequency[0] = 1
if not(1 in First_Spots):
    First_Spots_Frequency[1] = 1
if not(2 in First_Spots):
    First_Spots_Frequency[2] = 1
if not(3 in First_Spots):
    First_Spots_Frequency[3] = 1
if not(4 in First_Spots):
    First_Spots_Frequency[4] = 1
if not(5 in First_Spots):
    First_Spots_Frequency[5] = 1
if not(6 in First_Spots):
    First_Spots_Frequency[6] = 1
if not(7 in First_Spots):
    First_Spots_Frequency[7] = 1

if not(0 in Second_Spots):
    Second_Spots_Frequency[0] = 1
if not(1 in Second_Spots):
    Second_Spots_Frequency[1] = 1
if not(2 in Second_Spots):
    Second_Spots_Frequency[2] = 1
if not(3 in Second_Spots):
    Second_Spots_Frequency[3] = 1
if not(4 in Second_Spots):
    Second_Spots_Frequency[4] = 1
if not(5 in Second_Spots):
    Second_Spots_Frequency[5] = 1
if not(6 in Second_Spots):
    Second_Spots_Frequency[6] = 1
if not(7 in Second_Spots):
    Second_Spots_Frequency[7] = 1

# Calculate likelihood 
iteration = 0
First_Spot_Likelihood = {}
Second_Spot_Likelihood = {}
while iteration <= 7:
    First_Spot_Likelihood[iteration] = First_Spots_Frequency[iteration]/sum(First_Spots_Frequency.values())
    Second_Spot_Likelihood[iteration] = Second_Spots_Frequency[iteration]/sum(Second_Spots_Frequency.values())
    iteration += 1

# Print tables based on dictionaries made so far.
print('\n')
print(tabulate(First_Spots_Frequency.items(), headers=['How Many Days Do People Water a Week in The Summer', 'Frequency']))
print(tabulate(Second_Spots_Frequency.items(), headers=['How Many Days Do People Water a Week in The Winter', 'Frequency']))
print(tabulate(First_Spot_Likelihood.items(), headers=['How Many Days Do People Water a Week in The Summer', 'Likelihood']))
print(tabulate(Second_Spot_Likelihood.items(), headers=['How Many Days Do People Water a Week in The Winter', 'Likelihood']))

# Create a fit using Gaussian Naive Bayes
print('\n')
clf = GaussianNB()
clf.fit(X, Y)
print("Based on this data, I predict that a person that waters their lawn twice a week in the summer and once in the winter will have(1 means yellow lawn, 2 means green lawn.):",clf.predict([[2, 1]]))
print("Based on this data, I predict that a person that waters their lawn four times a week in summer and four times a week in winter will have(1 means yellow lawn, 2 means green lawn.):",clf.predict([[4, 4]]))
print('\n')

# Enter a loop where the user can input a test case and it will predict an outcome as well as list probabilities.
while(1):
    summer_water = input("Please input a number (e.g. 4) of times to water your lawn in the summer. Or exit to end the script\n")
    if summer_water == 'exit' or summer_water == 'Exit':
        break
    winter_water = input("Please input a number (e.g. 4) of times to water your lawn in the winter. Or exit to end the script\n")
    if winter_water == 'exit' or winter_water == 'Exit':
        break
    summer_water_number = int(summer_water)
    winter_water_number = int(winter_water)
    number_prediction = clf.predict([[summer_water_number,winter_water_number]])
    if number_prediction[0] == 1:
        prediction = 'yellow'
    else:
        prediction = 'green'

    print("Based on {0} days a week in the summer and {1} days a week in the winter, I predict your lawn will be {2}".format(summer_water, winter_water, prediction))
    print("The probabilities for yellow and green lawn respectively for this sample are {0}\n".format(clf.predict_proba([[summer_water_number,winter_water_number]])))