from Restaurant import Restaurant
from abc import ABC, abstractclassmethod
from datetime import datetime

class User(ABC):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__()
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        

class Customer(User):
    def __init__(self, name, wallet, email, address, phone) -> None:
        self.wallet = wallet
        super().__init__(name, email, address, phone)
        self.__order = None
        self.due_bill = 0
    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self, order):
        self.__order = order

    def eat_food(self, order):
        print(f"{self.name}eating items of food is/are {order.items2}")
    def place_order(self, order):
        self.order = order # setter
        self.due_bill += order.bill
        print(f"{self.name} placed an order with bill {order.bill}")
    
    def pay_for_order(self, order, restaurant): # eita ekhon o use kori nai. eta restaurant class theka pay receive korba
        if order.bill > self.wallet:
            return f"Sorry. You have not enough money"
        else:
            self.wallet -= order.bill
            self.due_bill -= order.bill
            restaurant.add_order(order)
            return restaurant.receive_payment(order, self)# it use parameter as order and customer


    def tips(self, tips_amount):
        pass
def write_review(self, stars):
    pass


class Employee(User):
    def  __init__(self, name, phone, email, address, starting_date, department, salary) -> None:
        self.starting_date = starting_date
        self.salary = salary
        self.due = salary
        self.department = department
        if datetime.now().date().day == 1:
            self.due = salary
        super().__init__(name, phone, email, address)
    def receive_salary(self):
        self.due = 0

class Chef(Employee):
    def __init__(self, name, phone, email, address, starting_date, department, cocking_item,salary) -> None:
        super().__init__(name, phone, email, address, starting_date, department,salary)
        self.cocking_item = cocking_item


class Server(Employee):
    def __init__(self, name, phone, email, address, starting_date, department, salary) -> None:
        super().__init__(name, phone, email, address, starting_date, department, salary)
        self.__tips_money = 0

    def take_order(self, order):
        pass

    def transfer_order(self, order): # transfer order to the chef
        pass

    def serve(self, order):
        print(f"{self.name} serves {order.items2} to {order.customer.name}")

    def receive_tips(self,customer, money):
        self.__tips_money += money
        customer.wallet -= money


class Manager(Employee):
    def __init__(self, name, phone, email, address, starting_date, department, salary) -> None:
        super().__init__(name, phone, email, address, starting_date, department, salary)
                                
