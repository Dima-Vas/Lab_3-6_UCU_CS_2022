
class Item():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class Location():
    def __init__(self, city, postoffice) -> None:
        self.city = city
        self.postoffice = postoffice

class Vehicle():
    def __init__(self, vehicleNo, isAvailable) -> None:
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


class Order():
    def __init__(self, user_name, orderId, location, items, vehicle) -> None:
        self.orderId = orderId
        self.user_name = user_name
        self.location = location
        self.items = items
        self.vehicle = vehicle