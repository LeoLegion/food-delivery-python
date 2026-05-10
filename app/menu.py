import json

MENU_FILE = "data/menu.json"

def load_menu():
    try:
        with open(MENU_FILE, "r") as file:
            menu = json.load(file)
            return menu
    
    except FileNotFoundError:
        return []

def display_menu():
    menu = load_menu()

    print("\n========== FOOD MENU ==========")

    for item in menu:
        print(f"{item['id']}. {item['name']} - ₹{item['price']}")
    
    print("================================")


def add_food_item():
    menu = load_menu()

    food_id = len(menu) + 1
    name = input("Enter food name: ")
    price = float(input("Enter price: "))

    new_item = {
        "id": food_id,
        "name": name,
        "price": price
    }

    menu.append(new_item)

    with open(MENU_FILE, "w") as file:
        json.dump(menu, file, indent=4)
    
    print(f"{name} added successfully!")


def search_food():
    menu = load_menu()

    keyword = input("Enter food name to search: ").lower()

    found = False

    for item in menu:
        if keyword in item["name"].lower():
            print(f"Found: {item['name']} - ₹{item['price']}")
            found = True

    if not found:
        print("Food item not found.")