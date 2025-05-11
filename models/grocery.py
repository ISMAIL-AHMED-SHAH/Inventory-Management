from models.product import Product
from datetime import datetime

class Grocery(Product):
    def __init__(self, product_id, name, price, quantity, expiry_date):
        super().__init__(product_id, name, price, quantity)
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")

    def is_expired(self):
        return datetime.now() > self.expiry_date

    def __str__(self):
        status = "Expired" if self.is_expired() else "Fresh"
        return f"[Grocery] {self._name} - ${self._price}, Stock: {self._quantity_in_stock}, Expiry: {self.expiry_date.date()} ({status})"
