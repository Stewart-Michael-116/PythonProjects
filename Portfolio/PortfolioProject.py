class ItemToPurchase:
    
    def __init__(self):
        item_name = 'none'
        item_price = 0.0
        item_quantity = 0
        total_price = 0.0

    def print_item_cost(self):
        self.total_price = self.item_quantity * self.item_price
        print("\n{} {} @ ${} = ${}\n".format(self.item_name, self.item_quantity, self.item_price, self.total_price))

class ShoppingCart:

    def __init__(self, customer_name, current_date):
        customer_name = None
        current_date = "January 1, 2020"
        cart_items = []
        

    def add_item(self, item:ItemToPurchase):
        pass

    def remove_item(self, item: str):
        pass

    def modify_item(self, item: ItemToPurchase):
        pass

    def get_num_items_in_cart(self):
        pass

    def get_cost_of_cart(self):
        pass

    def print_total(self):
        pass

    def print_descriptions(self):
        pass



# Main Code

# Definitions

item1 = ItemToPurchase()

item2 = ItemToPurchase()

def print_menu(cart: ShoppingCart):
    pass




# Prompt User for two items

item1.item_name = input("\nPlease enter the first item's name:\n")
item1.item_price = float(input("\nPlease enter the first item's price:\n"))
item1.item_quantity = int(input("\nPlease enter the first item's quantity:\n"))

item2.item_name = input("\nPlease enter the second item's name:\n")
item2.item_price = float(input("\nPlease enter the second item's price:\n"))
item2.item_quantity = int(input("\nPlease enter the second item's quantity:\n"))

# Results

item1.print_item_cost()
item2.print_item_cost()

print('Total: ${}'.format((item1.total_price+item2.total_price)))