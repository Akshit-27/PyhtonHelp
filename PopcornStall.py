items = [
    {'name': 'Salted Popcorn', 'size': 'Small', 'cost': '10'},
    {'name': 'Salted Popcorn', 'size': 'Large', 'cost': '30'},
    {'name': 'Masala Popcorn', 'size': 'Small', 'cost': '15'},
    {'name': 'Masala Popcorn', 'size': 'Large', 'cost': '35'},
    {'name': 'Cheese Popcorn', 'size': 'Small', 'cost': '15'},
    {'name': 'Cheese Popcorn', 'size': 'Large', 'cost': '35'}
]

myCart = []


def show_menu():
    """This function displays all the available items """
    def get_item_name(item):
        return item['name']

    item_name=list(map(get_item_name,items))

    for names in item_name:
        print(names)

    # for item in items:
    #     print(list(item.values())[1] + " " + list(item.values())[0] + " at INR " + list(item.values())[2])


def add_item():
    pass
def show_cart():
    # print(myCart)
    pass

def checkout():
    pass

def calculate():
    for cost in myCart:
        print(list(cost.values())[2])

    pass



show_menu()
# choice = input("Enter the item you want to add")
# add_item()