"""
A simple logistics system.
"""
from numpy import random

class Item():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class Vehicle():
    def __init__(self, vehicleNo, isAvailable = True) -> None:
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


class City():
    def __init__(self, city, postoffice) -> None:
        self.city = city
        self.postoffice = postoffice

class Order():
    def __init__(self, user_name, city, postoffice, items) -> None:
        self.user_name = user_name
        self.city = city
        self.postoffice = postoffice
        self.items = items
        self.id = str(random.randint(10000000, 99999999))
        print(f"Your order id is {self.id}")

class LogisticsSystem():
    def __init__(self, vehicles) -> None:
        self.vehicles = vehicles
        self.orders = []

    def placeOrder(self, order):
        available_vehicles = [x for x in self.vehicles if x.isAvailable == True]
        if len(available_vehicles) > 0 :
            for i in self.vehicles:
                if i.isAvailable == False:
                    pass
                else :
                    i.isAvailable = False
                    self.orders.append(order)
                    break
        else :
            print(">There is no available vehicle to deliver an order.")

    def trackOrder(self, orderNo):
        if orderNo in [x.id for x in self.orders]:
            orderIndex = self.orders.index([x for x in self.orders if x.id == orderNo][0])
            order_refered = self.orders[orderIndex]
            print(f"Your order #{orderNo} is sent to {order_refered.city}. " + \
            f"Total price: {sum([x.price for x in order_refered.items])} UAH.")
        else :
            print("No such order.")


"""
A simple interactive panel to work with. 
To test classes with your own code comment all the lines below and paste your code.
"""
name = input("Type your name please :\n>>> ")
logSystem = LogisticsSystem([Vehicle(1), Vehicle(2)])
while True :
    def note_order():
        output = []
        while True :
            to_do = input("Type 0 if you want to end your order, otherwise type \
your good`s name and price in the next format :\n\
Sofa 5800\n>>> ")
            if to_do !="0":
                try :
                    int(to_do.split(" ")[1])
                    output.append(to_do.split(" "))
                except (ValueError and IndexError):
                    print("Type the proper price (use numbers)")
                    pass
                print(f"Your order is next: {output}")
            else :
                print(f"Your final order: {output}")
                break
        return output

    action = input("Type what action you want to do. Type 0 for placing an \
order and 1 for tracking an order. Type any other button to leave.:\n>>> ")
    if action == "0":
        my_items = note_order()
        city = input("Type the city the goods to be delivered:\n>>> ")
        post_num = input("Type the post office number the goods to be delivered:\n>>> ")
        items_to_write = []
        for i in my_items:
            items_to_write.append(Item(i[0], int(i[1])))
        logSystem.placeOrder(Order(name, city, post_num, items_to_write))
    elif action == "1":
        logSystem.trackOrder(input("Type the id of the order to be found:\n>>> "))
    else :
        print("Thank you for choosing our service.")
        break
