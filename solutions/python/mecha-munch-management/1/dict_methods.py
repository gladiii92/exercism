"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add: # Für Item in Tuple (items_to_add)
        if item not in current_cart: # Wenn "Orange" etc. nicht in bisherigem Dict
            current_cart[item] = 0 # Füge das item hinzu und setzte den Val auf 0
        current_cart[item] += 1 # Andernfalls, zähl das Item einfach hoch
    return current_cart # ganze geupdatetes Dict mit neuen Werten zurückgeben    

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    result = {}
    for item in notes:
        if item not in result:
            result[item] = 1
    return result

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    for recipe in recipe_updates:
        ideas.update(recipe_updates)
    return ideas

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return sorted(cart.items())

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    empty = {} # Leeres dict
    for item in cart.keys(): # für jedes Item in Warenkorb (Schlüssel - Orange, Banane, Milk etc.)
        empty[item] = [cart[item]] + aisle_mapping[item]
    return sorted(empty.items(), reverse = True)

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item, info in fulfillment_cart.items():
        current_stock = store_inventory[item][0]
        ordered_amount = info[0]
        
        if current_stock == 0:
            store_inventory[item][0] = 'Out of Stock'
        else:
            store_inventory[item][0] -= ordered_amount 
            if store_inventory[item][0] == 0:
                store_inventory[item][0] = 'Out of Stock'
    
    return store_inventory