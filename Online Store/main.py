from product import Product
from shoppingCart import ShoppingCart
from user import User

# Create some product objects
product1 = Product("T-Shirt", "Blue cotton t-shirt", 15.99, 10)
product2 = Product("Jeans", "Slim fit jeans", 29.99, 5)
product3 = Product("Sneakers", "White running sneakers", 59.99, 3)

# Create a shopping cart object
cart = ShoppingCart()

# Create a user object
user = User("John Smith", "123 Main St, City")

# Add products to the shopping cart
cart.add_item(product1, 2)
cart.add_item(product2, 1)
cart.add_item(product3, 1)

# Remove a product from the shopping cart
cart.remove_item(product2)

# Calculate the total amount
total = cart.calculate_total()
print(f"Total amount in the cart: ${total}")

# Checkout the cart
cart.checkout()

# Display user information
print(user)
