class User:
    def __init__(self, userid, username, pswd, email, phone, shipping, credit_num, billing):
        self.userid = userid
        self.username = username
        self.pswd = pswd
        self.email = email
        self.phone = phone
        self.shipping = shipping
        self.credit_num = credit_num
        self.billing = billing

    def get_userid(self):
        return self.userid

    def get_username(self):
        return self.username



class Books:
    def __init__(self, itemID, name, price, inventory):
        self.itemID = itemID
        self.name = name
        self.price = price
        self.inventory = inventory

class Shirts:
    def __init__(self, shirtID, color, price, inventory):
        self.itemID = shirtID
        self.color = color
        self.price = price
        self.inventory = inventory