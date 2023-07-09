from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

make_coffee = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

machine_on = True

print(menu.get_items())

while machine_on:
    order = input(f"What would you like? ({menu.get_items()}): ").lower()
    if order == "report":
        make_coffee.report()
        money.report()
        continue
    elif order == "off":
        break
    elif menu.find_drink(order) is not None:
        drink = menu.find_drink(order)
        cost = menu.find_drink(order).cost
        if make_coffee.is_resource_sufficient(drink):
            if money.make_payment(cost):
                make_coffee.make_coffee(drink)
