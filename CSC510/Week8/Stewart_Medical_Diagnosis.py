# Take in medical data.
# Use Naive bayes to classify.
# Use symbolic logic to add information about if they should call 911.
# Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.

# Using pandas read_csv method to read this csv I have downloaded from Kaggle.
# Data set here: https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset
# Importing files from my bayes analysis

import pandas as pd
from sklearn.naive_bayes import GaussianNB
import numpy as np
import sys



def disease_symptom_frequency(dataset):
    data_file_pandas = pd.read_csv(dataset)
    disease_symptom_freq = {}


    for i, row in data_file_pandas.iterrows():
        disease = row.iloc[0]  
        symptoms = row.iloc[1:] 
        if disease not in disease_symptom_freq:
            disease_symptom_freq[disease] = {}
        for symptom in symptoms:
            # Added handling for nan since some of the squares were giving this string.
            if isinstance(symptom, str) and symptom != 'nan':
                if symptom.lstrip() not in disease_symptom_freq[disease]:
                    disease_symptom_freq[disease][symptom.lstrip()] = 1
                else:
                    disease_symptom_freq[disease][symptom.lstrip()] += 1
    return disease_symptom_freq


dataset = 'dataset.csv'
Frequency_Sets = disease_symptom_frequency(dataset)

# Print dataset import here.
for disease, symptoms in Frequency_Sets.items():
    print(disease)
    print("----------------")
    for symptom, frequency in symptoms.items():
        print("{0} occured {1} times".format(symptom, frequency))
    print("\n")
    

print('\nHere is the datasets for Common Cold and Allergy:')
print(Frequency_Sets['Common Cold'])
print(Frequency_Sets['Allergy'])
print("\nThese are all the diseases and symptoms in the dataset we are working with.")
print("Based on this data, I will give you a likelihood that you have the common cold or it's just allergies.")

# Do Naive Bayes, 120 common cold, 120 allergy
Cold_Dictionary = dict(Frequency_Sets['Common Cold'])
Allergy_Dictionary = dict(Frequency_Sets['Allergy'])

# Create lists for frequency:
Sets_For_List = set(Cold_Dictionary.keys()) | set(Allergy_Dictionary.keys())
cold_data_list = []
allergy_data_list = []

for symptom in Sets_For_List:
    cold_data_list.append(Cold_Dictionary.get(symptom, 1))
    allergy_data_list.append(Allergy_Dictionary.get(symptom, 1))
print('\nThese are the frequencies converted to lists for our Naive Bayes ')
print(cold_data_list)
print(allergy_data_list)

print('\nThis is the data converted to a numpy array for input. Next is the designation for cold and allergy arrays as the second input. 1 is cold, 2 is allergy.')
samples_array = np.array([cold_data_list,allergy_data_list])
print(samples_array)
class_array = np.array(['Common Cold', 'Allergy'])
print(class_array)

gaussianFit = GaussianNB()
gaussianFit.fit(samples_array, class_array)

gaussianFit_pf = GaussianNB()
gaussianFit_pf.partial_fit(samples_array, class_array, np.unique(class_array))

#print(clf.predict([[-0.8, -1]]))
#print(clf_pf.predict([[-0.8, -1]]))
def count_symptoms(input_string):
    # Get the unique symptoms from both cold and allergy
    input_freq_list = [0] * len(Sets_For_List)

    # enumerate to make it accessible
    for i, symptom in enumerate(Sets_For_List):
        count = input_string.lower().count(symptom)
        input_freq_list[i] = count

    return input_freq_list

user_input = input("\nPlease input a sentence describing all of your symptoms.\n")

# Check if substring is in list.
def is_substring_in_list(input_string, string_list):
    for substr in string_list:
        if substr in input_string:
            return True
    return False

# We will use symbolic logic to advise if the user should call 911.
Nine_One_One_Worthy_Symptoms = ["can't breathe", "Can't Breathe", "Can't breathe", "left side is numb", "Left side is numb", "cannot breathe"]
if is_substring_in_list(user_input, Nine_One_One_Worthy_Symptoms):
    print("\nIF YOU ARE EXPERIENCING ANY ABNORMAL NUMBNESS IN YOUR LEFT SIDE OR CANNOT BREATHE, YOU SHOULD STOP NOW AND CALL 911.\n")
    sys.exit()


prediction = count_symptoms(user_input)

#Modify prediction to fit curve better
weighted_prediction = [x * 100 for x in prediction]
modified_prediction = [x if x != 0 else 1 for x in weighted_prediction]

print("\n Here is the frequency array for your input and it's modified input into our model")
print(prediction)
print(modified_prediction)
print("\n")




print("\nOur fit and partial fit predictions are listed below based on your input:")
print(gaussianFit.predict([modified_prediction]))
print(gaussianFit_pf.predict([modified_prediction]))

