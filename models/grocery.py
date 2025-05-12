from models.product import Product
from datetime import datetime

class Grocery(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.expiry_date = expiry_date

    def to_dict(self):
        return {
            "__type__": "Grocery",
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity_in_stock": self.quantity,
            "expiry_date": self.expiry_date
        }

    def __str__(self):
        return f"Grocery(ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Expiry Date: {self.expiry_date})"
