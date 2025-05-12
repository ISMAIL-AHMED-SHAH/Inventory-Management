from models.product import Product

class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.size = size
        self.material = material

    def to_dict(self):
        return {
            "__type__": "Clothing",
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "size": self.size,
            "material": self.material
        }

    def __str__(self):
        return f"Clothing(ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Size: {self.size}, Material: {self.material})"
