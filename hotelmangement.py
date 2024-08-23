# Define menu of restaurant
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 20,
    'Tea': 20,
    'Dosa (Butter)': 125,
    'Onion Dosa (Butter)': 130,
    'Sambhar Rice': 60,
    'Curd Rice': 50,
    'Veg. Fried Rice': 50

}

# Greeting
print("Welcome to Cafe")

# Display Menu
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs20\nTea: Rs20\nDosa (Butter): Rs 125\nOnion Dosa (Butter): Rs130\nSambhar Rice : Rs60\nCurd Rice : Rs50\nVeg. Fried Rice: Rs50")

# Initialize order total
order_total = 0

# First item order
item_1 = input("Enter the name of the item you want to order: ").title()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available yet!")

# Asking for another order
another_order = input("Do you want to add another item? (Yes/No): ").strip().capitalize()
if another_order == "Yes":
    item_2 = input("Enter the name of the second item: ").title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available!")
    
# Print the final total
print(f"The total amount to pay is Rs{order_total}")