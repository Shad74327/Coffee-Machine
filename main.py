MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "deposit": 0,
}

currency = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}


def report(inventory):
    """Fetching inventory data."""
    return resources[inventory]


def check_resources(order):
    """Checking availability of the resources."""
    water_stock = resources["water"]
    milk_stock = resources["milk"]
    coffee_stock = resources["coffee"]

    required_water = MENU[order]["ingredients"]["water"]
    required_milk = MENU[order]["ingredients"]["milk"]
    required_coffee = MENU[order]["ingredients"]["coffee"]

    if water_stock >= required_water and milk_stock >= required_milk and coffee_stock >= required_coffee:
        return True
    else:
        return False


def calculate_cost(q_count, d_count, n_count, p_count, chosen_item):
    """Calculate the total cost as well as the change."""
    q_worth = q_count * currency["quarters"]
    d_worth = d_count * currency["dimes"]
    n_worth = n_count * currency["nickles"]
    p_worth = p_count * currency["pennies"]

    total = q_worth + d_worth + n_worth + p_worth

    if total >= MENU[chosen_item]["cost"]:
        """Checking for sufficient deposit for the order and returning the change if necessary."""
        return total - MENU[chosen_item]["cost"]
    else:
        """Insufficient deposit."""
        return False


def update_inventory(chosen_item, inventory):
    """Updating the inventory after each order."""
    inventory["water"] -= MENU[chosen_item]["ingredients"]["water"]
    inventory["milk"] -= MENU[chosen_item]["ingredients"]["milk"]
    inventory["coffee"] -= MENU[chosen_item]["ingredients"]["coffee"]


def process_order(item_chosen):
    """Processing the order."""
    ingredients_available = check_resources(item_chosen)

    if ingredients_available:
        print("Please insert coins.")
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickles = int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))

        change = calculate_cost(quarters, dimes, nickles, pennies, item_chosen)

        if not change:
            """Insufficient deposit."""
            print("Sorry, that's not enough money. Money refunded.")
        else:
            """Sufficient deposit. Delivering order."""
            resources["deposit"] += MENU[item_chosen]["cost"]
            update_inventory(item_chosen, resources)
            print(f"Here is ${"%.2f" % change} in change.")
            print(f"Here is your {item_chosen}! Enjoy!")
    else:
        print("Sorry! Insufficient inventory.")


while True:
    prompt = input("What do you want? (espresso/latte/cappuccino): ").lower()

    if prompt == "off":
        """Turning off the system."""
        break

    elif prompt == "report":
        """Generating report of the inventory."""
        water = report("water")
        milk = report("milk")
        coffee = report("coffee")
        deposit = report("deposit")

        print(f"Water: {water}")
        print(f"Milk: {milk}")
        print(f"Coffee: {coffee}")
        print(f"Money: ${deposit}")

    elif prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        process_order(prompt)

    else:
        print("Invalid answer! Please try again.")
