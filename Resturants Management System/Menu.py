class Food:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.cooking_time = 15

class Burger(Food):
    def  __init__(self, name, price, meat , ingredients) -> None: # ingredients means extra materials
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredients

class Pizza(Food):
    def __init__(self, name, price, size,ingredients) -> None:
        super().__init__(name, price)
        self.ingredients = ingredients
        self.size = size


class Drinks(Food):
    def __init__(self, name, price, isCold = True) -> None:
        super().__init__(name, price)
        self.isCold = isCold


class Menu:  # has a relation  or like composition
    def __init__(self) -> None:
        self.Pizza = []      
        self.Burger = []
        self.Drinks = []

    def add_item(self, item_type, item):
        if(item_type == "Pizza"):
            self.Pizza.append(item)
        elif(item_type == "Burger"):
            self.Burger.append(item)
        elif(item_type == 'Drinks'):
            self.Drinks.append(item)
    
    def remove_item(self, item_type, item):
        if item_type == "Pizza":
            if item in self.Pizza:
                self.Pizza.remove(item)
        elif item_type == "Burger":
            if item in self.Burger:
                self.Burger.remove(item)
        elif item_type == "Drinks":
            if item in Drinks:
                self.Drinks.remove(item)
    
    def show_menu(self):
        for pizza in self.Pizza:
            print(f"Name : {pizza.name}   price : {pizza.price}")
        
        for drink in self.Drinks:
            print(f"Name : {drink.name}  Price : {drink.price}")
        
        for burger in self.Burger:
            print(f"Name : {burger.name} price : {burger.price}")