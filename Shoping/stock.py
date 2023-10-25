
class Stock:
  
    def __init__(self,name) -> None:
        self.name = name
        self.__price = 0
        self.__profit = 0
        self.__product_list = []
    
    def has_product(self, product):
        if product in self.__product_list:
            return True
        else :
            return False

    def add_product(self, product, quantity):
        self.__price += product.price * quantity
        product.add_quantity(quantity)
        self.__product_list.append(product)
        return f"Successfully added {quantity} item in {product.name}"

    def add_quantity(self, product, quantity):
        self.__price += product.price * quantity
        product.add_quantity(quantity)
        return f"Successfully added {quantity} items in {product.name}"



    def buy_product(self, product,quantity, customer):
        if product not in self.__product_list:
            return f"This items does not exist in stock"
        elif product.quantity < quantity:
            return f"You can buy maximum {product.quantity} piece of this product"
        else:
            product.quantity -= quantity
            customer.buying_list.append([product,quantity])

    def sell_product(self,order):
        for i in range(len(order.product_list)):
            order.product_list[i].quantity -= order.quantities
            if order.product_list[i].quantities == 0:
                self.__product_list.remove(order.product_list[i])

    def show_product(self):
        for item in self.__product_list:
            print(f"item name : {item.name} : stock : {item.quantity}")