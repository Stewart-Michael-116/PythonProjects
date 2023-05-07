class ItemToPurchase:
    item_name = ''
    item_price = 0.0
    item_quantity = 0
    total_price = 0.0
    item_description = ""

    def __init__(self):
        pass

    def print_item_cost(self):
        self.total_price = self.item_quantity * self.item_price
        print("\n{} {} @ ${} = ${}\n".format(self.item_name, self.item_quantity, self.item_price, self.total_price))

class ShoppingCart:

    customer_name = None
    current_date = "January 1, 2020"
    cart_items = []

    def __init__(self, customer_name, current_date):
        self.customer_name = customer_name
        self.current_date = current_date
        

    def add_item(self, item: ItemToPurchase):
        self.cart_items.append(item)

    def remove_item(self, item: str):
        for x in self.cart_items:
            if x.item_name == item:
                self.cart_items.remove(x)
                

    # Needs to be finished
    def modify_item(self, item: ItemToPurchase):

        for i in range(len(self.cart_items)):
            if(self.cart_items[i].item_name == item.item_name):
                #if(item.item_name != 'none'):
                #    x
                if(item.item_price != 0.0):
                    self.cart_items[i].item_price = item.item_price
                if(item.item_quantity != 0):
                    self.cart_items[i].item_quantity = item.item_quantity
                if(item.item_description != ""):
                    self.cart_items[i].item_description = item.item_description
                self.cart_items[i].total_price = self.cart_items[i].item_quantity * self.cart_items[i].item_price
                print('\nItem Modified\n')
                return
            
        print('Item not found in cart. Nothing modified.')


    def get_num_items_in_cart(self):
        return len(self.cart_items)

    def get_cost_of_cart(self):
        total = 0

        for x in self.cart_items:
            total += x.total_price

        return total
            

    def print_total(self):
        
        print("\n{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Number of Items: {}".format(self.get_num_items_in_cart()))

        for x in self.cart_items:
            print("{} {} @ ${} = ${}".format(x.item_name, x.item_quantity, x.item_price, x.total_price))

        print("Total: ${}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print("\n{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Item Descriptions")

        for x in self.cart_items:
            print("{}: {}".format(x.item_name, x.item_description))

    def print_menu(self):
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")



# Main Code
#Milestone 3 Code
#-----------------------------------------------------------------------------------------------------------------------------------------------
#import
from datetime import date


# Definitions and ask for names
name = input("\nPlease Enter Customer Name:\n")
date_string = input("\nPlease Enter Today's Date:\n")
print("Customer name: {}\nToday's date: {}\n".format(name, date_string))
shopping_cart = ShoppingCart(name, date_string)


# Menu conditions and operations. while loop until user 
while(1):

    shopping_cart.print_menu()
    customer_request = input("Please Enter a Menu Option:\n")

    if(customer_request == 'a'):

        new_item = ItemToPurchase()
        new_item.item_name = input("Please put the item's name:\n")
        new_item.item_price = float(input("Please put the item's price:\n"))
        new_item.item_quantity = int(input("Please put the item's quantity:\n"))
        new_item.item_description = input("Please put the item's description:\n")
        new_item.total_price = new_item.item_price * new_item.item_quantity

        shopping_cart.add_item(new_item)

        print("Thank you, item added\n")

    elif(customer_request == 'r'):

        item_removing = input("Please enter the name of the item to be removed:\n")
        shopping_cart.remove_item(item_removing)

    elif(customer_request == 'c'):

        new_item = ItemToPurchase()
        new_item.item_name = input("Please put the item's name you'd like to modify:\n")
        new_item.item_price = float(input("Please put the item's price new price (press enter if no new price):\n"))

        quantity = input("Please put the item's new quantity (press enter if no new quantity):\n")

        if quantity == "":
            new_item.item_quantity = 0
        else:
            new_item.item_quantity = int(quantity)
        
        new_item.item_description = input("Please put the item's new description (press enter if no new description):\n")

        shopping_cart.modify_item(new_item)
        
    elif(customer_request == 'i'):
        
        shopping_cart.print_descriptions()

    elif(customer_request == 'o'):

        shopping_cart.print_total()
    
    elif(customer_request == 'q'):

        break

    else:

        print("Error: Incorrect Input")
        
        continue
        

print("\nSee you later!\n")







# Milestone 1 Code
#-----------------------------------------------------------------------------------------------------------------------------------------------

# # Definitions

# item1 = ItemToPurchase()

# item2 = ItemToPurchase()

# def print_menu(cart: ShoppingCart):
#     pass




# # Prompt User for two items

# item1.item_name = input("\nPlease enter the first item's name:\n")
# item1.item_price = float(input("\nPlease enter the first item's price:\n"))
# item1.item_quantity = int(input("\nPlease enter the first item's quantity:\n"))

# item2.item_name = input("\nPlease enter the second item's name:\n")
# item2.item_price = float(input("\nPlease enter the second item's price:\n"))
# item2.item_quantity = int(input("\nPlease enter the second item's quantity:\n"))

# # Results

# item1.print_item_cost()
# item2.print_item_cost()

# print('Total: ${}'.format((item1.total_price+item2.total_price)))