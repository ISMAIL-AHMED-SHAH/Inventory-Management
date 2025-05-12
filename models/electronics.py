from models.product import Product

class Electronics(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, brand, warranty):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.brand = brand
        self.warranty = warranty

    def to_dict(self):
        return {
            "__type__": "Electronics",
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "brand": self.brand,
            "warranty": self.warranty
        }

    def __str__(self):
        return f"Electronics(ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Brand: {self.brand}, Warranty: {self.warranty} years)"
