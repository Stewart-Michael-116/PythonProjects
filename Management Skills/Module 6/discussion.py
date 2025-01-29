# Students attending Class today
Grocery_List = {}

while(1):

    new_item = input("Please Enter Name of New Item")

    if(new_item == 'end'):
        break

    quantity = int(input("Please enter how many of this item you will buy"))

    Grocery_List[new_item] = quantity

print(Grocery_List)