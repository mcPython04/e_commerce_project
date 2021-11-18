import classes
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

                if option == '8':
                    print('Logging out......')
                    flag = False

        elif choice == '1':
            print('create account form here')

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

    if len(result) == 1:
        # instantiate User Object here
        # use result variable to instantiate User object
        print("Logged in successful")
        print(result)

        return True
    else:
        print('Failed to Log in')
        return False


if __name__ == '__main__':
    main()
