try:
    divisor = int(input('ingrese un numero divisor: '))
    division = 10/divisor
    print('division=', division)
except (ValueError, ZeroDivisionError) as e:
    print('Ocurrio un problema: ', e)
finally:
    print('es opcional, pero se ejecuta siempre con el error o si todo sale bien!')

print('Continuamos con el flujo normal de la app!')