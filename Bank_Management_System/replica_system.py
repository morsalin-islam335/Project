from admin import Admin
from bank import Bank
from user import User
from datetime import date
from datetime import datetime

IBBL = Bank("IBBL", "Dhaka", "Info@islamibankbd.com")




def functionality():
    # my_acount = (User("Morsalin", "hi@gmail.com", False))
    # my_acount.crate_acount(IBBL, "hi")
    # print(my_acount.acount_number)


    # print(my_acount.deposit(1000, IBBL))
    # print(my_acount.take_loan(IBBL,10000))
    # # print(my_acount.add_money(1000))
    # # print(my_acount.acount_number)
    # # print(my_acount.available_balance)
    # # print(my_acount.change_password('hello'))


    # admin = Admin("Raja", 'raja@gmail.com')
    # print(admin.acount_number)
    # print(admin.check_total_available_balance)

    # print(admin.see_all_users())




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