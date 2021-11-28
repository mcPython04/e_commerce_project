import mysql.connector
import pandas as pd
import pymysql
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder
import sys
import main
import paramiko
from paramiko import SSHClient

sql_hostname = 'localhost'
sql_username = 'client_x'
sql_password = 'SecretPassword7#'
sql_main_database = 'shopping'
sql_port = 3306
#ssh_host = '192.168.0.71'
ssh_host = '170.253.135.197'
ssh_user = 'client'
ssh_password = 'SecretPassword#'
ssh_port = 22




class User():

    result = []
    __userID = ""
    __userName = ""
    __password = ""
    __email = ""
    __contact = ""
    __shippingAddress = ""
    __creditNumber = ""
    __billingAddress = ""

    def login(self, userID, password):  # sign-in
        # connect to db
        try:
            with SSHTunnelForwarder((ssh_host, ssh_port),
                                        ssh_username=ssh_user,
                                        ssh_password=ssh_password,
                                        remote_bind_address=(sql_hostname, sql_port)) as tunnel:

                    print("Trying to make a connection")
                    conn = pymysql.connect(host=sql_hostname, user=sql_username,
                            passwd=sql_password, db=sql_main_database,
                            port=tunnel.local_bind_port)

                    print("made connection")
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    query = f"SELECT * FROM user WHERE userID = '{userID}' AND password= '{password}'"
                    try:
                        cur.execute(query)
                        result = cur.fetchall()
                        result = pd.DataFrame(result)

                        print('Successfully login')
                        
        
                    except:
                        print('Failed to login')
                    
                    conn.commit()
                    conn.close
        except:
            print("Failed connection.")
            ## exits the program if unsuccessful
            sys.exit()


        # if username & password was found/correct instantiate user object and log user in
        if len(result) == 1:
            # instantiate User Object here
            # use result variable to instantiate User object
            print("Logged in successful")

            # store tuple in 'flag' variable and grab user info
            self.__userID = result['userID'][0] 
            self.__userName= result['userName'][0]
            self.__password = result['password'][0]
            __email = result['email'][0]
            print(f"###{__email}###")
            self.__contact = result['contact'][0]
            self.__shippingAddress = result['shippingAddress'][0]
            self.__creditNumber = result['creditNumber'][0]
            self.__billingAddress = result['billingAddress'][0]

            self.authflag = True
        else:
            print('Failed to Log in')
            self.authflag = False


    def signup(self,userID, userName, password, email, contact, shippingAddress="", creditNumber="", billingAddress=""):  # sign-up
        # required feild : userID, userName, password, email, contact

        self.__userID = userID
        self.__userName = userName
        self.__password = password
        self.__email = email
        self.__contact = contact
        self.__shippingAddress = shippingAddress
        self.__creditNumber = creditNumber
        self.__billingAddress = billingAddress

        try:

            with SSHTunnelForwarder((ssh_host, ssh_port),
                                    ssh_username=ssh_user,
                                    ssh_password=ssh_password,
                                    remote_bind_address=(sql_hostname, sql_port)) as tunnel:

                print("Trying to make a connection")
                conn = pymysql.connect(host=sql_hostname, user=sql_username,
                        passwd=sql_password, db=sql_main_database,
                        port=tunnel.local_bind_port)

                print("made connection")
                cur = conn.cursor(pymysql.cursors.DictCursor)
                query = f"INSERT INTO user VALUES ('{userID}','{userName}','{password}','{email}','{contact}','{shippingAddress}','{creditNumber}','{billingAddress}');"
                try:
                    cur.execute(query)
                    result = cur.fetchall()
                    result = pd.DataFrame(result)

                    print(cur.rowcount, " record inserted.")
                    print('Successfully created account')
                                
                except:
                    print('Failed to create account')
                
                conn.commit()
                conn.close

        except:
            print("Failed connection.")
            ## exits the program if unsuccessful
            sys.exit()

    

    def set_pswd(self,changed_pswd):
        try:
            with SSHTunnelForwarder((ssh_host, ssh_port),
                                        ssh_username=ssh_user,
                                        ssh_password=ssh_password,
                                        remote_bind_address=(sql_hostname, sql_port)) as tunnel:

                    print("Trying to make a connection")
                    conn = pymysql.connect(host=sql_hostname, user=sql_username,
                            passwd=sql_password, db=sql_main_database,
                            port=tunnel.local_bind_port)

                    print("made connection")
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    query = f"UPDATE user SET password = {changed_pswd} WHERE userID = '{self.__userID}';"
                    try:
                        cur.execute(query)
                        result = cur.fetchall()
                        result = pd.DataFrame(result)

                        print('Successfully update the password')
                        
                    except:
                        print('Failed to update the password')
                    
                    self.__password=changed_pswd
                    conn.commit()                    
                    conn.close
        except:
            print("Failed connection.")
            ## exits the program if unsuccessful
            sys.exit()

    def set_email(self,changed_email):
        try:
            with SSHTunnelForwarder((ssh_host, ssh_port),
                                        ssh_username=ssh_user,
                                        ssh_password=ssh_password,
                                        remote_bind_address=(sql_hostname, sql_port)) as tunnel:

                    print("Trying to make a connection")
                    conn = pymysql.connect(host=sql_hostname, user=sql_username,
                            passwd=sql_password, db=sql_main_database,
                            port=tunnel.local_bind_port)

                    print("made connection")
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    query = f"UPDATE user SET email = '{changed_email}' WHERE userID = '{self.__userID}';"
                    try:
                        cur.execute(query)
                        result = cur.fetchall()
                        result = pd.DataFrame(result)

                        print('Successfully update the email')
                        
                    except:
                        print('Failed to update the email')
                    
                    self.__email=changed_email
                    conn.commit()
                    conn.close
        except:
            print("Failed connection.")
            ## exits the program if unsuccessful
            sys.exit()

    

    def set_ship_addr(self,changed_ship_addr):
        try:
            with SSHTunnelForwarder((ssh_host, ssh_port),
                                        ssh_username=ssh_user,
                                        ssh_password=ssh_password,
                                        remote_bind_address=(sql_hostname, sql_port)) as tunnel:

                    print("Trying to make a connection")
                    conn = pymysql.connect(host=sql_hostname, user=sql_username,
                            passwd=sql_password, db=sql_main_database,
                            port=tunnel.local_bind_port)

                    print("made connection")
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    query = f"UPDATE user SET shippingAddress = {changed_ship_addr} WHERE userID = '{self.__userID}';"
                    try:
                        cur.execute(query)
                        result = cur.fetchall()
                        result = pd.DataFrame(result)

                        print('Successfully update the ShippingAddress')
                        
                    except:
                        print('Failed to update the ShippingAddress')
                    
                    self.__shippingAddress=changed_ship_addr
                    conn.commit()
                    conn.close
        except:
            print("Failed connection.")
            ## exits the program if unsuccessful
            sys.exit()
    
    def set_bill_addr(self,changed_bill_addr):
        try:
            with SSHTunnelForwarder((ssh_host, ssh_port),
                                        ssh_username=ssh_user,
                                        ssh_password=ssh_password,
                                        remote_bind_address=(sql_hostname, sql_port)) as tunnel:

                    print("Trying to make a connection")
                    conn = pymysql.connect(host=sql_hostname, user=sql_username,
                            passwd=sql_password, db=sql_main_database,
                            port=tunnel.local_bind_port)

                    print("made connection")
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    query = f"UPDATE user SET billingAddress = {changed_bill_addr} WHERE userID = '{self.__userID}';"
                    try:
                        cur.execute(query)
                        result = cur.fetchall()
                        result = pd.DataFrame(result)

                        print('Successfully update the billingAddress')
                        
                    except:
                        print('Failed to update the billingAddress')
                    
                    self.__billingAddress=changed_bill_addr
                    conn.commit()
                    conn.close
        except:
            print("Failed connection.")
            ## exits the program if unsuccessful
            sys.exit()
    
    def set_credit_num(self,changed_credit_num):
        try:
            with SSHTunnelForwarder((ssh_host, ssh_port),
                                        ssh_username=ssh_user,
                                        ssh_password=ssh_password,
                                        remote_bind_address=(sql_hostname, sql_port)) as tunnel:

                    print("Trying to make a connection")
                    conn = pymysql.connect(host=sql_hostname, user=sql_username,
                            passwd=sql_password, db=sql_main_database,
                            port=tunnel.local_bind_port)

                    print("made connection")
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    query = f"UPDATE user SET creditNumber = {changed_credit_num} WHERE userID = '{self.__userID}';"
                    try:
                        cur.execute(query)
                        result = cur.fetchall()
                        result = pd.DataFrame(result)

                        print('Successfully update the creditNumber')
                        
                    except:
                        print('Failed to update the creditNumber')
                    
                    self.__creditNumber=changed_credit_num
                    conn.commit()
                    conn.close
        except:
            print("Failed connection.")
            ## exits the program if unsuccessful
            sys.exit()

    def set_contact(self,changed_contact):
        try:
            with SSHTunnelForwarder((ssh_host, ssh_port),
                                        ssh_username=ssh_user,
                                        ssh_password=ssh_password,
                                        remote_bind_address=(sql_hostname, sql_port)) as tunnel:

                    print("Trying to make a connection")
                    conn = pymysql.connect(host=sql_hostname, user=sql_username,
                            passwd=sql_password, db=sql_main_database,
                            port=tunnel.local_bind_port)

                    print("made connection")
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    query = f"UPDATE user SET contact = {changed_contact} WHERE userID = '{self.__userID}';"
                    try:
                        cur.execute(query)
                        result = cur.fetchall()
                        result = pd.DataFrame(result)

                        print('Successfully update the contact')
                        
                    except:
                        print('Failed to update the contact')
                    
                    self.__contact=changed_contact
                    conn.commit()
                    conn.close
        except:
            print("Failed connection.")
            ## exits the program if unsuccessful
            sys.exit()

    def show_info(self):
        print(f"\n  > userID: {self.__userID}"
              f"\n  > userName: {self.__userName}"
              f"\n  > email: {self.__email}"
              f"\n  > contact: {self.__contact}"
              f"\n  > shipping Address: {self.__shippingAddress}"
              f"\n  > credit card Number: {self.__creditNumber}"
              f"\n  > billing Address: {self.__billingAddress}\n")

    def delete_accnt(self):
        try:
            with SSHTunnelForwarder((ssh_host, ssh_port),
                                        ssh_username=ssh_user,
                                        ssh_password=ssh_password,
                                        remote_bind_address=(sql_hostname, sql_port)) as tunnel:

                    print("Trying to make a connection")
                    conn = pymysql.connect(host=sql_hostname, user=sql_username,
                            passwd=sql_password, db=sql_main_database,
                            port=tunnel.local_bind_port)

                    print("made connection")
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    query = f"DELETE FROM user WHERE userID = '{self.__userID}';"
                    try:
                        cur.execute(query)
                        result = cur.fetchall()
                        result = pd.DataFrame(result)

                        print('Successfully delete your account. Thank you!')
                        
                    except:
                        print('Failed to delete your account')

                    conn.commit()
                    conn.close
        except:
            print("Failed connection.")
            ## exits the program if unsuccessful
            sys.exit()              

    #def __del__(self): print(f" Your account ({self.__userID}) is logged out. ")


