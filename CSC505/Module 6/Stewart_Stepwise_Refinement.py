# Representation of Stepwise refinement
# I'll Use a tree data structure to explore this representation

class Stepwise_Tree:
    def __init__(self, step):
        self.step = step
        self.smaller_steps = []


mechanismTrigger = Stepwise_Tree("Mechanism for Other Programs to Trigger Task.")

mechanismReceive = Stepwise_Tree("Mechanism for Algorithm to Receive current tasks.")

mechanismRoot = Stepwise_Tree("Other Parts of OS triggers a task.")
mechanismRoot.smaller_steps = [mechanismTrigger,mechanismReceive]

storageStructure = Stepwise_Tree("Variable/Structure for task triggering storage.")

receivesTasks = Stepwise_Tree("Receives Tasks")
receivesTasks.smaller_steps = [mechanismRoot, storageStructure]

accessStorage = Stepwise_Tree("Access Storage and Assess Task Priority")
completeTask = Stepwise_Tree("Complete Tasks")
removeTrigger = Stepwise_Tree("Remove Trigger from Storage")

completeTaskParent = Stepwise_Tree("Complete Task")
completeTaskParent.smaller_steps = [accessStorage, completeTask, removeTrigger]

algorithm = Stepwise_Tree("Task Scheduling Algorithm")
algorithm.smaller_steps = [completeTaskParent, receivesTasks]

current = algorithm
while(1):
    children_count = str(len(current.smaller_steps))
    print("\nYou are currently at %s, with %s children\n" % (current.step,children_count))
    userInput = input("\nWhat would you like to do? You can travel to children 1 2 or 3 by typing 1 2 or 3, or go back to top by typing top. You can also exit by typing exit.\n")

    if userInput == "1":
        temp = current.smaller_steps[0]
        current = temp
    elif userInput == "2":
        temp = current.smaller_steps[1]
        current = temp
    elif userInput == "3":
        temp = current.smaller_steps[2]
        current = temp
    elif userInput == "top":
        current = algorithm
    elif userInput == "exit":
        break
    else:
        print("invalid input, try again")