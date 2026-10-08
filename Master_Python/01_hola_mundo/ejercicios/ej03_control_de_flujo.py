# =============================================================================
# EJERCICIO 03 - Flujo de Control: if/elif/else, match/case, ternario
# Bloques: 3 y 4 (input, if_statements, ternary, case)
# =============================================================================
#
# Contexto:
#   Simulador de calificaciones de una academia. El usuario ingresa su
#   puntaje y el sistema le indica su nivel, si aprobó y qué debe hacer.
#
# Instrucciones:
#
#   1. Pide al usuario que ingrese su puntaje (0-100) usando input().
#      Convierte el valor a int. Si la conversión falla, muestra un mensaje
#      de error y termina el programa (usa try/except).
#
#   2. Valida que el puntaje esté entre 0 y 100 (inclusive).
#      Si está fuera de rango, informa al usuario y termina.
#
#   3. Determina la letra de calificación con if/elif/else:
#       90 - 100  → "A"
#       80 -  89  → "B"
#       70 -  79  → "C"
#       60 -  69  → "D"
#        0 -  59  → "F"
#
#   4. Usando match/case sobre la letra obtenida, imprime:
#       "A" → "Excelente. Eres candidato a beca."
#       "B" → "Muy bien. Sigue así."
#       "C" → "Aprobado. Hay margen de mejora."
#       "D" → "Aprobado por mínimo. Se recomienda tutoría."
#       "F" → "Reprobado. Debes repetir el módulo."
#       _   → "Calificación desconocida."
#
#   5. Usando una expresión ternaria (una sola línea), define:
#       estado = "APROBADO" si puntaje >= 60, de lo contrario "REPROBADO"
#
#   6. Muestra el resumen final con f-string:
#       ----------------------------------------
#       Puntaje  : 85
#       Letra    : B
#       Estado   : APROBADO
#       Mensaje  : Muy bien. Sigue así.
#       ----------------------------------------
#
#   Reto adicional (opcional):
#       Envuelve todo en un while True para que el programa siga pidiendo
#       puntajes hasta que el usuario escriba "salir".
