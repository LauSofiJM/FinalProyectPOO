class Producto:
    # Información básica del producto
    def __init__(self, product_name, product_code, product_category, product_type, product_brand, product_supplier, product_description):
        self.product_name = product_name
        self.product_code = product_code
        self.product_category = product_category
        self.product_type = product_type
        self.product_brand = product_brand
        self.product_supplier = product_supplier
        self.product_description = product_description

        # Inicializar categorías con valores predeterminados o nulos
        self.inventario = None
        self.precios = None
        self.detalles_adicionales = None

    # Inventario del producto
    def establecer_inventario(self, product_quantity, product_min_quantity, product_max_quantity, product_sold_quantity, product_bought_quantity, product_status):
        self.inventario = {
            "cantidad": product_quantity,
            "cantidad_minima": product_min_quantity,
            "cantidad_maxima": product_max_quantity,
            "cantidad_vendida": product_sold_quantity,
            "cantidad_comprada": product_bought_quantity,
            "estado": product_status
        }
    
    def obtener_inventario(self):
        return self.inventario

    # Precios del producto
    def establecer_precios(self, product_price, product_purchase_price, product_sale_price):
        self.precios = {
            "precio": product_price,
            "precio_compra": product_purchase_price,
            "precio_venta": product_sale_price
        }
    
    def obtener_precios(self):
        return self.precios

    # Detalles adicionales del producto
    def establecer_detalles_adicionales(self, product_expiration, product_location, product_purchase_date, product_size, product_color, product_weight):
        self.detalles_adicionales = {
            "fecha_vencimiento": product_expiration,
            "ubicacion": product_location,
            "fecha_compra": product_purchase_date,
            "tamaño": product_size,
            "color": product_color,
            "peso": product_weight
        }
    
    def obtener_detalles_adicionales(self):
        return self.detalles_adicionales
    
    def a_diccionario(self):
        return {
            "informacion_basica": {
                "nombre": self.product_name,
                "codigo": self.product_code,
                "categoria": self.product_category,
                "tipo": self.product_type,
                "marca": self.product_brand,
                "proveedor": self.product_supplier,
                "descripcion": self.product_description
            },
            "inventario": self.inventario if self.inventario else {},
            "precios": self.precios if self.precios else {},
            "detalles_adicionales": self.detalles_adicionales if self.detalles_adicionales else {}
        }

class Alimentos(Producto):
    def tipo_aliment(self, tipo_alimento, defincion):
        return f"Tipo de alimento: {tipo_alimento}, es decir, {defincion}"
    def niveles(self, nivel_azucares , nivel_sodio):
        assert nivel_azucares.lower() in ['alto', 'medio', 'bajo'], "El nivel de azúcar debe ser 'alto', 'medio' o 'bajo'"
        assert nivel_sodio.lower() in ['alto', 'medio', 'bajo'], "El nivel de azúcar debe ser 'alto', 'medio' o 'bajo'"
        return f"Cuenta con un nivel de azucar {nivel_azucares} y un nivel de sodio {nivel_sodio}"
    
class Ropa(Producto):
    def talla(self, talla):
        assert talla.lower() in ['s', 'm', 'l', 'xl'], "Las tallas están en malébolo s, m, l o xl"
        return f"La talla del producto es: {talla}"
    
    def tipo_tela(self, tela, veces_lavado):
        return f"El tipo de tela es: {tela} y las veces de washing es {veces_lavado}"
    
    def prenda(self, prenda):
        return f"El tipo de prenda es {prenda}"

class Tecnologia(Producto):
    def dispositivo(self, dispositivo):
        return f"Este dispositivo es un/a {dispositivo}."

    def memoria(self, memoria):
        return f"Memoria: {memoria} GB."

    def tipo_cargador(self, cargador):
        assert cargador.lower() in ['tipo c', 'tipo b'], "El cargador debe ser 'tipo c' o 'tipo b'."
        return f"Tipo de cargador: {cargador}."

    def accesorios_incluidos(self, accesorios: list):
        accesorios_str = ", ".join(accesorios)
        return f"Accesorios incluidos: {accesorios_str}."

class Cosmeticos(Producto):
    def tipo_cosmetico(self, tipo):
        assert tipo.lower() in ['crema', 'lociones', 'pomadas', 'polvos']
        return f"Cosmetico de tipo {tipo}"
    
    def uso(self, uso):
        assert uso.lower() in ['limpieza profunda', 'embellecedora', 'tratamiento acne']
        return f"Cosmetico para uso de {uso}"
    
    def tipos_de_piel(self, tipos_pieles):
        return f"Para uso en pieles {tipos_pieles}"