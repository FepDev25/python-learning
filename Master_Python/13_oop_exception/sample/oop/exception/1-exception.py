try:
    divisor = int(input('ingrese un numero divisor: '))
    division = 10/divisor
    print('division=', division)
except ValueError as e:
    print('Se detecto un excepcion: ingrese un valor numerico valido:', e)
except ZeroDivisionError as e:
    print('Capturamos la excepcion en tiempo de ejecucion:', e)
except Exception as e:
    print('Ocurrio otro error!')

finally:
    print('es opcional, pero se ejecuta siempre con el error o si todo sale bien!')

print('Continuamos con el flujo normal de la app!')