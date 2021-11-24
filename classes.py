import mysql.connector
import sys


def User():

    def __init__(self, userID, password):  # sign-in
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

        # retrieve user info from db
        try:
            cursor = connection.cursor()
            query = 'INSERT INTO User (username, password, email, contact, shipping, credit, billing) ' \
                    'VALUES (%s, %s, %s, %s, %s, %s, %s)'
            param = (__userID, __userName, __password, __email, __contact,
                    __shippingAddress, __creditNumber, __billingAddress)
            cursor.execute(query, param)
            connection.commit()
            print(cursor.rowcount, " record inserted.")
            print('Successfully created account')
        except:
            print('Failed to create account')

            

    def __init__(self, userID, userName, password, email, contact, shippingAddress="", creditNumber="", billingAddress=""):  # sign-up
        # required feild : userID, userName, password, email, contact

        self.__userID = userID
        self.__userName = userName
        self.__password = password
        self.__email = email
        self.__contact = contact
        self.__shippingAddress = shippingAddress
        self.__creditNumber = creditNumber
        self.__billingAddress = billingAddress

    # ask user for info. input
    print('\nPlease fill out the form.')
    __userID = input('Create a UserID: ')
    __userName = input('Create a Username: ')
    __password = input('Create a Password: ')
    __email = input('Email: ')
    __contact = input('Contact: ')
    __shippingAddress = input('Shipping address: ')
    __creditNumber = input('Credit card number: ')
    __billingAddress = input('Billing address: ')

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
        param = (__userID, __userName, __password, __email, __contact,
                 __shippingAddress, __creditNumber, __billingAddress)
        cursor.execute(query, param)
        connection.commit()
        print(cursor.rowcount, " record inserted.")
        print('Successfully created account')
    except:
        print('Failed to create account')

    def __del__(self): print(f" Your account ({self.__userID}) is deleted. ")

    return
