menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

loop = True

water_left = 300
milk_left = 200
coffee_left = 100
profit = 0

while loop == True:

    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee == "report":
        print(f"Water: {water_left}ml")
        print(f"Milk: {milk_left}ml")
        print(f"Coffee: {coffee_left}g")
        profit = round(profit,2)
        print(f"Money: ${profit}")

    elif coffee == "off":
        loop = False


    elif water_left < menu[coffee]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        loop = False

    else:
        water_left -= menu[coffee]["ingredients"]["water"]
        if coffee != "espresso":
            milk_left -= menu[coffee]["ingredients"]["milk"]
        coffee_left -= menu[coffee]["ingredients"]["coffee"]
        print("Please insert coins.")
        quarters = int(input("how many quarters?: ")) * .25
        dimes = int(input("how many dimes?: ")) * .10
        nickles = int(input("how many nickles?: ")) * .05
        pennies = int(input("how many pennies?: ")) * .01

        total = quarters + dimes + nickles + pennies
        profit += total
        if total < menu[coffee]["cost"]:
            print("Sorry that's not enough money. Money refunded!")
            water_left += menu[coffee]["ingredients"]["water"]
            water_left += menu[coffee]["ingredients"]["milk"]
            water_left += menu[coffee]["ingredients"]["coffee"]
            profit -= total

        else:
            item_cost = menu[coffee]["cost"]
            change = round(total - item_cost, 2)
            print(f"Here is ${change} in change.\nHere is your {coffee}. Enjoy!")
            profit -= change


