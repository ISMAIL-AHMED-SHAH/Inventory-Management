from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, quantity_in_stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    def restock(self, amount):
        if amount > 0:
            self._quantity_in_stock += amount
        else:
            raise ValueError("Restock amount must be positive.")

    def sell(self, quantity):
        if quantity <= self._quantity_in_stock:
            self._quantity_in_stock -= quantity
        else:
            raise ValueError("Not enough stock to complete the sale.")

    def get_total_value(self):
        return self._price * self._quantity_in_stock

    @abstractmethod
    def __str__(self):
        pass

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity_in_stock

    @property
    def type(self):
        return self.__class__.__name__
