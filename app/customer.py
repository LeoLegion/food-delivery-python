import json
import hashlib

USERS_FILE = "data/users.json"

class Customer:

    def __init__(self):
        self.logged_in_user = None

    def load_users(self):

        try:
            with open(USERS_FILE, "r") as file:
                return json.load(file)
            
        except FileNotFoundError:
            return []
    
    def save_users(self, users):

        with open(USERS_FILE, "w") as file:
            json.dump(users, file, indent=4)

    def hash_password(self, password):

        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self):

        users = self.load_users()

        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in users:

            if user["username"] == username:
                print("Username already exists.")
                return
        
        hashed_password = self.hash_password(password)

        new_user = {
            "username": username,
            "password": hashed_password
        }

        users.append(new_user)

        self.save_users(users)

        print("Registration successful!")
    
    def login(self):

        users = self.load_users()

        username = input("Enter username: ")
        password = input("Enter password: ")

        hashed_password = self.hash_password(password)

        for user in users:

            if (
                user["username"] == username
                and user["password"] == hashed_password
            ):

                self.logged_in_user = username

                print(f"Welcome, {username}!")
                return
        
        print("Invalid username or password.")
    
    def logout(self):

        if self.logged_in_user:
            print(f"{self.logged_in_user} logged out.")
            self.logged_in_user = None
        
        else:
            print("No user is logged in.")