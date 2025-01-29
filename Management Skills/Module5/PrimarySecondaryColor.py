# Mixing primary colors script

# Variable definition

user_colors = []
accepted_colors = ["Blue", "blue", "red", "Red", "Yellow", "yellow"]
i = 0

# Take input and if it's anything besides a color, error message

while i < 2:

    # Get Color Inputt
    user_colors.insert(i,(input("\nPlease input a primary color:\n")))

    # Check if it is a color
    if user_colors[i] in accepted_colors:
        print("\nColor Registered!\n")
    else:
        print("\nNot a primary color! Please input a primary color.")
        continue
    i += 1


# Else perform Logic

# If red
if user_colors[0] == "red" or user_colors[0] == "Red":

    # if blue then purple
    if user_colors[1] == "blue" or user_colors[1] == "Blue":
        print("\nThe Resulting Color is Purple!")

    # if yellow then ornage
    elif user_colors[1] == "red" or user_colors[1] == "Red":
        print("\nThe Resulting Color is Red!")

    # else must be yellow
    else:
        print("\nThe Resulting Color is Orange!")
elif user_colors[0] == "Blue" or user_colors[0] == "blue":

    # if blue then blue
    if user_colors[1] == "Blue" or user_colors[1] == "blue":
        print("\nThe Resulting Color is Blue!")

    # if red then purple
    elif user_colors[1] == "red" or user_colors[1] == "Red":
        print("\nThe Resulting Color is Purple!")

    # else must be yellow
    else:
        print("\nThe Resulting Color is Green!")

    # If yellow
else:
    # yellow and blue is green
    if user_colors[1] == "Blue" or user_colors[1] == "blue":
        print("\nThe Resulting Color is Green!")

    # if yellow and red is orange
    elif user_colors[1] == "red" or user_colors[1] == "Red":
        print("\nThe Resulting Color is Orange!")

    # else must be two yellow
    else:
        print("\nThe Resulting Color is Yellow!")

print()
