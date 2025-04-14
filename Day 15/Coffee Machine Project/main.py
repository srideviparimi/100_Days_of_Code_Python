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
    "coffee": 10,
}
money=0
def check_resources(coffee):
    i_list=MENU[coffee]["ingredients"]
    availability=[]
    for key in i_list:
        if key in resources:
            availability.append(resources[key]>i_list[key])
    return False if False in availability else True

def print_report():
    print(f"Water : {resources["water"]} ml")
    print(f"Milk : {resources["milk"]} ml")
    print(f"Coffee : {resources["coffee"]} ml")
    print(f"Money : ${money}")


coffee=input( "What would you like? (espresso/latte/cappuccino)?").lower()
if coffee=="espresso":
    print("espresso")
    avail=check_resources(coffee)

elif coffee=="latte":
    print("latte")
    print(check_resources(coffee))
elif coffee=="cappuccino":
    print("cappuccino")
    print(check_resources(coffee))
elif coffee=="report":
    print("Report")
    print_report()
elif coffee=="off":
    print("terminate")