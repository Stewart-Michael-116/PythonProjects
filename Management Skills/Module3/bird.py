bird_dictionary = {}

#Continuous input until you're done birdwatching
while 1:

    # Ask for input from the user about type and number of birds
    bird_type = input("\nType the species of birds you saw\n")

    # Break if done birdwatching
    if bird_type == 'stop':
        break

    bird_number = int(input("\nHow many of them did you see?\n"))

    # Test if bird is already in dictionary
    if bird_type in bird_dictionary:
        bird_dictionary.update({bird_type: bird_number + bird_dictionary[bird_type]})
    else:
        bird_dictionary.update({bird_type: bird_number})

    print("bird registered!")c

print(bird_dictionary, '\n')


