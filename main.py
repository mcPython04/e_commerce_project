import classes


def main():
    print('Welcome to our cmd e-commerce shop!!!')

    while True:
        print('\n0: Login')
        print('1: Create Account')
        print('2: Quit program')

        choice = input('Please select a menu option (enter the number): ')

        if choice == '0':
            username = input('Username: ')
            pswd = input('Password: ')

            # if everything works fine print other menu
            while True:
                print('0. View Books')
                print('1. View Shirts')
                print('2. Add Item to Cart')
                print('3. Remove Item from Cart')
                print('4. Checkout Item from Cart')
                print('5. View Order History')
                print('6. Edit Account')
                print('7. Delete Account')
                print('8. Logout')

                option = input('Please select a menu option (enter the number): ')


        elif choice == '1':
            print('create account form here')

        elif choice == '2':
            break


if __name__ == '__main__':
    main()
