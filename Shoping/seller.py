class Seller:
    print(
        "can create new account"
        "can add products to sell"

    )


    
    __email_list = []
    def __init__(self) -> None:
        self.profile_name = None
        self.email = None
        self.__password = None
        self.__isSignIn = False
        self.__earning  = 0

    @property
    def earning(self):
        return self.__earning

    def add_earning(self,amount):
        self.__earing += amount
    def cash_out(self,amount):
        if self.earning < amount:
            self.__earning -= amount
    

    @property
    def isSignIn(self):
        return self.__isSignIn
    isSignIn@setattr
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

    def add_product(self,product, quantities,stock):
        if stock.has_product():
            f"{self.profile_name}", stock.add_quantity(product,quantities)
        else:
            pass
        
