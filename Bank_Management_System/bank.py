import random

class Bank:
    def __init__(self, name, address, email) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.__users = {} # key is user acount number and value is acount user object
        self.__admins = {} # key is admin acount number and value is admin objects
        self.bankrupt = True
        self.__total_balance = 10000000
        self.__isBankrupt = False
        self.__loan_feature  = True
        self.__users_email = []
        self.__admins_email = []
        self.__loan_balance = 0
    
    def create_acount(self, user,password):  #  This will create a user acount with valid information
        if user.email in self.__users_email:
            return f"This email is already in use"
        elif user.acount_number is  None:
            acount_number= f"{user.name[0:2]}-{random.randint(1,1000)}{random.randint(1,1000)}-{int(user.isSaving)}"
            user.set_acount_number(acount_number)
            self.__users[user.acount_number] = user
            user.change_password(password)
            self.__users_email.append(user.email)
            return f"""Congratulations! Now you're a new member of {self.name} bank
            Your acount number is : {acount_number}"""
        
        else:
            return f"You already have  an acount"
    
    def create_admin_acount(self, admin, password): #  This will create an admin acount with valid information
        if admin.email in self.__admins_email:
            return f"This email already in use"
        elif admin.acount_number is None:
            acount_number = f"{admin.name[0:2]}-{random.randint(1,1000)}{random.randint(1,1000)}-AD"
            admin.set_acount_number(acount_number)
            self.__admins[admin.acount_number] = admin
            admin.change_password(password)
            return f"""Congratulations! You're a now admin of this bank
            your acount number is : {acount_number}"""
        else:
            return f"This acount is already exist"
    @property
    def isBankrupt(self):
        return self.__isBankrupt
       

    @property
    def isBankrupt(self): # This will be return if bank is bankrupt or not
        return self.__isBankrupt
    
    
    def isUser(self, acount_number, password): # This will be check if a person is a user of bank or not with his acount number or not
        return acount_number in self.__users and self.__users[acount_number].match_password(password)
    
    def isUser2(self, acount_number): #That is for transfer money. if a user want to send money to another user acount he won't need sender password
        return acount_number in self.__users

    # if isUser method return true than in replica system there need to return user object
    def return_user_acount(self, acount_number):
        return self.__users[acount_number]
    
    def isAdmin(self, acount_number,password): # This will return if a person admin or not
        return acount_number in self.__admins and self.__admins[acount_number].match_password(password)
    
    def return_admin_acount(self, acount_number): # this will return admin object
        return self.__admins[acount_number]

    def sent_money(self, sender_acount, amount):  # This will be add money to sender acount        
        self.__users[sender_acount].add_money(amount)
    
    
    def add_balance(self, amount): # This will be bank total_balance
        if amount > 100: # user can add minimum 100 taka as deposit
            self.__total_balance += amount
            if self.__isBankrupt != False:
                self.__isBankrupt = False
    def has_money(self, money): # This will be check if bank has more than or equal to money or not
        if money <= self.__total_balance:
            return True
        else:
            return False
        

    def deduct_balance(self, amount): # This will be deduct balance from bank total_balance
        self.__total_balance -= amount
        if self.__total_balance < 100:
            self.__isBankrupt = True
        
    @property
    def loan_feature(self): # This will be return if loan feature is on or off
        return self.__loan_feature
    
    def change_loan_feature(self, admin,changing_with): #  This will change loan feature
        if admin.acount_number is not None:
            self.__loan_feature = changing_with
        else:
            print(f"You have to create acount first")
    def add_loan(self,amount): # This will be increase loan money
        self.__loan_balance += amount
    
    def show_loan_balance(self, admin): # This method will be show bank total loan balance
        if admin.acount_number in self.__admins:
            print(f"Bank total loan is {self.__loan_balance}")
        else:
            print("Information is not correct")
    
    def show_all_users(self):
        for user in self.__users.values():
            print(user) # here will be print User class representation
    @property
    def total_balance(self): # return total balance of bank
        return self.__total_balance
    def total_loan(self): # Total loan balance
        return self.__loan_balance
    
    def delete_user(self): # delete user who have  lowest balance
        if len(self.__users) == 0:
            print("There is no user")
        elif len(self.__users) == 1:
            self.__users.clear()
            print("1 acount  deleted successfully")
        else:
            user_acount_with_min_balance = None
            min = 1e9
            for user in self.__users.values():
                if user.available_balance < min:
                    min = user.available_balance
                    user_acount_with_min_balance = user.acount_number
            
            self.__users.pop(user_acount_with_min_balance)
            print("1 acount deleted successfully")

             
