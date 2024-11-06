#Drive Thru Menu
"""Create a drive_thru.py program with your favorite fast food chain's menu.

Define a get_item() function that takes in one parameter, the number of the item you want to order, and returns the name of that item!

For example, if you called the function with:

    Argument value 1, it could return '🍔 Cheeseburger'.
    Argument value 2, it could return '🍟 Fries'.
    Argument value 3, it could return '🥤 Soda'.
    Argument value 4, it could return '🍦 Ice Cream'.
    Argument value 5, it could return '🍪 Cookie'.

Make sure to call this function a few times to make sure that it works!

Lastly, let's do the following:

    Create a welcome menu and put that in a welcome() function.
    Create a main program that takes in user input with input().
    Create a math function that adds the total cost up.
    """
menu_items  = {1: ('🍔 Cheeseburger', 6.99),
    2:('🍟 Fries', 2.50),
    3:('🥤 Soda', 1.99),
    4:('🍦 Ice Cream', 3.99),
    5:('🍪 Cookie', 1.50),
    6:('Combo 1: Cheeseburger, fries, soda', 9.25),
    }


def welcome():
    print("Welcome to Backshot Burgers and Fries")
    print("What do you want to eat? ")
    for numbr, (item, price) in menu_items.items():
        print(f"{numbr}.  {item} - ${price:.2f}")

def order_item(order_number):
    "Should out put item and price"
    return  menu_items.get(order_number, ("Item not found", 0))

def calculate_total(order):
    "Adds the total cost"
    total_cost = sum(price for item, price in order)
    return total_cost

def main():
    welcome()
    order = []

    while True:
        try:         
            order_number = int(input("Enter the number of the item you want to order, (or 0 to finish): "))
            if order_number == 0:
             break
            item,  price = order_item(order_number)
            if item:
                order.append((item, price))
                print(f"You added {item} to your order.")
            else:
                print("That item does not exist, please repeat your order.")
        except ValueError:
            print("Please input a valid menu option.")
    
    total_cost = calculate_total(order)
    print("\Your order summary: ")
    for item, price in order:
        print(f"{item} - ${price:.2f}")
    
    print(f"Total: ${total_cost:.2f}")
    print("Thank you for ordering from Backshot Burgers")

if __name__ == "__main__":
    main()

 