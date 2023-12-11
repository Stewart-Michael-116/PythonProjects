# Random Number generator create a list of 500 ints
import random
import time
import sys

sys.setrecursionlimit(100000)

# Selection Sort
#-------------------------------------------------------------------------------------------------------------------------------------
# Python program for implementation of Selection
def selectionSort(array):
    size = len(array)
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])


# Insertion Sort
#-------------------------------------------------------------------------------------------------------------------------------------
def insertionSort(data):
    # return if array is size 1 or 0
    size = len(data)
    if size <= 1:
        return 
 
    for i in range(1, size):  
        key = data[i]  
        j = i-1
        while j >= 0 and key < data[j]:  
            data[j+1] = data[j]  
            j -= 1
        data[j+1] = key  

# Quick Sort
#-------------------------------------------------------------------------------------------------------------------------------------
# Quick sort function from discussion post
# Function to find the partition position
def partition(data, low, high):
    size = len(data)
    if size <= 1:
        return 
    
    pivot = data[high]
 
    i = low - 1
 

    for j in range(low, high):
        if data[j] <= pivot:
            i = i + 1
            (data[i], data[j]) = (data[j], data[i])
    (data[i + 1], data[high]) = (data[high], data[i + 1])

    return i + 1

def quickSort(data, low, high):
    if low < high:

        pi = partition(data, low, high)

        quickSort(data, low, pi - 1)

        quickSort(data, pi + 1, high)

# Testing and printing results
#-------------------------------------------------------------------------------------------------------------------------------------
data1 = [random.randint(0,9) for i in range(10000)]
data2 = data1.copy()
data3 = data1.copy()
data1 = data2.copy()
data1AverageTime = []
data2AverageTime = []
data3AverageTime = []

for i in range(10):
    start = time.time()
    selectionSort(data1)
    end = time.time()
    data1AverageTime.append(end-start)

print("Selection Sort: ",sum(data1AverageTime)/len(data1AverageTime))

for i in range(10):
    start = time.time()
    insertionSort(data2)
    end = time.time()
    data2AverageTime.append(end-start)

print("Insertion Sort: ",sum(data2AverageTime)/len(data2AverageTime))

for i in range(1):
    start = time.time()
    quickSort(data3, 0, len(data3)-1)
    end = time.time()
    data3AverageTime.append(end-start)

print("Quick Sort: ",sum(data3AverageTime)/len(data3AverageTime))
