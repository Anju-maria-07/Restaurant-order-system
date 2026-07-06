def new_order(orders):
    table_no=int(input('enter the table no: '))
    item_list=[]

    while True:
        print('1. Add item')
        print('2. save and finish order')
        print('3. cancel order')

        choice=int(input('enter your choice (eg.1,2...): '))
        if choice==1:

            item_no =int(input('enter the item no: '))
            quantity = int(input('enter the quantity: '))

            item_dic={
            'item_no':item_no ,
            'quantity': quantity
            }
            item_list.append(item_dic)



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
    if len(orders)==0:
        print('no orders yet!!')
    else:
        for i in range(len(orders)):
            print(i+1,'. table no:',orders[i]['table_no'])
            print('. item no:',orders[i]['item_no'],'  x',orders[i]['quantity'])

def add_item(orders):
    if len(orders)==0:
        print('no oders yet')

    else:
        table_no=int(input('enter the table number: '))
        for order in orders:
            if order['table_no']==table_no:
                item=int(input('enter the item to be added: '))
                quantity=int(input('enter the quantity of item: '))

                order['item_no']=item
                order['quantity']=quantity


if __name__=='__main__':
    orders=[]
    new_order(orders)
    print(orders)