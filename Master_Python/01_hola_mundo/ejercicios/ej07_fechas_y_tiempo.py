# =============================================================================
# EJERCICIO 07 - Fechas, Tiempo y Calendario
# Bloque: 7 (date_time_today, datetime_now, datetime_str, compare_date,
#            calendar_python, timestamp)
# =============================================================================
#
# Contexto:
#   Sistema de gestión de membresías. Debes calcular vigencias,
#   días restantes y medir el rendimiento de operaciones con fechas.
#
# Instrucciones:
#
#   PARTE A - Creación y formateo de fechas
#   ----------------------------------------
#   1. Importa datetime, date, timedelta desde el módulo datetime,
#      también importa calendar y time.
#
#   2. Obtén la fecha y hora actual y guárdalas en ahora.
#
#   3. Muestra la fecha actual en estos tres formatos distintos:
#       a) "19/02/2026"           (formato DD/MM/YYYY)
#       b) "jueves, 19 de febrero de 2026"   (formato largo en español,
#           construye el string manualmente con strftime y un diccionario
#           de nombres de meses/días, NO uses locale)
#       c) "2026-02-19T14:35:00"  (formato ISO 8601)
#
#   PARTE B - Aritmética de fechas
#   --------------------------------
#   4. Tienes estas membresías (fecha de inicio como string):
#       miembros = [
#           {"nombre": "Ana López",    "inicio": "2025-11-15", "duracion_dias": 90},
#           {"nombre": "Carlos Ruiz",  "inicio": "2026-01-01", "duracion_dias": 365},
#           {"nombre": "María Torres", "inicio": "2025-08-20", "duracion_dias": 180},
#       ]
#
#   5. Para cada miembro:
#       a) Parsea la fecha de inicio con strptime.
#       b) Calcula la fecha de vencimiento (inicio + timedelta(duracion_dias)).
#       c) Calcula los días restantes (vencimiento - hoy). Si es negativo,
#          la membresía ya venció.
#       d) Determina el estado: "VIGENTE", "VENCIDA" o
#          "POR VENCER" (si quedan 15 días o menos).
#       e) Imprime una fila formateada para cada miembro.
#
#   Ejemplo de salida:
#       Ana López    | Vence: 13/02/2026 | Días restantes:  -6 | VENCIDA
#       Carlos Ruiz  | Vence: 01/01/2027 | Días restantes: 315 | VIGENTE
#       María Torres | Vence: 16/02/2026 | Días restantes:  -3 | VENCIDA
#
#   PARTE C - Calendario
#   ----------------------
#   6. Pide al usuario un año con input() y valida que sea un número entero
#      mayor a 1582 (inicio del calendario gregoriano).
#
#   7. Con ese año:
#       a) Indica si es bisiesto usando calendar.isleap().
#       b) Muestra cuántos días tiene febrero ese año.
#       c) Imprime el calendario completo del mes de marzo de ese año
#          usando calendar.month().
#
#   PARTE D - Medición de rendimiento
#   ------------------------------------
#   8. Mide cuánto tiempo tarda en ejecutarse un bucle que suma
#      los días restantes de todos los miembros 100,000 veces.
#      Usa time.perf_counter() antes y después del bucle.
#      Muestra el tiempo en milisegundos con 4 decimales.
