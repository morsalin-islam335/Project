class Order:
    def __init__(self,items, customer) -> None:
        self.items = items
        self.customer =  customer
        self.bill = 0
        self.product_list = list(items.keys())
        self.quantities = list(items.values())
        


        for product, quantity in self.items.items():
            self.bill += product.price * quantity

        customer.due_bill += self.bill
        return self
    