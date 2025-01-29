# There is a tutorial in our book for making this KNN using SKLearn, but I will try and make it manually like the assignment suggests.
# This script was made using these sources:
#  
# https://stackoverflow.com/questions/11023411/how-to-import-csv-data-file-into-scikit-learn
# https://github.com/mfenner1/mlwpy_code/blob/master/03_GettingStartedWithClassification_code.ipynb
# Machine Learning With Python For Everyone

#from mlwpy import *
import pandas as pd
import numpy as np

# Load the data
# iris_measurements = np.genfromtxt('iris.csv', delimiter=',', skip_header=1, usecols=(0,1,2,3))
new_sepal_length = input("\nPlease type the new sample's sepal length. Typical measurements range from 4-8\n")
new_sepal_width = input("\nPlease type the new sample's sepal width. Typical measurements range from 2-4\n")
new_petal_length = input("\nPlease type the new sample's petal length. Typical measurements range from 1-6\n")
new_petal_width = input("\nPlease type the new sample's petal width. Typical measurements range from 0-2\n")

new_measurement_string = np.array([new_sepal_length, new_sepal_width, new_petal_length, new_petal_width])
new_measurement_float = new_measurement_string.astype(float)
iris_df = pd.read_csv("iris.csv")

# Initialize value of K
K = int(input("\nPlease set a K value for how many nearest neighbors should be included. 1-20 is normal\n"))

# calculate distances to all test points

measurements_df = iris_df[['SepalLength','SepalWidth','PetalLength','PetalWidth']].values
#print(measurements_df, new_measurement_float)
distances = np.linalg.norm(measurements_df - new_measurement_float, axis = 1)
iris_df['distances'] = distances

# Sort calculated distances by ascending order
iris_df_sorted = iris_df.sort_values(by='distances')

# Get top K rows of sorted array
top_k_rows = iris_df_sorted.head(K)

# Get most frequent class of these rows.
iris_counts = top_k_rows['Name'].value_counts()

count_setosa = iris_counts.get("Iris-setosa",0)
count_versicolor = iris_counts.get("Iris-versicolor",0)
count_virginica = iris_counts.get("Iris-virginica",0)

sum_all_types = count_setosa + count_versicolor + count_virginica
count_values = [count_setosa, count_versicolor, count_virginica]
names  = ["Setosa", "Versicolor", "Virginica"]

max_index = count_values.index(max(count_values))


# Return predicted class with confidence percentage
print(f"\n\nThe most likely Iris type is {names[max_index]}, with a confidence of {max(count_values)/float(sum_all_types)*100}%.")
print(f"\nHere is the top k={K} rows of distance:\n")
print(top_k_rows)
