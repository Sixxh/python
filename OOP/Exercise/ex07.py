class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_total_price(self):
        return self.price * self.quantity

class DiscountedProduct(Product):
    def __init__(self, name, price, quantity, discount):
        super().__init__(name, price, quantity)
        self.discount = discount

    def get_total_price(self):
        return (self.price * self.quantity) - (self.price * self.quantity * self.discount)
    
# Programa Principal

product = Product('Laptop', 1000,  2)
print(product.get_total_price())

discounted_product = DiscountedProduct('Laptop', 1000, 2, 0.1)
print(discounted_product.get_total_price())