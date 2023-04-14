import inventory_project

def test_add_item_to_inventory():
    # Create an empty inventory
    inventory = inventory_project.Inventory()
    
    # Test adding an item to the inventory
    inventory.add_item('apple', 5)
    assert inventory.get_item_count('apple') == 5
    
    # Test adding more items to the inventory
    inventory.add_item('apple', 10)
    assert inventory.get_item_count('apple') == 15

def test_remove_item_from_inventory():
    # Create an inventory with some items
    inventory = inventory_project.Inventory()
    inventory.add_item('apple', 10)
    inventory.add_item('banana', 20)
    
    # Test removing an item from the inventory
    inventory.remove_item('apple', 5)
    assert inventory.get_item_count('apple') == 5
    
    # Test removing all items of a certain type from the inventory
    inventory.remove_item('banana', 20)
    assert inventory.get_item_count('banana') == 0

def test_get_inventory_value():
    # Create an inventory with some items
    inventory = inventory_project.Inventory()
    inventory.add_item('apple', 10)
    inventory.add_item('banana', 20)
    
    # Test getting the value of the inventory
    assert inventory.get_inventory_value() == 35.0
