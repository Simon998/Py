
import csv

# Define a class for an inventory item with name, quantity, and price attributes
class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

# Define a class 
class InventoryManagement:
    def __init__(self):
        # Initialize an empty list to hold  items
        self.inventory = []

    # add a new item to the inventory
    def add_item(self, item):
        self.inventory.append(item)

    #  remove an item from the inventory by name
    def remove_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)

    #  update an item's quantity or price by name
    def update_item(self, item_name, quantity=None, price=None):
        for item in self.inventory:
            if item.name == item_name:
                if quantity is not None:
                    item.quantity = quantity
                if price is not None:
                    item.price = price

    # o display the current inventory
    def display_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"{item.name}: {item.quantity} - ${item.price}")

    #  load inventory data from a CSV file
    def load_inventory(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Parse the CSV row data and create a new InventoryItem object
                name, quantity, price = row
                item = InventoryItem(name, int(quantity), float(price))
                # Add the new item to the inventory
                self.add_item(item)

    # save the current inventory to a CSV file
    def save_inventory(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for item in self.inventory:
                # Write each inventory item to a new row in the CSV file
                writer.writerow([item.name, item.quantity, item.price])


def main():
    # Create a new instance of the InventoryManagement class
    inventory_manager = InventoryManagement()

    # Load inventory data from a CSV file
    inventory_manager.load_inventory('inventory.csv')

    # Display the main menu 
    while True:
        print("\n1. Add item")
        print("2. Remove item")
        print("3. Update item")
        print("4. Display inventory")
        print("5. Save inventory")
        print("6. Exit")
        choice = input("Enter your choice: ")

       
        if choice == '1':
            
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            item = InventoryItem(name, quantity, price)
            # Add the new item to the inventory
            inventory_manager.add_item(item)
            print("Item added to inventory.")

        elif choice == '2':
            name = input("Enter item name to remove: ")
            inventory_manager.remove_item(name)
            print("Item removed from inventory.")

        elif choice == '3':
            name = input("Enter item name to update: ")
            quantity = input("Enter new quantity (leave blank to skip): ")
            price = input("Enter new price (leave blank to skip): ")
            inventory_manager.update_item(name, int(quantity) if quantity else None, float(price) if price else None)
            print("Item updated.")

        elif choice == '4':
            inventory_manager.display_inventory()

        elif choice == '5':
            inventory_manager.save_inventory('inventory.csv')
            print("Inventory saved to file.")

        elif choice == '6':
            break

if __name__ == '__main__':
    main()

