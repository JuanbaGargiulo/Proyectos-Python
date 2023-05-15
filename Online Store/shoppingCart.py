
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))
        print(f"Added {quantity} {product.name}(s) to the cart.")

    def remove_item(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                print(f"Removed {product.name} from the cart.")
                return
        print(f"{product.name} is not in the cart.")

    def calculate_total(self):
        total = 0
        for item in self.items:
            product, quantity = item
            total += product.price * quantity
        return total

    def checkout(self):
        total = self.calculate_total()
        if total > 0:
            print(f"Total amount to pay: ${total}")
            self.clear_cart()
        else:
            print("Your cart is empty.")

    def clear_cart(self):
        self.items = []
        print("Cart cleared.")
