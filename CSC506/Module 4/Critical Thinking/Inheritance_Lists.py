# Create Ordered and Unordered Lists using Inheritance

# Create List to be used for inheritance
class PlainList():
    # List
    def __init__(self):
        self.list = []

    def printList(self):
        print(self.list)





# Create Ordered List using parent
class OrderedList(PlainList):

    def __init__(self):
        super().__init__()
    
    def Add(self, data):

        #search for when new data is more than items in list
        index = 0
        while index < len(self.list) and self.list[index] < data:
            index = index + 1
        #insert once done
        self.list.insert(index, data)

    def Remove(self, data):
        self.list.remove(data)

    def CheckIfItemIsInList(self, data):
        if data in self.list:
            return True
        else:
            return False

# Create Unordered list using parent
class UnorderedList(PlainList):
    def __init__(self):
        super().__init__()

    def Add(self, data):

        self.list.append(data)

    def Remove(self, data):
        self.list.remove(data)

    def CheckIfItemIsInList(self, data):
        if data in self.list:
            return True
        else:
            return False

# Implement a test of some kind maybe

OrderList = OrderedList()
UnorderList = UnorderedList()
OrderList.Add(3)
OrderList.Add(1)
OrderList.Add(2)
OrderList.Add(8)

UnorderList.Add(1)
UnorderList.Add(3)
UnorderList.Add(2)
UnorderList.Add(4)
print("Ordered List:")
OrderList.printList()
print("\nUnordered List:")
UnorderList.printList()
