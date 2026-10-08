# =============================================================================
# EJERCICIO 04 - Bucles: while, for, continue, break
# Bloque: 4 (while_statements, for_statements, label_control)
# =============================================================================
#
# Contexto:
#   Administrador de inventario. El sistema recorre productos, detecta
#   problemas y genera reportes usando bucles.
#
# Instrucciones:
#
#   PARTE A - for + continue + break
#   ----------------------------------
#   1. Tienes esta lista de precios de productos (algunos inválidos):
#       precios = [120.5, -30, 450, 0, 89.9, -5, 320, 0, 210, 175]
#
#   2. Recorre la lista con for. Para cada precio:
#       a) Si es negativo: imprime "Precio inválido: <precio>. Saltando..."
#          y usa continue para no procesarlo.
#       b) Si es 0: imprime "Precio en cero detectado. Deteniendo revisión."
#          y usa break para detener el bucle.
#       c) Si es válido (> 0): acumula el precio en una variable total
#          y cuenta cuántos productos válidos procesaste.
#
#   3. Al finalizar (o al hacer break), imprime:
#       - Cuántos productos válidos se procesaron.
#       - El total acumulado (con 2 decimales).
#       - El promedio de los precios válidos (con 2 decimales).
#
#   PARTE B - while con acumulador
#   --------------------------------
#   4. Simula un sistema de descuentos progresivos:
#       - Parte de un precio base de 1000.
#       - Cada iteración aplica un descuento del 15 % al precio actual.
#       - Detén el bucle cuando el precio baje de 200.
#       - En cada vuelta imprime: "Vuelta <n>: precio actual = <precio>"
#       - Al finalizar, imprime cuántas iteraciones tomó llegar a ese precio.
#
#   PARTE C - for anidado
#   ----------------------
#   5. Genera la tabla de multiplicar del 6 al 9 (ambos inclusive)
#      usando dos for anidados con range().
#      Formato de cada línea: "6 x 1 = 6"
#      Separa cada tabla con una línea en blanco.
#
#   Reto adicional (opcional):
#       En la Parte A, en lugar de break al encontrar precio 0,
#       reemplaza ese 0 por el promedio de los precios válidos hasta ese
#       momento y sigue procesando. Al final informa cuántos reemplazos hiciste.
