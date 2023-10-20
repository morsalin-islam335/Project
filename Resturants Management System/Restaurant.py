class Restaurant:
    def __init__(self, name,rent, investment, menu = []) -> None:
        self.name = name
        self.chef = None
        self.server = None
        self.manager = None
        self.menu = menu
        self.revenue = 0 # Total selling price with deducting expense
        self.balance = investment  # Total available balance
        self.expense = 0
        self.profit = 0
        self.rent = rent

        self.orders = []
    def add_order(self, order):
        self.orders.append(order)

    def Add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee
        elif employee_type == 'manager':
            self.manager = employee
    
    def receive_payment(self,order, customer):    
        self.revenue += order.bill
        self.balance += order.bill
        return customer.wallet - order.bill # it will return extra money

    def pay_expense(self, amount, description):
        if amount <= self.balance:
            self.balance -= amount
            self.expense += amount
            return f"Expense {amount} for {description}"
        else:
            return f"Not enough money to pay {amount}"
    
    def pay_salary(self, employee):
        if self.balance >= employee.salary:
            employee.receive_salary()
    
    def show_employee(self):
        print(f"__________________SHOWING EMPLOYEES_______________")

        if self.chef is not None:
            print(f"chef : {self.chef.name} with salary {self.chef.salary}")
        
        if self.server is not None:
            print(f"Server {self.server.name} with salary {self.server.salary}")
        