# Problem 7 - Shopping Cart Management (Lists, Tuples & Dictionaries)
# Inventory is a list of (item, price) tuples, the cart is a dictionary of item -> quantity,
# and calculate_total() works out the bill.

store_items = [("Apple", 2.5), ("Banana", 1.2), ("Milk", 3.0)]
cart = {}  # format: {'Apple': 3, 'Milk': 1}


def add_to_cart(cart, item, quantity):
    cart[item] = cart.get(item, 0) + quantity


def calculate_total(cart, store_items):
    # turn the list of tuples into a price lookup: {'Apple': 2.5, ...}
    prices = {}
    for name, price in store_items:
        prices[name] = price

    total = 0
    for item, quantity in cart.items():
        if item in prices:
            line = prices[item] * quantity
            print(f"  {item:<7} {quantity} x ${prices[item]:.2f} = ${line:.2f}")
            total = total + line
        else:
            print(f"  {item} is not sold in this store, skipped")
    return total


add_to_cart(cart, "Apple", 3)
add_to_cart(cart, "Milk", 1)
add_to_cart(cart, "Banana", 2)
add_to_cart(cart, "Apple", 1)   # adds to the existing quantity
add_to_cart(cart, "Bread", 1)   # not in the inventory

print("Cart:", cart)
total = calculate_total(cart, store_items)
print(f"Total bill: ${total:.2f}")
