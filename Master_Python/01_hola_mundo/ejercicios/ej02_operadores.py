# =============================================================================
# EJERCICIO 02 - Operadores (Aritméticos, Relacionales, Lógicos, Identidad)
# Bloques: 2 (todos los operadores)
# =============================================================================
#
# Contexto:
#   Sistema de validación de acceso a un edificio. Un guardia registra
#   datos y el sistema decide si se permite el ingreso.
#
# Instrucciones:
#
#   PARTE A - Aritmética y precedencia
#   ------------------------------------
#   1. Tienes estas variables:
#       hora_entrada = 8       # hora de entrada al edificio
#       hora_salida  = 17      # hora de salida
#       tarifa_hora  = 150.5   # tarifa por hora en pesos
#
#   2. Calcula:
#       a) Horas trabajadas (resta simple).
#       b) Pago total bruto (horas * tarifa).
#       c) Pago con impuesto del 16 %: total * 1.16
#          IMPORTANTE: escríbelo en una sola línea respetando la precedencia
#          correcta (sin usar variables intermedias).
#       d) Horas extras si la jornada normal es 8 h. Usa max(0, horas - 8)
#          sin importar módulos, solo operadores y expresión ternaria.
#
#   PARTE B - Operadores relacionales y lógicos
#   --------------------------------------------
#   3. Define:
#       edad        = 25
#       tiene_gafete = True
#       nivel_acceso = 2   # niveles: 1=básico, 2=intermedio, 3=alto
#
#   4. Usando solo operadores relacionales y lógicos (sin if todavía), crea
#      variables booleanas que respondan:
#       a) ¿Es mayor de 18 Y tiene gafete?          → puede_entrar
#       b) ¿Tiene nivel 2 O nivel 3?                 → acceso_areas_restringidas
#       c) ¿NO tiene gafete O su nivel es menor a 2? → requiere_supervision
#
#   5. Imprime las tres variables con una descripción clara.
#
#   PARTE C - Identidad y pertenencia
#   -----------------------------------
#   6. Define:
#       motivo_visita = "reunión"
#       motivos_validos = ["reunión", "entrega", "mantenimiento", "entrevista"]
#       visitante_a = None
#       visitante_b = None
#
#   7. Comprueba:
#       a) ¿motivo_visita está en motivos_validos?       → visita_permitida
#       b) ¿visitante_a es el mismo objeto que visitante_b? → son_el_mismo
#          (usa is, no ==). Explica en un comentario por qué es True.
#
#   8. Muestra un resumen final con todos los resultados usando f-strings.
