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

            # get authentication by checking username and password through db
            # then pass that return value to the while loop
            user, stat_flag = get_authentication(username, pswd)

            # if everything works fine print other menu
            while stat_flag:
                print('\nWelcome ' + user.username + '!!!')
                print('What page would you like to go to?')
                print('0. Books'
                      '\n1. Shirts'
                      '\n2. Account'
                      '\n3. Cart'
                      '\n4. Logout')

                option = input('Please select a menu option (enter the number): ')

                # Books menu
                while option == '0':
                    print("\nWelcome to the Books page!")
                    print('Menu options: ')
                    print('0. View all books'
                          '\n1. Add item to cart'
                          '\n2. Go back')

                    flag = int(input('Please select a menu option (enter the number): '))

                    if flag == 0:
                        view_books()

                    elif flag == 1:
                        itemID = int(input('Please enter the Item ID to add to cart: '))
                        quantity = int(input('Please enter the quantity you like: '))
                        add_cart(user.userid, itemID, quantity)

                    elif flag == 2:
                        break

                # Shirts menu
                while option == '1':
                    print("\nWelcome to the Shirts page!")
                    print('Menu options: ')
                    print('0. View all shirts'
                          '\n1. Add item to cart'
                          '\n2. Go back')

                    flag = int(input('Please select a menu option (enter the number): '))

                    if flag == 0:
                        view_shirts()

                    elif flag == 1:
                        itemID = int(input('Please enter the Item ID to add to cart: '))
                        quantity = int(input('Please enter the quantity you like: '))
                        add_cart(user.userid, itemID, quantity)

                    elif flag == 2:
                        break

                # Account menu
                while option == '2':
                    print("\nAccount page: ")
                    print('Menu options: ')
                    print('0. View order history'
                          '\n1. Edit account info'
                          '\n2. Delete account'
                          '\n3. Go back')

                    flag = int(input('Please select a menu option (enter the number): '))

                    if flag == 0:
                        view_order(user.userid)

                    # edit account menu
                    elif flag == 1:
                        print('\nCurrent account info: ')
                        print('\nUser ID: ' + str(user.userid))
                        print('Username: ' + user.username)
                        print('Password: ' + user.pswd)
                        print("Email: " + user.email)
                        print("Phone: " + user.phone)
                        print("Shipping: " + user.shipping)
                        print('Credit Card Number: ' + user.credit_num)
                        print('Billing: ' + user.billing)

                        print('\nOptions: ')
                        print('0. Update shipping info.'
                              '\n1. Update payment info. '
                              '\n2. Go back')

                        flag1 = int(input('Select a menu option: '))

                        if flag1 == 0:
                            new = input('Enter new shipping address: ')
                            user = update_shipping(new, user)

                        elif flag1 == 1:
                            new = input('Enter new credit card info: ')
                            user = update_credit(new, user)

                        elif flag1 == 2:
                            break

                    # delete account
                    elif flag == 2:
                        ans = input('Are you sure you want to delete the account (y/n)? ')

                        if ans == 'y':
                            delete_account(user.userid)
                            user = None
                            stat_flag = False
                            break

                        elif ans == 'n':
                            break

                    # go back
                    elif flag == 3:
                        break

                # Cart menu
                while option == '3':
                    print('\nCart page: ')
                    print('Menu options: ')
                    print('0. View Cart'
                          '\n1. Remove item from cart'
                          '\n2. Checkout'
                          '\n3. Go back')

                    flag = int(input('Please select a menu option (enter the number): '))

                    if flag == 0:
                        view_cart(user.userid)

                    elif flag == 1:
                        itemID = int(input('What item you would want to remove from cart (enter item ID)? '))
                        remove_cart(user.userid, itemID)

                    elif flag == 2:
                        ans = input('Proceed to checkout? (y/n)')

                        if ans == 'y':
                            checkout(user.userid)
                            break
                        else:
                            break

                    elif flag == 3:
                        break

                # Logout option
                while option == '4':
                    print('Logging out......')
                    stat_flag = False
                    user = None
                    break

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
        print("Login successful")

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
        user = User(userid, username, pswd, email, phone, shipping, credit_num, billing)

        return user, True
    else:
        print('Failed to Log in')
        return None, False


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


# function that queries database to update shipping info
def update_shipping(new, user):
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

    try:
        cursor = connection.cursor()
        query = 'UPDATE User SET shipping = %s WHERE userID = %s'
        param = (new, user.userid)
        cursor.execute(query, param)
        connection.commit()
        print(cursor.rowcount, " record inserted.")
        print('Successfully updated shipping info')
    except:
        print('Failed to update shipping info')

    print('Re-logging in...')
    user, flag = get_authentication(user.username, user.pswd)
    return user


# function that queries database to update credit card info
def update_credit(new, user):
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

    try:
        cursor = connection.cursor()
        query = 'UPDATE User SET credit = %s WHERE userID = %s'
        param = (new, user.userid)
        cursor.execute(query, param)
        connection.commit()
        print('Successfully updated credit card info')
    except:
        print('Failed to update credit card info')

    print('Re-logging in...')
    user, flag = get_authentication(user.username, user.pswd)
    return user


