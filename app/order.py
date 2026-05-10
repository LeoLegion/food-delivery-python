import json
import uuid
from datetime import datetime

MENU_FILE = "data/menu.json"
ORDERS_FILE = "data/orders.json"

class Order:

    def __init__(self):
        self.cart = []
        self.total = 0
    
    def load_menu(self):

        with open(MENU_FILE, "r") as file:
            return json.load(file)

    def add_to_cart(self):

        menu = self.load_menu()

        try:
            food_id = int(input("Enter food ID: "))

            for item in menu:

                if item["id"] == food_id:

                    self.cart.append(item)
                    self.total += item["price"]

                    print(f"{item['name']} added to cart.")
                    return
            
            print("Food item not found.")
        
        except ValueError:
            print("Invalid input.")
    
    def view_cart(self):

        if not self.cart:
            print("Cart is empty.")
            return 
        
        print("\n========== YOUR CART ==========")

        for item in self.cart:
            print(f"{item['name']} - ₹{item['price']}")
        
        print(f"\nTotal Amount: ₹{self.total}")
        print("================================")

    def place_order(self):

        if not self.cart:
            print("Cannot place empty order.")
            return
        
        order_data = {
            "order_id": str(uuid.uuid4()),
            "items": self.cart,
            "total": self.total,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        try:
            with open(ORDERS_FILE, "r") as file:
                orders = json.load(file)
            
        except FileNotFoundError:
            order = []
        
        orders.append(order_data)

        with open(ORDERS_FILE, "w") as file:
            json.dump(orders, file, indent=4)

        print("\nOrder placed successfully!")
        print(f"Order Total: ₹{self.total}")

        self.cart = []
        self.total = 0