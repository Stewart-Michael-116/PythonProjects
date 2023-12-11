from numpy import random
import time
import sys

def insertionSort(arr, start, end):
    n = end-start  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(start+1, end+1):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= start and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position

# Function to find the partition position
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSortEfficient(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        if (pi-low) < 100:
            insertionSort(array, low, pi)
        else:
            quickSortEfficient(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        if (high-(pi+1)) < 100:
            insertionSort(array, pi+1, high)
        else:
            quickSortEfficient(array, pi + 1, high)

def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot

        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot

        quickSort(array, pi + 1, high)


 
sys.setrecursionlimit(10000)

timesArray = []
timesArrayEfficient = []


for i in range(10): 
    data = [random.randint(0,9) for i in range(10000)]
    size = len(data)
    start = time.time()
    quickSortEfficient(data, 0, size - 1)
    end = time.time()
    timesArrayEfficient.append(end-start)

results2 = sum(timesArrayEfficient)/len(timesArrayEfficient)
print(results2)

for i in range(10): 
    data = [random.randint(0,9) for i in range(10000)]
    size = len(data)
    start = time.time()
    quickSort(data, 0, size - 1)
    end = time.time()
    timesArray.append(end-start)
 
results1 = sum(timesArray)/len(timesArray)

print(results1)


percentageReduction = (results1-results2)/results1*100

print(percentageReduction)