# queries the database and deletes an account
def delete_account(userID):
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

    try:
        cursor = connection.cursor()
        query = f'DELETE FROM User WHERE userID = {userID}'
        cursor.execute(query)
        connection.commit()
        print(cursor.rowcount, " record deleted.")
        print('Successfully deleted account')
    except:
        connection.rollback()
        print('Failed to delete account')


# displays all the shirts
def view_shirts():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="e_commerce"
        )

    except:
        print("Failed connection.")
        ## exits the program if unsuccessful
        sys.exit()

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Items WHERE category LIKE \"shirt\"')
    result = cursor.fetchall()

    print('\nShirt Items: ')

    for i in result:
        print('\nItem ID: ' + str(i[0]))
        print('Shirt Name: ' + i[1])
        print('Price: ' + str(i[2]))
        print('Inventory: ' + str(i[3]))


# displays all the books
def view_books():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="e_commerce"
        )

    except:
        print("Failed connection.")
        ## exits the program if unsuccessful
        sys.exit()

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Items WHERE category LIKE \"book\"')
    result = cursor.fetchall()

    print('\nBook Items: ')

    for i in result:
        print('\nItem ID: ' + str(i[0]))
        print('Book Name: ' + i[1])
        print('Price: ' + str(i[2]))
        print('Inventory: ' + str(i[3]))


# adds item to cart in database
def add_cart(userID, itemID, quantity):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="e_commerce"
        )

    except:
        print("Failed connection.")
        ## exits the program if unsuccessful
        sys.exit()

    # insert item into cart
    try:
        cursor = connection.cursor()
        query = 'INSERT INTO Cart (userID, itemID, quantity) ' \
                'VALUES (%s, %s, %s)'
        param = (userID, itemID, quantity)
        cursor.execute(query, param)
        connection.commit()
        print('Successfully added item to cart')
    except:
        print('Failed to add item to cart')


# view cart
def view_cart(userID):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="e_commerce"
        )

    except:
        print("Failed connection.")
        ## exits the program if unsuccessful
        sys.exit()

    cursor = connection.cursor()
    query = f'''
                SELECT Items.itemID AS ID,
                Items.name AS Item,
                Items.price AS Price,
                Cart.quantity AS Quantity
                From Items
                INNER JOIN Cart ON Items.itemID = Cart.itemID
                WHERE userID = {userID}
            '''
    cursor.execute(query)
    result = cursor.fetchall()

    id = []
    quantity = []
    price = []

    print('\nCart Items: ')

    for i in result:
        print('\nItem ID: ' + str(i[0]))
        print('Item name: ' + str(i[1]))
        print('Item price: ' + str(i[2]))
        print('Item quantity: ' + str(i[3]))
        print('')

        id.append(i[0])
        price.append(i[2])
        quantity.append(i[3])

    return id, price, quantity


# removes an item from the cart
def remove_cart(userID, itemID):
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

    try:
        cursor = connection.cursor()
        query = f'DELETE FROM Cart WHERE itemID = {itemID} AND userID = {userID}'
        cursor.execute(query)
        connection.commit()
        print(cursor.rowcount, " record deleted.")
        print('Successfully deleted item from cart')
    except:
        connection.rollback()
        print("Failed to delete from cart")


# checkouts the cart
def checkout(userID):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="e_commerce"
        )

    except:
        print("Failed connection.")
        ## exits the program if unsuccessful
        sys.exit()

    try:
        id, price, quantity = view_cart(userID)

        # Queries database to update inventory information on items
        count = 0
        for i in id:
            cursor = connection.cursor()
            query = f"UPDATE Items SET inventory = (inventory - {quantity[count]}) WHERE itemID = {i}"
            cursor.execute(query)
            connection.commit()
            count += 1


        total_price = 0

        # Calculates total price to create order
        count1 = 0
        for i in price:
            total_price += i * quantity[count1]
            count1 += 1

        # Calls function to create order and add order to database
        create_order(userID, total_price)

        # Empties user's cart
        cursor = connection.cursor()
        query = f"DELETE FROM Cart WHERE userID = {userID}"
        cursor.execute(query)
        connection.commit()

        print("Checkout successful!!! Successfully created order for above items!")
    except:
        print("Checkout unsuccessful.")


# function that queries database to add orders
def create_order(userID, total_price):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="e_commerce"
        )

    except:
        print("Failed connection.")
        ## exits the program if unsuccessful
        sys.exit()

    # insert new order info into db
    try:
        cursor = connection.cursor()
        query = f'INSERT INTO Orders(userID, total_price) VALUES ({userID}, {total_price})'
        cursor.execute(query)
        connection.commit()
        print('Successfully created order')
    except:
        print('Failed to create order')


# functions that displays user's order history
def view_order(userID):
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
    query = f"SELECT * FROM Orders WHERE userID = {userID}"
    cursor.execute(query)
    result = cursor.fetchall()

    print('\nOrder History: ')

    for i in result:
        print('\nOrder ID: ' + str(i[0]))
        print('Total Price: ' + str(i[2]))


if __name__ == '__main__':
    main()
