# DESCRIPTION: First attempt, tried thinking through it with recursion, this might work, but might I thought of trying loops.

# def stringEditDistanceCustomCost(stringA, stringASize, stringB, stringBSize, insertCost, copyCost, deleteCost):
#     # Cover Base Cases
#     if(stringA == ''):
#         return(len(stringB)*insertCost)
    
#     if(stringB == ''):
#         return(len(stringA)*deleteCost)


    # Get String 1, the one we need to turn into to string 2

    # Get String 2, the thing we need to get String 1 to be

    # Assign Costs

    # Start Loop to Start Replacing

# String One to be changed from User

# String Two "The Model" from User

# Assign Costs to each Action

# Call Our Function

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------







# Get string A from user
stringA = input("Please enter the first word:\n")

# Get string B from user
stringB = input("Please enter the second string:\n")

# Lengths
lengthA = int(len(stringA))
lengthB = int(len(stringB))

# Create Table of size for each word
wordArray = [[0 for i in range(lengthA+1)] for j in range(lengthB+1)]

# Fill in first row
for i in range(lengthA+1):
    wordArray[0][i] = i*20 

# Fill in first column
for i in range(lengthB+1):
    wordArray[i][0] = i*20 


# For each square, find the minimum between the previous interactions, and add 5 for replace.
for i in range(1, lengthB+1):

    for j in range(1, lengthA+1):

        if stringA[j-1] == stringB[i-1]:
            if i == j:
                wordArray[i][j] = wordArray[i-1][j-1]
            else:
                wordArray[i][j] = min(wordArray[i][j-1], wordArray[i-1][j], wordArray[i-1][j-1]) + 20 
        else:
            if i == j:
 
                wordArray[i][j] = min(wordArray[i][j-1], wordArray[i-1][j], wordArray[i-1][j-1]) + 5 
            else:

                wordArray[i][j] = min(wordArray[i][j-1], wordArray[i-1][j], wordArray[i-1][j-1]) + 20 





# Return the number at the end of the grid as that is the cheapest interaction.

print(wordArray[int(len(wordArray))-1][int(len(wordArray[0]))-1])

