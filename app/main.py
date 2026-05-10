from menu import display_menu, add_food_item, search_food
from order import Order

order = Order()

def show_options():

    print("\n===== FOOD DELIVERY APP =====")

    print("1. Display Menu")
    print("2. Add Food Item")
    print("3. Search Food")
    print("4. Add to Cart")
    print("5. View Cart")
    print("6. Place Order")
    print("7. Exit")


def main():

    while True:

        show_options()

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()
        
        elif choice == "2":
            add_food_item()
        
        elif choice == "3":
            search_food()

        elif choice == "4":
            display_menu()
            order.add_to_cart()
        
        elif choice == "5":
            order.view_cart()

        elif choice == "6":
            order.place_order()
        
        elif choice == "7":
            print("Thank you for using the app.")
            break
        
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()