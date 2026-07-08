
MENU_ITEMS = {
    1: {
            'item_name': 'Chicken Biriyani',
            'price':  180
        },
    2: {
            'item_name': 'Mutton Biriyani',
            'price':  200
        },
    3: {
            'item_name': 'Veg Biriyani',
            'price':  150
        },
    4: {
            'item_name': 'Chicken Fried Rice',
            'price':  160
        },
    5: {
            'item_name': 'Veg Fried Rice',
            'price':  140
        },
    6: {
            'item_name': 'Chicken Noodles',
            'price':  170
        },
    7: {
            'item_name': 'Veg Noodles',
            'price':  150
        },
    8: {
            'item_name': 'Chicken Manchurian',
            'price':  180
        },
    9: {
            'item_name': 'Pizza',
            'price':  250
        },
    10: {
            'item_name': 'Burger', 
            'price':  150
        },
    11: {
            'item_name': 'Pasta',
            'price':  190
        },
    12: {
            'item_name': 'Sandwich',
            'price': 120
        },
    13: {
            'item_name': 'French Fries',
            'price':  100
        },
    14: {
            'item_name': 'Coke',
            'price':  50
        },
    15: {
            'item_name': 'Coffee',
            'price':  25
        },
    16: {
            'item_name': 'Tea',
            'price':  20
        },
    17: {
            'item_name': 'Fresh Lime Juice',
            'price':  30
        },
    18: {
            'item_name': 'Cold Coffee',
            'price': 80
        }
    }

def display_food_menu():
    print('===FOOD MENU===')
    for item_no,item in MENU_ITEMS.items():
        print(f"{item_no:<3}. {item['item_name']:<25} Rs.{item['price']}")

