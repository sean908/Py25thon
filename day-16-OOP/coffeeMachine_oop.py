from menu import Menu
from coffee_machine import CoffeeMachine
from money_machine import MoneyMachine


def main():
    menu = Menu()
    coffee_machine = CoffeeMachine()
    money_machine = MoneyMachine()
    
    is_on = True
    
    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ").lower()
        
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_machine.report()
            money_machine.report()
        elif choice == "fill":
            coffee_machine.fill_resources()
        else:
            drink = menu.find_drink(choice)
            if drink:
                if coffee_machine.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_machine.make_coffee(drink)


if __name__ == "__main__":
    main()