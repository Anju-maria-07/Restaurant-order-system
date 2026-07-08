from menu import MENU_ITEMS

def new_order(orders):
    table_no = int(input('enter the table no: '))
    item_list=[]

    while True:
        print('1. Add item')
        print('2. save and finish order')
        print('3. cancel order')

        choice=int(input('enter your choice (eg.1,2...): '))
        if choice==1:

            item_no =int(input('enter the item no: '))
            if item_no in MENU_ITEMS:

                quantity = int(input('enter the quantity: '))

                found = False
                
                for item in item_list:
                    if item['item_no'] == item_no:
                        found = True
                        item['quantity'] += quantity

                if found == False:
                    item_dic={
                        'item_no':item_no ,
                        'quantity': quantity
                    }
                    item_list.append(item_dic)
            else:
                print('invalid item no!!. please select the ryt item number.')


        elif choice==2:
            if len(item_list)==0:
                print('No items added yet.')
                print('Please add atleast one item to finish the order.')

            else:
                order={
                'table_no': table_no,
                'items': item_list
               }
                orders.append(order)
                break

        elif choice==3:
            print('order cancelled!!')
            break
        else:
            print('invalid choice!!')

def view_current_order(orders):
    if len(orders) == 0:
        print('no orders yet!!')
    else:
        for i in range(len(orders)):
            print(i+1,'. table no:',orders[i]['table_no'])
            for item in orders[i]['items']:
                item_no_selected= item['item_no']
                item_name= MENU_ITEMS[item_no_selected]['item_name']
                print ( f" {item_name :<25} x {item['quantity']}")

            print('-----------------------------')

def add_item(orders):
    if len(orders) == 0:
        print('no oders yet')

    else:
        table_no=int(input('enter the table number: '))
        found_table =False
        for order in orders:
            if order['table_no'] == table_no:
                found_table = True

                item_no = int(input('enter the item number to be added: '))
                if item_no in MENU_ITEMS:
                    quantity = int(input('enter the quantity of item: '))

                    found = False
                    for item in order['items']:
                        if item['item_no'] == item_no:
                            found = True

                            item['quantity']+= quantity

                    if found == False:

                        item_dic = {
                                'item_no': item_no,
                                'quantity': quantity
                            }
                        order['items'].append(item_dic)


                else:
                    print('invalid item no!!!')

        if not found_table:
            print('No order in that table !!')            

def remove_item(orders):
    if len(orders) == 0 :
        print (' no orders yet!!')

    else:
        table_no_del =int(input('enter the table no of the item to be deleted: '))

        found_table = False
        for order in orders:
            if order['table_no'] == table_no_del:
                found_table = True

                item_no_del = int(input('enter the item no to be deleted: '))
                found_item = False

                for item in order['items']:
                    if item['item_no'] == item_no_del :
                        found_item = True
                        order['items'].remove(item)
                        print(' successfully deleted item !!')
                        break

                if found_item == False:
                    print('item no not found, item no: ',item_no_del , 'has never been ordered!!')
        if found_table == False:
            print('table no not found, no order in that table yet !!')

def cancel_order(orders):
    if len(orders) == 0:
        print('No orders yet !!')

    else:
        table_no_cancel = int(input('enter the table no to cancel order: '))
        found = False

        for order in orders:
            if order['table_no'] == table_no_cancel:
                found = True
                orders.remove(order)
                print('Successfully cancelled order !!!')
                break

        if not found:
            print('there isno order for table no: ', table_no_cancel )

    