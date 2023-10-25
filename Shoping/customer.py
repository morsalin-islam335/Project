from order import Order
from stock import Stock
class Customer:
    __email_list = []
    def __init__(self) -> None:
        self.profile_name = None
        self.email = None
        self.__password = None
        self.__isSignIn = False
        self.__balance = None
        self.due_bill = 0
        self.buying_list = []


    def add_balance(self,amount):
        self.__balance += amount


    @property
    def balance(self):
        return self.__balance
    
    @property
    def isSignIn(self):
        return self.__isSignIn
    @isSignIn.setter

    def isSignIn(self, bool_value):
        self.isSignIn = bool_value
        
    def sign_up(self,name,email,password):
        if email not in self.__email_list:
            self.profile_name = name
            self.email = email
            self.__email_list.append(email)
            self.__password = password
            return f"congratulations. You successfully create a new account"
        else:
            return f"this email already exist. Try with another account"

    
    def sign_in(self,email,password):
        if email in self.__email_list:
            if self.email == email and self.__password == password:
                self.isSignIn = True
                print("Log in successfully")
            else:
                print("Your password is wrong. Try with correct password")
        else:
            print("There is no account with this email")
    
    def see_product(self,stock):
        stock.show_product()

    def place_order(self,stock, product_with_quantities):
        product_list = list(product_with_quantities.keys())
        product_quantities = list(product_with_quantities.values())

        for i in range(len(product_list)):
            if stock.has_product(product_list[i] == False):
                return f"Products does not exist on stock"

        flag = True
        for i in range(len(product_list)):
            if product_list[i].quantity < product_quantities[i]:
                flag = False
                break
        if flag == False or len(product_list) == 0:
            return f"Insufficient product in this stock"
        else:
            my_order = Order(product_with_quantities, self)
            print(f"{self.profile_name} give an order successfully")

    def buy_product(self,stock, order):
