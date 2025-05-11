from models.product import Product
from models.grocery import Grocery
from models.electronics import Electronics
from models.clothing import Clothing
import json
import os

class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product.product_id in self._products:
            raise ValueError("Product ID already exists.")
        self._products[product.product_id] = product

    def remove_product(self, product_id):
        self._products.pop(product_id, None)

    def search_by_name(self, name):
        return [p for p in self._products.values() if name.lower() in p.name.lower()]

    def search_by_type(self, product_type):
        return [p for p in self._products.values() if p.type == product_type]

    def list_all_products(self):
        return list(self._products.values())

    def sell_product(self, product_id, quantity):
        if product_id not in self._products:
            raise ValueError("Product not found.")
        self._products[product_id].sell(quantity)

    def restock_product(self, product_id, quantity):
        if product_id not in self._products:
            raise ValueError("Product not found.")
        self._products[product_id].restock(quantity)

    def total_inventory_value(self):
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        expired = [
            pid for pid, prod in self._products.items()
            if isinstance(prod, Grocery) and prod.is_expired()
        ]
        for pid in expired:
            self.remove_product(pid)

    def save_to_file(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        data = [p.to_dict() for p in self._products.values()]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            return

        self._products = {}
        with open(filename, 'r') as f:
            data = json.load(f)
            for item in data:
                ptype = item.pop("__type__")
                cls_map = {
                    "Electronics": Electronics,
                    "Grocery": Grocery,
                    "Clothing": Clothing
                }
                cls = cls_map.get(ptype)
                if cls:
                    product = cls(**item)
                    self.add_product(product)
