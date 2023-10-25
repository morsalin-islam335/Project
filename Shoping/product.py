class Product:
    # print(
    #     "product will have name , price and this will be parent class"

    # )
    def __init__(self,name, price) -> None:
        self.name = name
        self.price = price
        self.__quantity = 0
    
    @property
    def quantity(self):
        return self.__quantity

    def add_quantity(self, quantity):
        self.__quantity += quantity
    


class Pant(Product):
    def __init__(self, name, price,size, color,brand) -> None:
        self.size = size
        self.color = color
        self.brand = brand
        super().__init__(name, price)
    
class Shirt(Product):
    def __init__(self, name, price ,size, color,  brand) -> None:
        self.brand = brand
        self.color = color
        self.size  = size
        self.quantity = None
        super().__init__(name, price)

class Sari(Product):
    def __init__(self, name, price,color ,brand) -> None:
        self.color = color
        self.brand  = brand
        super().__init__(name, price)


class Pazama(Product):
    def __init__(self, name, price,size, color, brand) -> None:
        self.size = size
        self.color = color
        self.brand = brand
        super().__init__(name, price,quantity)