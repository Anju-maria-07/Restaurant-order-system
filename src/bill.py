from menu import MENU_ITEMS

def generate_bill(orders):
    if len(orders) == 0:
        print('No orders yet !!')
    else:
        table_no_bill = int(input('Enter the table no: '))

        for order in orders:
            if order['table_no'] == table_no_bill:
                print('==========Restaurant Name==========')
                print('===============Bill===============')
                print('')
                print('Table No: ',table_no_bill)
                print(f" {'item':<25} {'Qty':<5} {'Amount':<10}")

                total=0

                for item in order['items']:
                    
                    item_name = MENU_ITEMS[item['item_no']]['item_name']
                    price = MENU_ITEMS[item['item_no']]['price']
                    quantity_price = price * item['quantity']

                    total += quantity_price

                    print(f"{item_name:<25} {item['quantity']:<5} Rs.{quantity_price}") 

                print('-------------------------------------------------------------------')
                print(f"{'total':<30} Rs {total}")
