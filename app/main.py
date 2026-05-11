from menu import display_menu, add_food_item, search_food
from order import Order
from customer import Customer

customer = Customer()
order = Order(customer)

def show_options():

    print("\n===== FOOD DELIVERY APP =====")

    if customer.logged_in_user:
        print(f"Logged in as: {customer.logged_in_user}")

    print("1. Register")
    print("2. Login")
    print("3. Display Menu")
    print("4. Add Food Item")
    print("5. Search Food")
    print("6. Add to Cart")
    print("7. View Cart")
    print("8. Place Order")
    print("9. Logout")
    print("10. Exit")


def main():

    while True:

        show_options()

        choice = input("Enter your choice: ")

        if choice == "1":
            customer.register()
        
        elif choice == "2":
            customer.login()

        elif choice == "3":
            display_menu()
        
        elif choice == "4":
            add_food_item()

        elif choice == "5":
            search_food()

        elif choice == "6":
            display_menu()
            order.add_to_cart()
        
        elif choice == "7":
            order.view_cart()

        elif choice == "8":
            order.place_order()
        
        elif choice == "9":
            customer.logout()
        
        elif choice == "10":
            print("Thank you for using the app.")
            break
        
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()