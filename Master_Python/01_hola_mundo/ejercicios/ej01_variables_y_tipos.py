# =============================================================================
# EJERCICIO 01 - Variables, Tipos de Datos y Conversión
# Bloques: 1 (quotes, type_python, my_numbers, none_null)
# =============================================================================
#
# Contexto:
#   Eres un cajero de una tienda. Debes registrar los datos de una venta
#   y mostrarlos correctamente tipados en pantalla.
#
# Instrucciones:
#
#   1. Crea las siguientes variables con los tipos indicados:
#       - nombre_producto  : str  → "Laptop Gamer Pro"
#       - precio_unitario  : float → 1299.99
#       - cantidad         : int  → 3
#       - en_oferta        : bool → True
#       - descuento        : None (aún no se ha definido el valor)
#
#   2. Imprime el tipo de cada variable usando type().
#
#   3. Calcula el subtotal (precio_unitario * cantidad) y almacénalo
#      en una variable. Imprime su tipo y valor.
#
#   4. Convierte precio_unitario a int y guárdalo como precio_entero.
#      Explica en un comentario qué información se pierde al hacer esa conversión.
#
#   5. Convierte cantidad a float y guárdala como cantidad_float.
#      ¿Por qué puede ser útil tener la cantidad como float?
#      Responde en un comentario.
#
#   6. Evalúa si descuento es falsy usando un if.
#      Si lo es, asígnale el valor 0.10 (10 % de descuento por ser oferta).
#      Si no, deja el valor que ya tiene.
#
#   7. Calcula el total final aplicando el descuento al subtotal.
#      Muestra el resultado con exactamente 2 decimales usando f-string.
#
#   Salida esperada (ejemplo):
#       Tipo de nombre_producto: <class 'str'>
#       ...
#       Total con descuento: $3509.97
