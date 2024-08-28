def main_app():
    import json

    try:
        with open('user.json', 'r') as file:
            user_alm = json.load(file)
    except FileNotFoundError:
        user_alm = {}

    status = None
    while status != 'exit':
        print("\n__________________________________________________________\n\nBienvenido a la aplicación. A continuación seleccione una opción:")
        choice = int(input("1. Registrarse en el sistema\n2. Iniciar sesión\n3. Salir\n"))

        if choice == 1:
            username, password = input("Ingrese su nombre de usuario y contraseña: ").split()
            if username in user_alm:
                print("El nombre de usuario ya existe.")
            else:
                user_alm[username] = password
            
            # Guardar el diccionario actualizado en el archivo JSON
            with open('users.json', 'w') as f:
                json.dump(user_alm, f, indent=4)
        
        elif choice == 2:
            # Buscar en el archivo o en el diccionario
            user_log1, pass_log1 = input("Ingrese su nombre de usuario y contraseña: ").split()
            if user_log1 in user_alm and user_alm[user_log1] == pass_log1:
                print("Inicio de sesión exitoso.")
                return None
            else:
                print("Usuario o contraseña incorrectos.")
            
        
        elif choice == 3:
            print("Gracias por usar la aplicación.")
            return None