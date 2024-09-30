import math
from app.car import Car
from app.shop import Shop
import datetime


class Customer:
    def __init__(self, name: str, product_cart: dict, location: list,
                 money: float, car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance_to_shop = self.calculate_distance(shop.location)
        fuel_cost_to_shop = (
            self.car.calculate_fuel_cost(distance_to_shop, fuel_price))
        fuel_cost_return = (
            self.car.calculate_fuel_cost(distance_to_shop, fuel_price))
        product_cost = shop.calculate_total_cost(self.product_cart)
        return round(fuel_cost_to_shop + product_cost + fuel_cost_return, 2)

    def calculate_distance(self, shop_location: list) -> float:
        return math.sqrt((self.location[0] - shop_location[0])
                         ** 2 + (self.location[1] - shop_location[1]) ** 2)

    def make_purchase(self, shop: Shop, fuel_price: float,
                      current_time: datetime) -> None:
        trip_cost = self.calculate_trip_cost(shop, fuel_price)
        if trip_cost > self.money:
            print(f"{self.name} "
                  f"doesn't have enough money to make a purchase at "
                  f"{shop.name}")
        else:
            print(f"{self.name} rides to {shop.name}")
            shop.print_receipt(self.name, self.product_cart, current_time)
            self.location = shop.location
            self.money -= trip_cost
            print(f"{self.name} rides home")
            self.location = [0, 0]
            print(f"{self.name} now has {round(self.money, 2)} dollars")
