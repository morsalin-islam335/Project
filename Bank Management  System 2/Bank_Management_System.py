# Project name: Bank Management System


from datetime import date
from datetime import datetime
import random

#______________________parent class of user and admin____________________
class Person:
    def __init__(self, name,email):
        self.name = name
        self.email = email = email

#_________________admin class___________________ 
class Admin(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__acount_number = None
        self.__password = None

    def crate_acount(self, password, bank):
        return bank.create_admin_acount(self,password)
    
    def match_password(self, password): # This will be check if input password and admin password is same or not
        return self.__password == password
    
    @property
    def acount_number(self): # This will be return admin acount number as read only value
        return self.__acount_number

    def set_acount_number(self, number): # This will be set admin acount number
        self.__acount_number = number

    def change_password(self, password): # This will be change admin password. This function will work when an admin create acount and this function will be call automatically
        self.__password = password
    
    def declare_bankrupt(self, bank):#Admin can declare bankrupt. This method will be work like this
        bank.bankrupt(self)
    
    def delete_user_acount(self):  #  This method will be delete user who have lowest money
        pass #TODO delete user acount who's balance is lowest
    def see_all_users(self): # This method will be present all users information
        pass #TODO see all users

    def check_total_available_balance(self, bank): # Admin will be able to check bank total balance
        return bank.total_balance # check total_balance

    def total_loan_amount(self, bank):  # admin will be able to see total_loan_amount
        return bank.total_loan() #  check total loan amount

    def delete_user(self,bank):
        bank.delete_user()

    def change_loan_feature(self, bank, change_with): # Admin can change loan feature
        bank.change_loan_feature(self, change_with)
    
    def see_all_users(self, bank):
        bank.show_all_users()

#_____________________User Class _________________

class User(Person):
    def __init__(self, name, email, acount_type):
        super().__init__(name, email)

        self.__acount_number = None        
        self.isSaving = acount_type
        self.__balance = 0
        self.loan_limit = 0
        self.__transaction_history = []
        self.__password = None
    
    def set_acount_number(self, number): #  This method will be set acount number form bank while creating it's acount
        self.__acount_number = number
    def match_password(self, password):# match password if password is correct or not
        return self.__password == password

    def change_password(self, password): # This will be change password
        self.__password = password
    
    def crate_acount(self, bank,password):# This method will be create a user acount with valid information
        return bank.create_acount(self, password)
    
    @property
    def acount_number(self):  # acount number won't be change without user want to change it
        return self.__acount_number

    def add_money(self, amount): # if user receive money form another user transaction history will be add in bank class
        self.__balance += amount
        self.__transaction_history.append((f"cash-in {amount}TK date: {datetime.now().date()} at {datetime.now().hour} {datetime.now().time().minute}")) # list of tuple of transaction history

    def deposit(self, amount, bank):# By calling this method user can add deposit
        bank.add_balance(amount)
        self.__balance += amount
        self.__transaction_history.append((f"cash-in {amount}TK date: {datetime.now().date()} at {datetime.now().hour} {datetime.now().time().minute}"))
        return f"receive {amount} Tk Total Balance is {self.__balance}"

    
    def withdraw(self, amount, bank):# User can withdraw
        if amount > self.__balance:
            return f"Withdrawal Exceeded"
        elif bank.isBankrupt:
            return f"The bank is bankrupt"
        
        elif amount <100:
            return f"You can't withdraw less than 100 taka"
        elif bank.has_money(amount) != True:
            return f"Bank has not {amount} money right now"
        else:
            self.__balance -= amount
            bank.deduct_balance(amount)
            self.__transaction_history.append((f"cash out {amount}TK date: {datetime.now().date()} at {datetime.now().hour} {datetime.now().minute}")) # list of tuple of transaction history
            return f"{amount} taka withdraw successfully"

    def view_transaction_history(self): #User will be able to see his transaction history
        for transaction in self.__transaction_history:
            print(transaction)

    @property
    def available_balance(self): # User can see his balance but not change
        return self.__balance
    
    def take_loan(self,bank, amount): # user will be able to take loan at most 2 times
        if bank.loan_feature and self.loan_limit <2  and bank.has_money(amount) and amount >= 5000 and amount <= 100000:  # loan limit 5000-> 100000
            self.loan_limit += 1
            self.__balance += amount
            bank.deduct_balance(amount)
            bank.add_loan(amount)
            self.__transaction_history.append((f"take loan {amount}TK date: {datetime.now().date()} at {datetime.now().hour} {datetime.now().minute}"))
            return f"{amount} has been added to your acount and your current balance is {self.__balance}"
        else:
            return f"You are not capable for loan"

    def transfer_money(self, amount, sender_acount_number, bank):# This will be sent money to another acount with existence of sender acount number and user have more balance
        if(bank.isBankrupt):
            return f"Bank is bankrupt"
        if bank.isUser2(sender_acount_number) and self.__balance >= amount:
            self.__balance -= amount
            bank.deduct_balance(amount)
            bank.sent_money(sender_acount_number, amount)
            self.__transaction_history.append((f"{amount}TK sent  date: {datetime.now().date()} at {datetime.now().hour} {datetime.now().minute}"))
            return f"You successfully sent {amount} money. Now your current balance is {self.__balance}"
        else:
            return f"acount does not exist"

    @property
    def show_balance(self): # user can show his balance
        return self.__balance
    
    def __repr__(self) -> str:
        print(f"user name : {self.name}, user email {self.email}, balance {self.show_balance}")
        return ""



#_____________Bank class_______________


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

             



################ creating replica system  ####################
def functionality():
    IBBL = Bank("IBBL","Dhaka","info@islamibankbd.com")

    while(True):
        print("""log in or sign-up:
            \tpress 1 for log in
            \tpress 2 for sign-up
            \tpress 3 for EXIT""")
        option = int(input("Option :")) #Log in  sing -up or EXIT OPTION
        if option == 1: #Log in
            print("""Log in as User press 1 \nLog in as admin press 2""")
            option = int(input("Enter  Option :"))
            print() # for beauty
            if option == 1: # Log-in as user
                acount = input("Enter your acount number :")
                password = input("Enter your acount password :")
                if IBBL.isUser(acount,password):
                    print() # for beauty
                    user = IBBL.return_user_acount(acount) # if User acount number and password is correct  that will be return that user object
                    while(True):

                        print(f"_______________Log In as {user.name}___________")
                        print("""\tpress 1 for deposit\n\tpress 2 for withdraw\n\tpress 3 for check available balance\n\tpress 4 for show transaction history\n\tpress 5 for take loan\n\tpress 6 for transfer money\n\tpress 7 for sign-up""")
                        option = int(input("Enter option :"))
                        if option == 1: # deposit money
                            amount = int(input("how much money do you wanna deposit :"))
                            print(user.deposit(amount, IBBL)) 
                            print()#for beauty

                        elif  option == 2: # withdraw money
                            amount = int(input("How much money do you wanna withdraw : "))
                            print(user.withdraw(amount, IBBL),"\n")

                        elif option == 3:  # check available balance
                            print("Your Available balance is ",user.available_balance ,"\n") 

                        elif option == 4: # show transaction history
                            user.view_transaction_history() 
                            print() # for beauty

                        elif option == 5: # take loan from bank
                            amount = int(input("How much money do you want as loan? : "))
                            print(user.take_loan(IBBL, amount))
                            print() # for beauty

                        elif option == 6: # transfer money to another user
                            sender_ID = input("Enter sender acount number : ") 
                            amount = int(input("How much ? : "))
                            print(user.transfer_money(amount, sender_ID, IBBL),'\n')

                        elif option == 7: #  terminate inner loop
                            print()
                            break
                        else:
                            print("Please select correct option with integer value \n")
                else:
                    print("Your acount number or password is not correct\n")
                        
            elif option == 2: # log in as admin
                acount = input("Enter your acount number : ")
                password = input("Enter your password :")
                
                if IBBL.isAdmin(acount, password):
                    admin = IBBL.return_admin_acount(acount)
                    print() # for beauty
                        
                    while(True):
                        print(f"__________Log in as {admin.name}________")
                        print("\tpress 1 for delete user acount\n\tpress 2 for see all users acount list\n\tpress 3 for check total_available_balance\n\tpress 4 for check total_loan_amount\n\tpress 5 for change_loan_feature\n\tpress 6 for Log OUt")
                        option = int(input("Enter Option : "))
                        if option == 1:
                            admin.delete_user(IBBL) # delete user acount with lowest money
                            print() # for beauty
                            
                        elif option == 2:
                            admin.see_all_users(IBBL)  # see all users acount
                            print() # for beauty

                        elif option == 3: #check bank all balance
                            print("Total taka in bank is", admin.check_total_available_balance(IBBL)) # print total_taka in bank
                            print() # for beauty

                        elif option == 4:
                            print("Total loan of all users is ", admin.total_loan_amount(IBBL)) # check total loan balance
                            print() # for beauty
                        elif option == 5: # change loan feature
                            changing_with = int(input("Press 1 for stop or press 2 for continue loan feature : "))
                            if not(changing_with == 1 or changing_with ==2):
                                print("Invalid input\n")
                            else:
                                admin.change_loan_feature(IBBL, bool(changing_with-1)) # change loan feature
                                print() # for beauty

                        elif option == 6:
                            print() # for beauty
                            break
                        else:
                            print("Please select correct option with integer value\n")
                else:
                    print("Your acount or password is not correct. Try again\n")

        elif option == 2: # Sign-Up
            print("press 1 for sign-up as user\npress 2 for sign-up as admin")
            option = int(input("Enter Option :"))
            if option == 1: # Sign-up as user
                name = input("Enter your name :")
                email = input("Enter your email :")
                print("Select Acount Type")
                print("press 1 for current \npress 2 for saving")
                select = (int(input("Enter option :")))
                if not(select == 1 or select == 2):
                    print("Wrong Selection")
                    print("") # new line will print for beauty

                else:
                    password = input("Input a strong password including character letter(Upper case and lower case) and number :")

                    user = User(name,email,bool(select-1))
                    print(user.crate_acount(IBBL, password))
                    print() # for beauty

            elif option == 2: # Sign-up as admin
                name = input("Enter your name :")
                email = input("Enter your email :")
                admin = Admin(name,email)
                password =input("Enter a strong password :")

                print(admin.crate_acount(password,IBBL))
                print()

            else:
                print("Invalid input\n")



        elif option == 3: # program will be terminate
            break
        else: # Invalid input
            print("Please select correct option\n")





# Calling Main Function
def main():
    functionality()
    
if __name__ == "__main__":
    # Note that to use proper use you need to copy and paste acount number from automatically generated program
    main()