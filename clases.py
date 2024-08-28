import json

# User Management Classes
class UserManager:
    def __init__(self, user_file='users.json'):
        self.user_file = user_file
        self.user_data = self.load_users()

    def load_users(self):
        try:
            with open(self.user_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open(self.user_file, 'w') as file:
            json.dump(self.user_data, file, indent=4)

    def register_user(self):
        username, password = input("Enter your username and password: ").split()
        if username in self.user_data:
            print("The username already exists.")
        else:
            self.user_data[username] = password
            self.save_users()
            print(f"User {username} successfully registered.")

    def login_user(self):
        username, password = input("Enter your username and password: ").split()
        if username in self.user_data and self.user_data[username] == password:
            print("Login successful.")
            return True
        else:
            print("Incorrect username or password.")
            return False

# Product Classes
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Quantity: {self.quantity}, Price: {self.price}"

    def update_quantity(self, quantity):
        self.quantity = quantity

    def update_price(self, price):
        self.price = price

class PerishableProduct(Product):
    def __init__(self, name, quantity, price, expiration_date):
        super().__init__(name, quantity, price)
        self.expiration_date = expiration_date

    def __str__(self):
        return f"Perishable Product: {self.name}, Quantity: {self.quantity}, Price: {self.price}, Expiration Date: {self.expiration_date}"

class NonPerishableProduct(Product):
    def __init__(self, name, quantity, price, shelf_life):
        super().__init__(name, quantity, price)
        self.shelf_life = shelf_life

    def __str__(self):
        return f"Non-Perishable Product: {self.name}, Quantity: {self.quantity}, Price: {self.price}, Shelf Life: {self.shelf_life}"

# Inventory Management Class
class Inventory:
    def __init__(self):
        self.total_inv = []

    def show_inventory(self):
        if not self.total_inv:
            print("Inventory is empty.")
        else:
            for index, product in enumerate(self.total_inv, start=1):
                print(f"{index}. {product}")

    def add_product(self, product):
        self.total_inv.append(product)
        print(f"{product.name} added to inventory.")

    def remove_product(self, product_index):
        try:
            removed_product = self.total_inv.pop(product_index)
            print(f"{removed_product.name} removed from inventory.")
        except IndexError:
            print("Invalid selection. Please try again.")

    def update_product(self, product_index, quantity=None, price=None):
        try:
            product = self.total_inv[product_index]
            if quantity is not None:
                product.update_quantity(quantity)
            if price is not None:
                product.update_price(price)
            print(f"{product.name} updated.")
        except IndexError:
            print("Invalid selection. Please try again.")

# Main application loop with menus
if __name__ == "__main__":
    user_manager = UserManager()
    
    while True:
        print("\nWelcome to the warehouse application. Please choose an option:")
        print("1. Register")
        print("2. Log in")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_manager.register_user()
        
        elif choice == '2':
            if user_manager.login_user():  # If login is successful
                inventory = Inventory()
                
                while True:
                    print("\nInventory Management Menu:")
                    print("1. Add a new product")
                    print("2. Remove a product")
                    print("3. Edit a product")
                    print("4. Show inventory")
                    print("5. Log out")
                    inventory_choice = input("Enter your choice: ")

                    if inventory_choice == '1':
                        product_type = input("Is the product perishable (yes/no)? ").lower()
                        name = input("Enter product name: ")
                        quantity = int(input("Enter product quantity: "))
                        price = float(input("Enter product price: "))

                        if product_type == 'yes':
                            expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
                            product = PerishableProduct(name, quantity, price, expiration_date)
                        else:
                            shelf_life = input("Enter shelf life (e.g., 2 years): ")
                            product = NonPerishableProduct(name, quantity, price, shelf_life)
                        
                        inventory.add_product(product)

                    elif inventory_choice == '2':
                        print("Current Inventory:")
                        inventory.show_inventory()
                        product_index = int(input("Enter the number of the product to remove: ")) - 1
                        inventory.remove_product(product_index)

                    elif inventory_choice == '3':
                        print("Current Inventory:")
                        inventory.show_inventory()
                        product_index = int(input("Enter the number of the product to edit: ")) - 1
                        quantity = input("Enter new quantity (leave empty to keep current): ")
                        price = input("Enter new price (leave empty to keep current): ")

                        new_quantity = int(quantity) if quantity else None
                        new_price = float(price) if price else None

                        inventory.update_product(product_index, quantity=new_quantity, price=new_price)

                    elif inventory_choice == '4':
                        print("Current Inventory:")
                        inventory.show_inventory()

                    elif inventory_choice == '5':
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice. Please try again.")
        
        elif choice == '3':
            print("Thank you for using the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")
