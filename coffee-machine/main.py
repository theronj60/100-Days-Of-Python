MENU = {
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

stillOrdering = True

while stillOrdering: 
    drinkOrder = input("What would you like? (espresso/latte/cappuccino): ")
    drinkOrder = drinkOrder.lower()

    def drink(drink):
        if (drink == 'espresso'):
            return MENU['espresso']
        elif (drink == 'latte'):
            return MENU['latte']
        elif (drink == 'cappuccino'):
            return MENU['cappuccino']
        else:
            return "coffee will do"    

    print(drink(drinkOrder))
    still = input("would you like to order another? y/n: " )
    if (still == 'n'):
        stillOrdering = False
        exit()
    else:
        continue

