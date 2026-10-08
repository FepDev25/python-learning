# =============================================================================
# EJERCICIO 05 - Strings: métodos, slicing y formateo
# Bloque: 5 (str_methods, slicing, format)
# =============================================================================
#
# Contexto:
#   Procesador de nombres de usuario para un sistema de registro.
#   Los datos llegan "sucios" y debes normalizarlos y validarlos.
#
# Instrucciones:
#
#   PARTE A - Limpieza y normalización
#   ------------------------------------
#   1. Tienes este nombre de usuario tal como lo escribió el usuario:
#       raw_input = "   felIPe  gómez_99   "
#
#   2. Aplica en orden:
#       a) Elimina espacios al inicio y al final (strip).
#       b) Conviértelo a minúsculas.
#       c) Reemplaza el guion bajo '_' por un punto '.'.
#       d) Guarda el resultado en username_limpio.
#
#   3. Imprime username_limpio. Resultado esperado: "felipe.gómez.99"
#
#   PARTE B - Validación
#   ---------------------
#   4. Usando solo métodos de string y operadores (sin regex), valida:
#       a) ¿El username_limpio empieza con una letra? (startswith con rango no
#          aplica; usa username_limpio[0].isalpha())
#       b) ¿Tiene al menos 6 caracteres? (len)
#       c) ¿Contiene algún dígito? (any + isdigit sobre cada caracter con for)
#          Guarda el resultado en tiene_numero (bool).
#
#   5. Imprime un resumen de validación con f-strings:
#       "Username: felipe.gómez.99 | Válido: True/False | Tiene número: True"
#       (Válido es True solo si cumple las 3 condiciones anteriores)
#
#   PARTE C - Slicing
#   ------------------
#   6. Con la cadena:
#       mensaje = "Python es poderoso y elegante"
#
#       a) Extrae la primera palabra ("Python") usando slicing por índice.
#       b) Extrae la última palabra ("elegante") usando índice negativo.
#       c) Obtén el mensaje al revés usando slicing con paso -1.
#       d) Extrae una de cada dos letras del mensaje completo.
#
#   PARTE D - Formateo avanzado con f-strings
#   ------------------------------------------
#   7. Genera un recibo de bienvenida formateado así (usa f-strings y
#      los resultados de las partes anteriores):
#
#       ╔══════════════════════════════╗
#       ║   BIENVENIDO AL SISTEMA      ║
#       ╠══════════════════════════════╣
#       ║ Usuario  : felipe.gómez.99   ║
#       ║ Longitud : 15 caracteres     ║
#       ║ Estado   : ACTIVO            ║
#       ╚══════════════════════════════╝
#
#      El estado es "ACTIVO" si el username es válido, "PENDIENTE" si no.
#      Usa una expresión ternaria para determinarlo en una línea.
