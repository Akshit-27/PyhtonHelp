# Calculate the total of items in the cart.

def cost_calculator(cart):
    """This function help to calculate the total cost of items added in the cart"""
    total_cost = 0
    for items in cart:
        print(items["cost"])
        total_cost = total_cost + int(items["cost"])
    return total_cost


cart = [
    {'name': 'Apple', 'cost': '200'},
    {'name': 'Grapes', 'cost': '180'},
    {'name': 'Mango', 'cost': '250'},
    {'name': 'Cherry', 'cost': '100'},
    {'name': 'Kivi', 'cost': '115'},
    {'name': 'Avocado', 'cost': '500'},
]
print("Your Total cost is : Rs.", cost_calculator(cart))
