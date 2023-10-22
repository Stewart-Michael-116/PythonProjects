# Stewart Module 5

while 1:

    user_input = input("\nWould you like to hear about the Pothole Reporting System's Actors, Use Cases, or a general description?\n")

    if user_input.lower() == "actors":
        #Add
        print("\nThe actors in this system are the citizens, repair team, database, and anyone involved in maintenance or infrastructure for reporting.")

    elif user_input.lower() == "use cases":
        #Add
        print ("\nThe use  cases in this system involve the user reporting a pothole and then receiving a report once it's fixed, the repair team getting work orders and adding details to their reporting, and other citizens requesting data about potholes.")

    elif user_input.lower() == "general description":
        #Add
        print("\nThe PHTRS system is where users across the city are able to report information and have repair teams go and fix them. This system will store information for all users involved in order to record and fix potholes quickly in order to avoid losing money from damages.")

    elif user_input.lower() == "exit": 
        break

    else:
        print("\nInvalid Input, please type actors, use cases, general descriptions, or exit.")