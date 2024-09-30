from datetime import datetime


class Shop:
    def __init__(self, name: str, location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_total_cost(self, product_cart: dict) -> float:
        total_cost = 0
        for product, quantity in product_cart.items():
            if product in self.products:
                price = self.products[product]
                total_cost += price * quantity
        return total_cost

    def print_receipt(self, customer_name: str, product_cart: dict,
                      current_time: datetime) -> None:
        print(f'\nDate: {current_time.strftime("%d/%m/%Y %H:%M:%S")}')
        print(f"Thanks, {customer_name}, for your purchase!")
        total_cost = self.calculate_total_cost(product_cart)
        for product, quantity in product_cart.items():
            if product in self.products:
                price = self.products[product]
                total_price = price * quantity
                print(f"{quantity} {product}(s) for {total_price} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
