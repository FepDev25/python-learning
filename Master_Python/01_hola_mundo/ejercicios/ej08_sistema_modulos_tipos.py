# =============================================================================
# EJERCICIO 08 - Sistema, Módulos, isinstance y __main__
# Bloques: 8 y 9 (os_getenv, platform_sample, system_sample, is_instance,
#                  other, main)
# =============================================================================
#
# Contexto:
#   Script de diagnóstico del entorno. Al ejecutarlo debe recopilar
#   información del sistema, validar tipos de datos y comportarse
#   diferente según si se ejecuta directamente o se importa.
#
# Instrucciones:
#
#   PARTE A - Información del entorno
#   -----------------------------------
#   1. Importa os, sys y platform.
#
#   2. Recopila y muestra en pantalla:
#       a) Sistema operativo y versión  (platform.system(), platform.version())
#       b) Versión de Python            (sys.version)
#       c) PID del proceso actual       (os.getpid())
#       d) Directorio de trabajo actual (os.getcwd())
#       e) Variable de entorno PATH (solo los primeros 80 caracteres,
#          usa os.getenv y slicing)
#       f) Argumentos de línea de comandos pasados al script (sys.argv).
#          Si no se pasó ninguno (len == 1), muestra "Sin argumentos".
#
#   PARTE B - Escritura en stdout y stderr
#   ----------------------------------------
#   3. Escribe directamente en sys.stdout el mensaje:
#          "[INFO] Diagnóstico iniciado correctamente.\n"
#
#   4. Simula un error escribiendo en sys.stderr:
#          "[ERROR] Simulación: módulo ficticio no encontrado.\n"
#
#   5. Atrapa cualquier excepción usando try/except Exception as e
#      alrededor de una línea que intentará convertir "abc" a int.
#      Escribe el mensaje de error en sys.stderr y continúa el programa.
#
#   PARTE C - Validación de tipos con isinstance
#   -----------------------------------------------
#   6. Crea una lista mixta de valores:
#       datos = [42, 3.14, "hola", True, None, [1, 2], (3, 4), {"a": 1}]
#
#   7. Recorre la lista e imprime el tipo de cada elemento usando isinstance
#      para clasificarlos en las siguientes categorías (en este orden):
#       - bool   (verifica ANTES que int, ¿por qué? Explícalo en un comentario)
#       - int
#       - float
#       - str
#       - list
#       - tuple
#       - dict
#       - NoneType (usa type(valor) is type(None))
#       - Desconocido
#
#   Formato de salida:
#       42      → int
#       3.14    → float
#       ...
#
#   PARTE D - Patrón __main__
#   --------------------------
#   8. Al final del archivo coloca toda la lógica de las partes A, B y C
#      dentro del bloque:
#
#       if __name__ == "__main__":
#           ...
#
#   9. Define también una función llamada resumen_sistema() que devuelva
#      (return) un string con el SO y la versión de Python.
#      Esta función debe poder ser importada desde otro módulo sin ejecutar
#      el bloque principal. Verifica que funciona importándola desde la
#      consola interactiva (instrucción en comentario).
#
#   Reto adicional (opcional):
#       Acepta un argumento de línea de comandos --verbose.
#       Si está presente (comprueba con "in sys.argv"), muestra información
#       extra: encoding del sistema, número de CPUs disponibles con os.cpu_count(),
#       y si el script corre en un entorno virtual (comprueba si sys.prefix
#       es distinto de sys.base_prefix).
