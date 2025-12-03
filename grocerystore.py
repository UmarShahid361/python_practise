# Grocery Store Management System
inventory = {
    "Apples": 5,
    "Banana": 2
}
cart = []
discount_codes = {"SAVE10"}

user_choice = 0


def displayInventory():
    print(inventory)


def addItemsToCart():
    displayInventory()
    user_input = input("Enter what you want: ")
    if (user_input in inventory):
        print("Item added to cart.")
        cart.append(user_input)
        print(cart)
    else:
        print("Invalid Input")


def checkout():
    total = 0
    for item in cart:
        print(cart)
        total += inventory[item]
    print(f"Your bill is {total}")


while user_choice != 4:
    print("1.View Inventory")
    print("2.Add to Cart")
    print("3.Checkout")
    print("4.Exit")

    try:
        user_choice = int(input("Enter your desired number: "))
    except:
        print("Enter Integars Only!")

    match user_choice:
        case 1:
            displayInventory()
        case 2:
            addItemsToCart()
        case 3:
            checkout()
        case 4:
            break
        case _:
            print("Invalid Input! Please enter correct details.")
