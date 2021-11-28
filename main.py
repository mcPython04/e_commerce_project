import classes
import mysql.connector
import sys
import pandas as pd
import pymysql
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder
import sys


def main():
    print('Welcome to our cmd e-commerce shop!!!')

    while True:
        # info about currently logged in user
        user = None

        print('\n0: Login')
        print('1: Create Account')
        print('2: Quit program')

        choice = input('Please select a menu option (enter the number): ')

        if choice == '0':
            userID = input('UserID: ')
            pswd = input('Password: ')

            # try to get authentication by checking username and password through db
            # then pass that return value to the while loop

            user = classes.User()
            user.login(userID, pswd)
            auth_flag = user.authflag

            # if everything works fine print other menu
            while auth_flag:
                print('What page would you like to go to?')
                print('0. Books'
                      '\n1. Shirts'
                      '\n2. Account'
                      '\n3. Cart'
                      '\n4. Logout')

                option = input(
                    'Please select a menu option (enter the number): ')

                if option == '0':
                    print("Welcome to the Books page!")
                    print('Menu options: ')

                elif option == '1':
                    print("Welcome to the Shirts page!")
                    print('Menu options: ')

                elif option == '2':
                    print("Account page: 'Please select a menu option")
                    print('0. Update the password'
                            '\n1. Update your email'
                            '\n2. Update your shipping address'
                            '\n3. Update your billing address'
                            '\n4. Update your credit card number'
                            '\n5. Update your contact'
                            '\n6. Show all my account information'
                            '\n7. Delete your account')
                    accnt_option= input("Enter the number : ")

                    if accnt_option == '0':
                        changed_pswd = input('Update your Password: ')
                        user.set_pswd(changed_pswd)

                    elif accnt_option == '1':
                        changed_email = input('Update your email: ')
                        user.set_email(changed_email)


                    elif accnt_option == '2':
                        changed_ship_addr = input('Update your shipping address: ')
                        user.set_ship_addr(changed_ship_addr)


                    elif accnt_option == '3':
                        changed_bill_addr = input('Update your billing address: ')
                        user.set_bill_addr(changed_bill_addr)

                    elif accnt_option == '4':
                        changed_credit_num = input('Update your credit card number: ')
                        user.set_credit_num(changed_credit_num)

                    elif accnt_option == '5':
                        changed_contact = input('Update your contact: ')
                        user.set_contact(changed_contact)

                    elif accnt_option == '6':
                        print("Here is your account information: ")
                        user.show_info()

                    elif accnt_option == '7':
                        user.delete_accnt()
                        auth_flag = False

                elif option == '3':
                    print('Cart page: ')
                    print('Menu options: ')

                elif option == '4':
                    del user
                    print('Logging out......')
                    auth_flag = False

        # calls function to create account
        elif choice == '1':
            create_account()

        # exits the program
        elif choice == '2':              
            break


# ask user for information and create account for user
def create_account():

    # ask user for info. input
    print('\nPlease fill out the form.')
    userID = input('Create a UserID: ')
    username = input('Create a Username: ')
    pswd = input('Create a Password: ')
    email = input('Email: ')
    phone = input('Phone: ')
    shipping = input('Shipping address: ')
    credit_num = input('Credit card number: ')
    billing = input('Billing address: ')

    user = classes.User()
    user.signup(userID, username, pswd, email, phone, shipping, credit_num, billing)

    return 0


if __name__ == '__main__':
    main()
