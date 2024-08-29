import json
from datetime import datetime

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
        while True:
            try:
                username, password = input("Enter your username and password: ").split()
                if username in self.user_data:
                    print("The username already exists.")
                else:
                    self.user_data[username] = password
                    self.save_users()
                    print(f"User {username} successfully registered.")
                    break
            except ValueError:
                print("Invalid input format. Please enter both username and password.")

    def login_user(self):
        while True:
            try:
                username, password = input("Enter your username and password: ").split()
                if username in self.user_data and self.user_data[username] == password:
                    print("Login successful.")
                    return True
                else:
                    print("Incorrect username or password.")
            except ValueError:
                print("Invalid input format. Please enter both username and password.")

# Supplier Class
class Supplier:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

# Product Classes
class Product:
    def __init__(self, name, quantity, price, supplier=None, min_stock=0, max_stock=None):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
        self.min_stock = min_stock
        self.max_stock = max_stock

    def __str__(self):
        return f"Product: {self.name}, Quantity: {self.quantity}, Price: {self.price}, Supplier: {self.supplier.name if self.supplier else 'N/A'}"

    def update_quantity(self, quantity):
        self.quantity = quantity

    def update_price(self, price):
        self.price = price

    def check_stock(self):
        if self.quantity < self.min_stock:
            print(f"Warning: {self.name} is below the minimum stock level!")
        if self.max_stock and self.quantity > self.max_stock:
            print(f"Warning: {self.name} exceeds the maximum stock level!")

class PerishableProduct(Product):
    def __init__(self, name, quantity, price, expiration_date, supplier=None, min_stock=0, max_stock=None):
        super().__init__(name, quantity, price, supplier, min_stock, max_stock)
        self.expiration_date = expiration_date

    def __str__(self):
        return f"Perishable Product: {self.name}, Quantity: {self.quantity}, Price: {self.price}, Expiration Date: {self.expiration_date}, Supplier: {self.supplier.name if self.supplier else 'N/A'}"

class NonPerishableProduct(Product):
    def __init__(self, name, quantity, price, shelf_life, supplier=None, min_stock=0, max_stock=None):
        super().__init__(name, quantity, price, supplier, min_stock, max_stock)
        self.shelf_life = shelf_life

    def __str__(self):
        return f"Non-Perishable Product: {self.name}, Quantity: {self.quantity}, Price: {self.price}, Shelf Life: {self.shelf_life}, Supplier: {self.supplier.name if self.supplier else 'N/A'}"

