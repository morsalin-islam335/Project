from person import Person

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