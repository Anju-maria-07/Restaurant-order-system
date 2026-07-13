import json

def save_orders(orders):
    with open('orders.json','w') as file:
        json.dump(orders,file)


def load_orders():
    try:
        with open("orders.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []