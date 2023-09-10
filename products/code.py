class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

class Order:
    order_count = 0

    def __init__(self, customer_name, cart):
        Order.order_count += 1
        self.order_id = Order.order_count
        self.customer_name = customer_name
        self.cart = cart

    def process_order(self):
        print(f"Processing order #{self.order_id} for {self.customer_name}")
        print("Items in the order:")
        for item in self.cart.items:
            print(f"{item['product'].name}: {item['quantity']} @ ${item['product'].price}")
        print(f"Total amount: ${self.cart.calculate_total()}")

# Example usage:
if __name__ == "__main__":
    # Create some products
    product1 = Product(1, "Laptop", 800)
    product2 = Product(2, "Mouse", 20)
    product3 = Product(3, "Keyboard", 50)

    # Create a shopping cart
    cart = ShoppingCart()
    cart.add_item(product1, 2)
    cart.add_item(product2, 3)
    cart.add_item(product3, 1)

    # Create an order
    order = Order("John Doe", cart)

    # Process the order
    order.process_order()

