class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    
    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
    
    def is_resource_sufficient(self, drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True
    
    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}. Enjoy!")
    
    def fill_resources(self):
        print("Filling the machine...")
        self.resources["water"] += int(input("How much water to add (ml)? "))
        self.resources["milk"] += int(input("How much milk to add (ml)? "))
        self.resources["coffee"] += int(input("How much coffee to add (g)? "))
        print("Machine refilled!")