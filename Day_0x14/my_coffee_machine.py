import math

# Resource values for the coffee machine
water = 300
milk = 200
coffee = 100
money = 0

# Drink prices
espresso_price = 2.5
latte_price = 3.5
cappuccino_price = 4

# Drink recipes
espresso = {"water": 30, "coffee": 7}
latte = {"water": 200, "milk": 50, "coffee": 7}
cappuccino = {"water": 100, "milk": 30, "coffee": 7}

# Coin values
quarters = 0.25
dimes = 0.1
nickels = 0.05
pennies = 0.01

while True:
    # Prompt user for their drink choice
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # Check if user entered "off" to turn off the machine
    if choice == "off":
        print("Turning off coffee machine...")
        break

    # Check if user entered "report" to generate a report
    if choice == "report":
        print("Water: " + str(water) + "ml")
        print("Milk: " + str(milk) + "ml")
        print("Coffee: " + str(coffee) + "g")
        print("Money: $" + str(money))
        continue

    # Check if there are enough resources to make the chosen drink
    if choice == "espresso":
        if water < espresso["water"] or coffee < espresso["coffee"]:
            print("Sorry, there are not enough resources to make an espresso.")
            continue
        drink_price = espresso_price
    elif choice == "latte":
        if water < latte["water"] or milk < latte["milk"] or coffee < latte["coffee"]:
            print("Sorry, there are not enough resources to make a latte.")
            continue
        drink_price = latte_price
    elif choice == "cappuccino":
        if water < cappuccino["water"] or milk < cappuccino["milk"] or coffee < cappuccino["coffee"]:
            print("Sorry, there are not enough resources to make a cappuccino.")
            continue
        drink_price = cappuccino_price
    else:
        print("Invalid choice. Please enter a valid drink.")
        continue

    # Get the user's coin input
    quarters_inserted = int(input("Insert quarters: "))
    dimes_inserted = int(input("Insert dimes: "))
    nickels_inserted = int(input("Insert nickels: "))
    pennies_inserted = int(input("Insert pennies: "))

    # Calculate the monetary value of the coins inserted
    money_inserted = (quarters * quarters_inserted) + (dimes * dimes_inserted) + (nickels * nickels_inserted) + (pennies * pennies_inserted)
    if money_inserted < drink_price:
        print("Sorry, that's not enough money. Money refunded.")
        continue
    elif money_inserted > drink_price:
        change = money_inserted - drink
