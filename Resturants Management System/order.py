class Order:
    def __init__(self, customer, items) -> None:
        self.customer = customer
        self.items = items
        self.items2 = []
        total = 0

        for item in items:
            total += item.price
            self.items2.append(item.name)
        self.bill = total

        
        
