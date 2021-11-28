from classes import *
import mysql.connector
import sys


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

            # try to get authentication by checking username and password through db
            # then pass that return value to the while loop

            flag = get_authentication(username, pswd)

            # if everything works fine print other menu
            while flag:
                print('What page would you like to go to?')
                print('0. Books'
                      '\n1. Shirts'
                      '\n2. Account'
                      '\n3. Cart'
                      '\n4. Logout')

                option = input('Please select a menu option (enter the number): ')

                if option == '0':
                    print("Welcome to the Books page!")
                    print('Menu options: ')
                    print('0. View all Books'
                          '\n1. Add item to cart'
                          '\n2. Go back')

                    flag = input('Please select a menu option (enter the number): ')


                elif option == '1':
                    print("Welcome to the Shirts page!")
                    print('Menu options: ')
                    print('0. View all Shirts'
                          '\n1. Add item to cart'
                          '\n2. Go back')

                    flag = input('Please select a menu option (enter the number): ')


                elif option == '2':
                    print("Account page: ")
                    print('Menu options: ')
                    print('0. View order history'
                          '\n1. Edit account info'
                          '\n2. Delete account'
                          '\n3. Go back')

                    flag = input('Please select a menu option (enter the number): ')


                elif option == '3':
                    print('Cart page: ')
                    print('Menu options: ')
                    print('0. View Cart'
                          '\n1. Remove item from cart'
                          '\n2. Checkout'
                          '\n3. Go back')

                    flag = input('Please select a menu option (enter the number): ')


                elif option == '4':
                    print('Logging out......')
                    flag = False

        # calls function to create account
        elif choice == '1':
            create_account()

        # exits the program
        elif choice == '2':
            break


# tries to see if such username or password exists in db
# if exists instantiate the user object
def get_authentication(username, password):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="e_commerce"
        )
        print("Successful connection.")

    except:
        print("Failed connection.")
        ## exits the program if unsuccessful
        sys.exit()

    cursor = connection.cursor()
    query = "SELECT * FROM User WHERE username=%s AND password=%s"
    param = (username, password)
    cursor.execute(query, param)
    result = cursor.fetchall()

    # if username & password was found/correct instantiate user object and log user in
    if len(result) == 1:
        # instantiate User Object here
        # use result variable to instantiate User object
        print("Logged in successful")

        # store tuple in 'flag' variable and grab user info
        flag = result[0]
        userid = flag[0]
        username = flag[1]
        pswd = flag[2]
        email = flag[3]
        phone = flag[4]
        shipping = flag[5]
        credit_num = flag[6]
        billing = flag[7]

        # INSTANTIATE USER OBJECT HERE!!!!

        print(result)

        # returns the user object and the bool flag
        return True
    else:
        print('Failed to Log in')
        return False


# ask user for information and create account for user
def create_account():

    # ask user for info. input
    print('\nPlease fill out the form.')
    username = input('Create a Username: ')
    pswd = input('Create a Password: ')
    email = input('Email: ')
    phone = input('Phone: ')
    shipping = input('Shipping address: ')
    credit_num = input('Credit card number: ')
    billing = input('Billing address: ')

    # connect to db
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="e_commerce"
        )
        print("Successful connection.")

    except:
        print("Failed connection.")
        ## exits the program if unsuccessful
        sys.exit()

    # insert new user info into db
    try:
        cursor = connection.cursor()
        query = 'INSERT INTO User (username, password, email, contact, shipping, credit, billing) ' \
                'VALUES (%s, %s, %s, %s, %s, %s, %s)'
        param = (username, pswd, email, phone, shipping, credit_num, billing)
        cursor.execute(query, param)
        connection.commit()
        print(cursor.rowcount, " record inserted.")
        print('Successfully created account')
    except:
        print('Failed to create account')

    return 0


if __name__ == '__main__':
    main()
