from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker_obj=CoffeeMaker()
menu_obj=Menu()
money_machine_obj=MoneyMachine()
should_continue=True

while should_continue:
    choice=input(f"Which coffee would you like {menu_obj.get_items()}")
    if choice=="report":
        print(coffee_maker_obj.report())
    elif choice in menu_obj.get_items():
        drink=menu_obj.find_drink(choice)
        if coffee_maker_obj.is_resource_sufficient(drink) and money_machine_obj.make_payment(drink.cost):
            coffee_maker_obj.make_coffee(drink)
        else:
            should_continue=False
    else:
        should_continue=False