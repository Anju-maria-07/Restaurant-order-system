from menu import display_food_menu
import order
from bill import generate_bill

def main():
    orders=[]

    while True:
        print('====================RESTAURANT ORDER SYSTEM====================')
        print('main Menu:')
        print('1. New order')
        print('2. View current order')
        print('3. Add item')
        print('4. Remove item')
        print('5. Cancel order')
        print('6. Generate bill')
        print('7.Exit')

        choice=int(input('enter your choice: '))

        if choice==1:    #new order
            display_food_menu()
            order.new_order(orders)

        elif choice==2:  #view order
            order.view_current_order(orders)

        elif choice==3:  #add item
            order.add_item(orders)

        elif choice==4:    #remove item
            order.remove_item(orders)

        elif choice==5:  #cancel order
            order.cancel_order(orders)
        elif choice==6:   #generate bill
            generate_bill(orders)

        elif choice == 7:
            print('Thank you !!')
            break

        else:
            print('invalid choice. Please enter correct choice !!!')


if __name__=='__main__':
    main()