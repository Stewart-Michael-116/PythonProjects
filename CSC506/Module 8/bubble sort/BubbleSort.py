# Bubble Sort

# Define
def modifiedBubbleSort(data):
    
    length = len(data)

    # Big for loop
    for i in range(length):
        # Check if we are on odd or even pass
        if i % 2 == 0:
            # subtract one since we are comparing element and the one after it
            for j in range(int(i/2), length - 1, 1):
                if data[j] > data[j+1]:
                    data [j], data[j+1] = data[j+1], data[j]

        # Check if we are on odd or even pass
        if i % 2 == 1:
            for j in range(length - i - 1, int((i-1)/2), -1):
                if data[j] < data[j-1]:
                    data[j], data[j-1] = data[j-1], data[j]

    # Done
    return data

array = [3,1,34,4,5,2,32,2,4,4]
print(modifiedBubbleSort(array))