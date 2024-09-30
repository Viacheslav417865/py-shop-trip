import os
import json
from app.customer import Customer
from app.shop import Shop
import datetime


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer(**customer_data)
                 for customer_data in config["customers"]]
    shops = [Shop(**shop_data) for shop_data in config["shops"]]

    for customer in customers:
        print(f"\n{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        cheapest_cost = float("inf")

        for shop in shops:
            try:
                trip_cost = customer.calculate_trip_cost(shop, fuel_price)
                print(f"{customer.name}'s trip to {shop.name}"
                      f" costs {trip_cost}")
                if trip_cost < cheapest_cost:
                    cheapest_cost = trip_cost
                    cheapest_shop = shop
            except ValueError as e:
                print(e)

        if cheapest_shop:
            customer.make_purchase(cheapest_shop,
                                   fuel_price,
                                   datetime.datetime(2021, 1, 4, 12, 33, 41))
