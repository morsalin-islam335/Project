# Project name: Restaurant Management System
from Restaurant import Restaurant
from Menu import Pizza, Burger, Drinks, Menu
from Users import Manager, Server, Customer, Chef
from order import Order

def main():
    
    menu = Menu()

    #add Pizza to menu
    pizza_1 = Pizza("Shukti Pizza", 500, "Large", ["Shutki", 'Onion'])
    menu.add_item('Pizza', pizza_1)

    pizza_2 = Pizza("Alu Pizza", 300, 'Large', ['Alu', 'Onion', 'oil'])
    menu.add_item('Pizza', pizza_2)

    pizza_3 = Pizza("Dal Pizza", 550, 'Large', ['Dal', 'Oil'])
    menu.add_item("Pizza", pizza_3)

    # Add burger to menu
    burger_1 = Burger("Naga Burger", 1000,'chicken', ['bread', 'chill'])
    menu.add_item("Burger", burger_1)

    burger_2 = Burger("Beef Burger", 1100, 'Beef', ['met', 'bone'])
    menu.add_item("Burger", burger_2)

    # Add drinks to menu

    coke = Drinks("Coke", 80, True)
    menu.add_item("Drinks", coke)

    mocha = Drinks("Mocha", 100, False)
    menu.add_item("Drinks", mocha)

    # show menu
    menu.show_menu()

    # add manager
    restaurant = Restaurant("Mayer Dowa Restaurant", 10000, 1000000, menu)
    manager  = Manager("Monowar Hossen",1314,'manage@gmail.com', "Dimla, NIlphamari", "25-12-2018","Core", 2000)
    restaurant.Add_employee("manager", manager)

    # add chef

    chef = Chef("Ab: Lotif", 1454,"ablotif@gmail.com", 'Dimla, Nilphamary',"25-12-2019", 'Chef',['Meat', "Burger", "Pizza"], 1200)
    restaurant.Add_employee("chef", chef)

    # add server

    server = Server("Babu", 157, "neajay@gmail.com", "Nilphamary",'15-10-2022','server',400)
    restaurant.Add_employee('server', server)
    restaurant.show_employee()

    customer_1 = Customer("Rakib", 10000, 'rakib@gmail.com','jeshore', 188955)
    # restaurant.
    order_1 = Order(customer_1, [pizza_3, burger_2, mocha])
    customer_1.place_order(order_1)
    customer_1.eat_food(order_1)


    print( f"customer due bill is :",customer_1.due_bill)
    print(customer_1.pay_for_order(order_1,restaurant)) # if customer have enough money it will return extra money
    print(f"after paying for an order due bill is: ", customer_1.due_bill)
    print("after  paying cutomer wallet is : ",customer_1.wallet)
    print(f"rstaurant revenue is : ",restaurant.revenue)
    print(f"restaurant balance is :", restaurant.balance)

    
    





if __name__ == "__main__":
    main()