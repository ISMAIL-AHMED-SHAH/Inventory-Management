from models.product import Product

class Electronics(Product):
    def __init__(self, product_id, name, price, quantity, brand, warranty_years):
        super().__init__(product_id, name, price, quantity)
        self.brand = brand
        self.warranty_years = warranty_years

    def __str__(self):
        return f"[Electronics] {self._name} ({self.brand}) - ${self._price}, Stock: {self._quantity_in_stock}, Warranty: {self.warranty_years} years"