# Inventory Management Class
class Inventory:
    def __init__(self):
        self.total_inv = []
        self.transaction_history = []

    def show_inventory(self):
        if not self.total_inv:
            print("Inventory is empty.")
        else:
            for index, product in enumerate(self.total_inv, start=1):
                print(f"{index}. {product}")

    def add_product(self, product):
        self.total_inv.append(product)
        self.transaction_history.append(f"Added {product.name} at {datetime.now()}")
        print(f"{product.name} added to inventory.")

    def remove_product(self, product_index):
        try:
            removed_product = self.total_inv.pop(product_index)
            self.transaction_history.append(f"Removed {removed_product.name} at {datetime.now()}")
            print(f"{removed_product.name} removed from inventory.")
        except IndexError:
            print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def update_product(self, product_index, quantity=None, price=None):
        try:
            product = self.total_inv[product_index]
            if quantity is not None:
                product.update_quantity(quantity)
            if price is not None:
                product.update_price(price)
            self.transaction_history.append(f"Updated {product.name} at {datetime.now()}")
            print(f"{product.name} updated.")
        except IndexError:
            print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    def search_product(self, name=None, category=None, min_price=None, max_price=None):
        results = []
        for product in self.total_inv:
            if (name and name.lower() in product.name.lower()) or \
               (category and isinstance(product, category)) or \
               (min_price is not None and product.price >= min_price) or \
               (max_price is not None and product.price <= max_price):
                results.append(product)
        return results

    def generate_report(self, report_type="all"):
        if report_type == "all":
            print("Full Inventory Report:")
            self.show_inventory()
        elif report_type == "low_stock":
            print("Low Stock Report:")
            for product in self.total_inv:
                if product.quantity < product.min_stock:
                    print(product)
        elif report_type == "expiring_soon":
            print("Expiring Soon Report:")
            for product in self.total_inv:
                if isinstance(product, PerishableProduct) and product.expiration_date < datetime.now().date():
                    print(product)
        else:
            print("Invalid report type.")

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
                    print("5. Search for a product")
                    print("6. Generate inventory report")
                    print("7. Log out")
                    
                    while True:
                        try:
                            inventory_choice = int(input("Enter your choice: "))
                            if inventory_choice in [1, 2, 3, 4, 5, 6, 7]:
                                break
                            else:
                                print("Invalid choice, please try again.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")

                    if inventory_choice == 1:
                        while True:
                            product_type = input("Is the product perishable (yes/no)? ").strip().lower()
                            if product_type in ['yes', 'no']:
                                break
                            else:
                                print("Please answer with 'yes' or 'no'.")
                        
                        name = input("Enter product name: ")
                        while True:
                            try:
                                quantity = int(input("Enter product quantity: "))
                                price = float(input("Enter product price: "))
                                min_stock = int(input("Enter minimum stock level: "))
                                max_stock = input("Enter maximum stock level (leave blank for no limit): ")
                                max_stock = int(max_stock) if max_stock else None
                                break
                            except ValueError:
                                print("Invalid input. Please enter numeric values for quantity, price, and stock levels.")
                        
                        supplier_name = input("Enter supplier name: ")
                        supplier_contact = input("Enter supplier contact information: ")
                        supplier = Supplier(supplier_name, supplier_contact)

                        if product_type == 'yes':
                            while True:
                                expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
                                try:
                                    expiration_date_parsed = datetime.strptime(expiration_date, "%Y-%m-%d").date()
                                    break
                                except ValueError:
                                    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                            product = PerishableProduct(name, quantity, price, expiration_date_parsed, supplier, min_stock, max_stock)
                        else:
                            shelf_life = input("Enter shelf life (e.g., 2 years): ")
                            product = NonPerishableProduct(name, quantity, price, shelf_life, supplier, min_stock, max_stock)
                        
                        inventory.add_product(product)

                    elif inventory_choice == 2:
                        print("Current Inventory:")
                        inventory.show_inventory()
                        while True:
                            try:
                                product_index = int(input("Enter the number of the product to remove: ")) - 1
                                inventory.remove_product(product_index)
                                break
                            except ValueError:
                                print("Invalid input. Please enter a valid number.")

                    elif inventory_choice == 3:
                        print("Current Inventory:")
                        inventory.show_inventory()
                        while True:
                            try:
                                product_index = int(input("Enter the number of the product to edit: ")) - 1
                                quantity = input("Enter new quantity (leave empty to keep current): ")
                                price = input("Enter new price (leave empty to keep current): ")

                                new_quantity = int(quantity) if quantity else None
                                new_price = float(price) if price else None

                                inventory.update_product(product_index, quantity=new_quantity, price=new_price)
                                break
                            except ValueError:
                                print("Invalid input. Please enter valid numbers for quantity and price.")

                    elif inventory_choice == 4:
                        print("Current Inventory:")
                        inventory.show_inventory()

                    elif inventory_choice == 5:
                        print("Search for a Product:")
                        search_name = input("Enter product name to search (leave empty to skip): ")
                        search_category = input("Enter category to search (perishable/non-perishable, leave empty to skip): ").strip().lower()
                        while True:
                            try:
                                search_min_price = input("Enter minimum price to search (leave empty to skip): ")
                                search_max_price = input("Enter maximum price to search (leave empty to skip): ")
                                search_min_price = float(search_min_price) if search_min_price else None
                                search_max_price = float(search_max_price) if search_max_price else None
                                break
                            except ValueError:
                                print("Invalid input. Please enter numeric values for prices.")

                        if search_category == 'perishable':
                            category = PerishableProduct
                        elif search_category == 'non-perishable':
                            category = NonPerishableProduct
                        else:
                            category = None

                        results = inventory.search_product(name=search_name, category=category, min_price=search_min_price, max_price=search_max_price)
                        if results:
                            print("Search Results:")
                            for result in results:
                                print(result)
                        else:
                            print("No products found matching your criteria.")

                    elif inventory_choice == 6:
                        print("Generate Report:")
                        print("1. Full Inventory")
                        print("2. Low Stock")
                        print("3. Expiring Soon")
                        while True:
                            try:
                                report_choice = int(input("Enter your choice: "))
                                if report_choice in [1, 2, 3]:
                                    break
                                else:
                                    print("Invalid choice. Please choose 1, 2, or 3.")
                            except ValueError:
                                print("Invalid input. Please enter a number.")

                        if report_choice == 1:
                            inventory.generate_report(report_type="all")
                        elif report_choice == 2:
                            inventory.generate_report(report_type="low_stock")
                        elif report_choice == 3:
                            inventory.generate_report(report_type="expiring_soon")

                    elif inventory_choice == 7:
                        print("Logging out.")
                        break

        elif choice == '3':
            print("Thank you for using the application. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")
