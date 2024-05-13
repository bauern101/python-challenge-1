# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list or Dict. --> item name, item price, and quantity
# [] --> List
# {} --> Dict
# [{},{}] --> List of 2 Dict
# print(menu["Meals"]["Burrito"])
#
# order = [
# {
#     "Item name": "string",
#     "Price": float,
#     "Quantity": int
# },
# {
#     "Item name": "string",
#     "Price": float,
#     "Quantity": int
# }
# ]
order = []
# ---------------------------------------------------------------------------------- > An order list is initialized. (2 points)

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number DISPLAY
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        # Creates variable 'key'
        #   On each loop, 'key' will equal each item on the list
        # loops through only the '.key' side of Dict 'menue'
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        #    ---> Uses 'i' as index to store items in the dict
        #                                     ---->   i:Item
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            #
            # 'menu' dict section referenced by menu_category_name
            #   is unpacked as a tuple list of 2 items
            #   the pair gets stored into the comma variables, 
            #   the 1st into 'key', and the 2nd into 'value'
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    # Do it again, but only for Dict obj in the list
                    for key2, value2 in value.items():
                        # (- 3) is to compensate for the " - " used as a divder
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # The menu is now printed 
            #<----- Go back to here to have next action outside printing loop
            # Use line 102
            # 2. Ask customer to input menu item number
# -----------------------------> User is prompted for their menu item selection and it's saved as a variable menu_selection. (4 points)
            menu_selection = input(f"What selection would you like?\n")
            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
#-----------------------------------> User input menu_selection is checked as a number and an error is printed if it is not. (4 points)
#                                                                       (error, both for null and non-valid value @ end of If)
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)
# -------------------------------------------------------------------------->  menu_selection is converted to an integer. (2 points)
                # 4. Check if the menu selection is in the menu items 
                # Dict menue_items --> (key is menu #)  : 
                #                   (Value is sub-Dict {Item Name, Price})
                # Sub catagoires (like 'pizza') have already been looped out 
                if menu_selection in menu_items.keys():
# -------------------------------------> An if-else statement is used to check if menu_selection is in the menu_items keys, 
#                                                                                       and an error is printed if it isn't. (4 points)
#                                                                    (error, both for null and non-valid value @ end of If)
                    # Store the item name as a variable
                    order_name = menu_items[menu_selection]["Item name"]
# ---------> The item name of the customer's selection is extracted from the menu_items dictionary and stored as a variable. (4 points)
                   
                    # Ask the customer for the quantity of the menu item
                    order_qty = input(f"How many {order_name} would you like?\n")


                    # Check if the quantity is a number, default to 1 if not
                    if order_qty.isdigit() != True:
                        print("Invalid entry. Selection set to 1.")
                        order_qty = 1
                    order_qty = int(order_qty)
                    print(f"{order_qty} {order_name} has been added to your order.")
#---------------------------------------------------> The customer is prompted for a quantity of their item selection 
#                                           and the value defaults to 1 if the customer does not input a valid number. (10 points)

                    # Add the item name, price, and quantity to the order list
                    order_price = menu_items[menu_selection]["Price"]
                    order.append(
                        {
                            "Item name": order_name,
                            "Price": order_price,
                            "Quantity": order_qty
                        })
#-------------> The customer's selected item, price, and quantity are appended to the order list in dictionary format. (10 points)                 

   # Tell the customer that their input isn't valid
   #      Menue_number is NOT in menue_times keys
                else:
                    print("That is not a valid selection.")


                # Tell the customer they didn't select a menu option
                # menu_number is NOT a didgit
            else:
                if menu_selection =="":
                    print("A selection needs to be made.")
                else:
                    print(f"{menu_selection} is not a valid menu option.")

        else:
            # Tell the customer they didn't select a menu option
            # menu_catagory was not in menu_item.keys() 
            if menu_category == "":
                print("A selection needs to be made.")
            else:
                print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        # menu_catagory was NOT a didgit
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        #    --> Converting, any non-viable ansewr will restart loop
        match keep_ordering.lower():
# -----------------> The match-case statement converts the use input to lowercase or uppercase before checking the case. (4 points)
                # Keep ordering
            case "y":
                break
                # Exit the keep ordering question loop
            case  "n":
                # Complete the order
                place_order = False
                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you for ordering")
                # Exit the keep ordering question loop
                break
            case _ :
                # Tell the customer to try again
                print("Not a valid choice.  Please Try again")
# ------------------------------> A match-case statement is used to check if the customer would like to keep ordering,
#                                                        and performs the correct actions for y, n, and default cases. (10 points) 
               

# ****************************************************
# **************  Receipt  ***************************
# ****************************************************




# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
    #  < ------ 26-------------->
    #                           "| $"
    #                               <-6-->
    #                                    "| "
    #                                        {qty}
    # Pipe 1 starts at position 27
    #   Price "$" to be at 29 (for a space between pipe and sign)
    #    Name - spaces = 26
    #   2 spaces after money before 'pipe' 2
    #     Group them --> "f{receipt_spaces}| $"{price}  | {qty}
    # Pipe 1 starts at position 36
    # ------> NEED len check for price // some prices over $9

# 6. Loop through the items in the customer's order
for receipt_dict in order:
# ---------------------------------------------------------------> A for loop is used to loop through the order list. (10 points)

    # 7. Store the dictionary items as variables
    receipt_item_name = receipt_dict["Item name"]
    receipt_price = receipt_dict["Price"]
    receipt_quantity = receipt_dict["Quantity"]
 # -------------------------------------------> The value of each key in each order dictionary is saved as a variable. (6 points)

    # 8. Calculate the number of spaces for formatted printing
    #  Generate the correct spacing for the one item you pulled out
    receipt_iten_name_space = (26 - len(receipt_item_name))*" "
    receipt_price_space = (6 - len(str(receipt_price)))*" "
# ---------------------------------------------------------> The number of formatting spaces are correctly calculated. (6 points)
# ------------------------------------------------------------> Space strings are created using string multiplication. (4 points)

    # 9. Create space strings
    # math for the string

    #**********************************************
    #********** Compleated in previous line *******
    #**********************************************

    # 10. Print the item name, price, and quantity
    #     Itme name / space variable / "pipe" / price / "pipe" / qty
    print(f"{receipt_item_name}{receipt_iten_name_space}| ${receipt_price}{receipt_price_space}| {receipt_quantity}")
# ------------------------------------------> The customer's order is printed with the item name, price, and quantity. (6 points)

# 11. Calculate the cost of the order using list comprehension
#    Multiply the price by quantity for each item in the order list, then sum()
#    and print the prices.
receipt_total = 0
for sub_t_dict in order:
    receipt_total = float(receipt_total) + (sub_t_dict["Price"] * sub_t_dict["Quantity"])
# ---------------------------------------------> List comprehension is used to calculate the total price of the order. (10 points)

receipt_total = format(receipt_total,".2f")

# test_01 = sum(order[i]["Price"])
# print(test_01)
# print(order[0]["Price"])

# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

print(f"\nYour total today is : ${receipt_total}\n")
# --------------------------------------------------> The total price of the order is printed to the screen. (4 points)
print("Thank you for shopping at the AI Bootcamp Food Truck.")



