import json 

filename= "bodega.json"


class Bodega:
    @staticmethod
    def open_warehouse():
        with open(filename, "r") as file:
            warehouse = json.load(file)
            print(warehouse)
    

class System:
    def __init__(self, admin_password):
        self.admin_password = admin_password
        self.users = []  # Lista para almacenar los usuarios registrados en el sistema

    def authenticate_admin(self, password):
        return password == self.admin_password
    
    def get_users(self):
        return self.users


class User:
    def __init__(self, system, name, phone, email, password, username, role):
        self.system = system
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.username = username
        self.role = role

    def register_user(self):
        #if len(self.password) < 10 or not any(char.isupper() for char in self.password) or not any(char.islower() for char in self.password):
         #   raise ValueError("The password must have at least 10 characters, including one uppercase and one lowercase letter.")

        #if self.role.lower() not in ["client", "provider", "personal"]:
         #   raise ValueError("The role must be client, provider or personal.")

        #if len(self.phone) != 10:
        #    raise ValueError("The phone number must have 10 digits.")

        self.system.users.append(self)  # Agrega el usuario al sistema
        print(f"\nUser {self.username} registered as {self.role}.")

    def login(self, username, password):
        for user in system.users:
            if self.username == username and self.password == password:
                print("Welcome to the system!")

                

            else:
                print("Invalid username or password.")
                register(system)


            
def register(system):
    print("Welcome to the Warehouse System.")
    
    
    while True:
        
        print("\nPlease choose an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print("4. Show users")  # This is for testing if the users are registered

        option = input("Enter your choice: ")
        
        if option == "1":
            print("\nPlease register a new user:")
            name = input("Enter your name: ")
            phone = input("Enter your phone number: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            username = input("Enter your username: ").lower()
            role = input("Enter your role (client, provider, personal): ")

            user = User(system, name, phone, email, password, username, role)
            user.register_user()

        if option == "2":
            username1 = input("Enter your username: ").lower()
            password1 = input("Enter your password: ")
            user.login(username1, password1)
            break
            
        elif option == "3":
            print("Exiting program. Goodbye!")
            break

        elif option == "4":
            User.display_registered_users(system)

        else:
            print("Invalid option. Please enter a valid choice.")

system = System("admin123")
register(system)
