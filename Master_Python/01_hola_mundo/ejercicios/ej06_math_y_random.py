# =============================================================================
# EJERCICIO 06 - Módulos math y random
# Bloque: 6 (math_sample, random_sample)
# =============================================================================
#
# Contexto:
#   Mini simulador de un juego de dados con estadísticas.
#   Combinarás generación aleatoria con funciones matemáticas.
#
# Instrucciones:
#
#   PARTE A - Simulación de lanzamientos
#   --------------------------------------
#   1. Importa los módulos math y random.
#
#   2. Simula el lanzamiento de 2 dados de 6 caras, 20 veces.
#      Usa un bucle for y random.randint(1, 6) para cada dado.
#      En cada lanzamiento guarda la suma de los dos dados en una lista
#      llamada resultados.
#
#   3. Imprime la lista resultados.
#
#   PARTE B - Estadísticas con math
#   ---------------------------------
#   4. Con la lista resultados calcula (sin importar statistics):
#       a) Suma total de todos los lanzamientos.
#       b) Promedio (suma / cantidad).
#       c) El valor máximo y mínimo usando max() y min().
#       d) La raíz cuadrada del promedio usando math.sqrt().
#          Redondea el resultado a 4 decimales con round().
#       e) El promedio redondeado hacia arriba (math.ceil) y
#          hacia abajo (math.floor).
#
#   5. Imprime todas las estadísticas con f-strings y etiquetas claras.
#
#   PARTE C - Probabilidad básica
#   -------------------------------
#   6. Cuenta cuántas veces la suma de los dados fue:
#       a) 7 (el resultado más probable estadísticamente).
#       b) 2 o 12 (los resultados menos probables).
#       c) Mayor que 9.
#
#   7. Para cada conteo calcula el porcentaje sobre 20 lanzamientos
#      y muéstralo con 1 decimal.
#
#   PARTE D - Geometría con math
#   ------------------------------
#   8. Calcula e imprime:
#       a) El área y perímetro de un círculo con radio = 7.5
#          (usa math.pi y math.pow).
#       b) La hipotenusa de un triángulo rectángulo con catetos 3 y 4
#          (usa math.sqrt y el teorema de Pitágoras). ¿Coincide con math.hypot?
#       c) El seno y coseno de 45 grados
#          (convierte primero a radianes con math.radians).
#
#   Reto adicional (opcional):
#       Ejecuta la simulación con una semilla fija (random.seed(42)) al inicio
#       y verifica que obtienes los mismos resultados cada vez que corres el script.
#       Explica en un comentario para qué sirve fijar la semilla.
