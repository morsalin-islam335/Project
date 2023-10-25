from datetime import datetime
from datetime import date
# from bank import Bank
# from admin import Admin
from person import Person

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
    

# IBBL = Bank('IBBL', "Dhaka", 'ib')
# user1 = User("A",'a', False)
# user1.crate_acount(IBBL, 'hi')

# user2  = User("B", 'x', False)
# user2.crate_acount(IBBL,'hi')

# print(user2.take_loan(IBBL,5000))
# print(user2.take_loan(IBBL,5000))
# print(user1.take_loan(IBBL,5000))

# admin = Admin("admin", 'ad')
# admin.crate_acount('hi', IBBL)

# print("Total balance of bank is ",admin.check_total_available_balance(IBBL))
# print(user1.transfer_money(500,user2.acount_number, IBBL))

# admin.delete_user(IBBL)

# admin.see_all_users(IBBL)
