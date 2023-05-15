class Product:
    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Name: {self.name} | Price: ${self.price} | Stock: {self.stock}"

    def update_stock(self, quantity):
        self.stock += quantity

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            print("Insufficient stock.")
            return False
