import random
def get_order_default():
    paper_color = "yellow"
    quantity = "10"
    return "I need " + str(quantity) + " of the " + paper_color + " paper"


print(get_order_default())

def get_order_from_user():
    paper_color = input("Enter a paper color: ")
    quantity = input("Enter quantity: ")
    return "I need " + str(quantity) + " of the " + paper_color + " paper"

# print(get_order_from_user())

def get_random_order():
    color_options = ['yellow', 'blue', 'pink', 'white']
    quantity_options = [10, 20, 30, 50, 80, 100]
    return "I need " + str(random.choice(quantity_options)) + " of the " + random.choice(color_options) + " paper"

print(get_random_order())
