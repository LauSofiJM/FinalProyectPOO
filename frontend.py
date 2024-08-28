from register import main_app
# Importar la clase Producto desde el archivo clases.py
from clases import Producto, Alimentos, Ropa, Tecnologia, Cosmeticos

# Lista para mantener un registro de productos existentes en el inventario
productos_existentes = []
main_app()

status = None
while status != 'exit':
    print("\n__________________________________________________________")
    print("\n\nGracias por usar la aplicación. Seleccione las siguientes opciones para habilitar inventario: ")
    choice = int(input("1. Agregar algo al inventario\n2. Salir\n"))
    
    if choice == 1:
        product_name = input("Ingrese el nombre del producto: ") 
        product_code = input("Ingrese el código del producto: ")
        
        # Generar un nombre único para el producto
        nombre_unico = f"{product_name.strip()}--{product_code.strip()}"# Eliminar espacios en blanco al principio
        productos_existentes
        # Verificar si el producto ya existe en el inventario
        if nombre_unico in productos_existentes:
            print("\nEl producto ya existe en el inventario.")
            continue
        else:
            # Obtener información adicional del producto
            print("Seleccionar.\n1. Alimentos\n2. Ropa\n3. Tecnología\n4. Cosmeticos\n5. Hogar\n6. Otro")
            product_category = input("Ingrese la categoria del producto")
            product_category1 = int(input("Ingrese el numero la categoría del producto: "))

                
            product_type = input("Ingrese el tipo de producto: ")
            product_brand = input("Ingrese la marca del producto: ")
            product_supplier = input("Ingrese el proveedor del producto: ")
            product_description = input("Ingrese la descripción del producto: ")
            
            # Crear una nueva instancia de Producto
            if product_category1 == 1:
                producto_new = Alimentos(product_name, product_code, product_category, product_type, product_brand, product_supplier, product_description)
            elif product_category1 == 2:
                producto_new = Ropa(product_name, product_code, product_category, product_type, product_brand, product_supplier, product_description)
            elif product_category1 == 3:
                producto_new = Tecnologia(product_name, product_code, product_category, product_type, product_brand, product_supplier, product_description)
            elif product_category1 == 4:
                producto_new = Cosmeticos(product_name, product_code, product_category, product_type, product_brand, product_supplier, product_description)
            else:
                producto_new = Producto(product_name, product_code, product_category, product_type, product_brand, product_supplier, product_description)
                            
            
            # Agregar el nombre único del producto a la lista de productos existentes
            productos_existentes.append(nombre_unico)
            
