from datetime import datetime
import sys

sys.stdout.write('Hola Mundo desde std out!\n')
# sys.stderr.write('Hola tenemos un problema de error!\n')
print('Hola Mundo!')

try:
    date_event = datetime.strptime('2026-09-18', '%Y-%m-%d')
    print(date_event)
except ValueError as err:
    sys.stderr.write(f'Error con el formato de fecha {err}\n')
    sys.exit(1)

print('Otra tarea a ejecutar!')
sys.exit(0)
