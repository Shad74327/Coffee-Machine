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
    available_water = resources["water"]
    available_milk = resources["milk"]
    available_coffee = resources["coffee"]

    required_water = MENU[order]["ingredients"]["water"]
    required_milk = MENU[order]["ingredients"]["milk"]
    required_coffee = MENU[order]["ingredients"]["coffee"]

    if available_water >= required_water and available_milk >= required_milk and available_coffee >= required_coffee:
        return True
    else:
        return False


def calculate_cost(q_count, d_count, n_count, p_count, chosen_item):
    q_worth = q_count * currency["quarters"]
    d_worth = d_count * currency["dimes"]
    n_worth = n_count * currency["nickles"]
    p_worth = p_count * currency["pennies"]

    total = q_worth + d_worth + n_worth + p_worth

    if total >= MENU[chosen_item]["cost"]:
        return total - MENU[chosen_item]["cost"]
    else:
        return False


def update_inventory(chosen_item, inventory):
    inventory["water"] -= MENU[chosen_item]["ingredients"]["water"]
    inventory["milk"] -= MENU[chosen_item]["ingredients"]["milk"]
    inventory["coffee"] -= MENU[chosen_item]["ingredients"]["coffee"]


while True:
    prompt = input("What do you want? (espresso/latte/cappuccino): ").lower()

    if prompt == "off":
        """Turning off the system."""
        break

    if prompt == "report":
        """Generating report of the inventory."""
        water = report("water")
        milk = report("milk")
        coffee = report("coffee")
        deposit = report("deposit")

        print(f"Water: {water}")
        print(f"Milk: {milk}")
        print(f"Coffee: {coffee}")
        print(f"Money: ${deposit}")

    if prompt == "espresso":
        ingredients_available = check_resources(prompt)

        if ingredients_available:
            print("Please insert coins.")
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))

            change = calculate_cost(quarters, dimes, nickles, pennies, prompt)

            if not change:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                resources["deposit"] += MENU[prompt]["cost"]
                update_inventory(prompt, resources)
                print(f"Here is ${"%.2f" % change} in change.")
                print(f"Here is your {prompt}! Enjoy!")
        else:
            print("Sorry! Insufficient inventory.")
    # elif prompt == "latte":
    #     ingredients_available = check_resources(prompt)
    # elif prompt == "cappuccino":
    #     ingredients_available = check_resources(prompt)
