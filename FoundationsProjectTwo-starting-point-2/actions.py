# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = ""  "www.TheShopCo.com"

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    for store in stores:
        print("-%s" % store.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for store in stores:
        if store_name == store.name:
            return store

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()
    user_input = input("please pick a store ny typing its name")
    store_titel = get_store(user_input)
    while not store_titel:
        user_input = input("invalid store name. please try again")
        store_titel = get_store(user_input)

    store_titel

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    picked_store.print_products()
    prine("pick the item you'd like to add in your cart (with a right spelling)")
    prim("type\"back\" to go back to main venu")
    user_input = ""

    while user_input.lower() != "back":
        for product in picked_store.products:
            if user_input.lower() == product.name.lower():
                cart.add_to_cart(product)

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    print_stores()

    user_input ""
    while user_input.lower() != "checkout":
        store_titel = picked_store
        if store_titel

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
