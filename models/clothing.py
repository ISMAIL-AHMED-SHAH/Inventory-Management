from models.product import Product

class Clothing(Product):
    def __init__(self, product_id, name, price, quantity, size, material):
        super().__init__(product_id, name, price, quantity)
        self.size = size
        self.material = material

    def __str__(self):
        return f"[Clothing] {self._name} - ${self._price}, Size: {self.size}, Material: {self.material}, Stock: {self._quantity_in_stock}"
