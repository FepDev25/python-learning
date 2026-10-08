class Vehicle:

    def __init__(self, *args, **kwargs):
        self.manufacturer = None
        self.model = None
        self.color = None
        self.cylinder = None
        self.tank_capacity = None

        arg_names = ['manufacturer', 'model', 'color', 'cylinder', 'tank_capacity']
        for name, value in zip(arg_names, args):
            setattr(self, name, value)

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in arg_names:
                    setattr(self, key, value)
                else:
                    raise TypeError(f'Argumento desconocido: {key}')
            # if 'manufacturer' in arg_names:
            #     self.manufacturer = kwargs.get('manufacturer')
            # if 'model' in arg_names:
            #     self.model = kwargs.get('model')
            # if 'color' in arg_names:
            #     self.color = kwargs.get('color')
            # if 'cylinder' in arg_names:
            #     self.cylinder = kwargs.get('cylinder')
            # if 'tank_capacity' in arg_names:
            #     self.tank_capacity = kwargs.get('tank_capacity')

        # total = len(args)
        #
        # if total == 0:
        #     pass
        # elif total == 1:
        #     self.manufacturer = args[0]
        # elif total == 2:
        #     self.manufacturer, self.model = args
        # elif total == 3:
        #     self.manufacturer, self.model, self.color = args
        # elif total == 4:
        #     self.manufacturer, self.model, self.color, self.cylinder = args
        # elif total == 5:
        #     self.manufacturer, self.model, self.color, self.cylinder, self.tank_capacity = args
        # else:
        #     raise TypeError(f'Invalida cantidad de argumentos: esperado 0 - 5, fueron {total}')

    def __str__(self):
        return f'Car(manufacturer={self.manufacturer}, model={self.model}, color={self.color}, cylinder={self.cylinder}, tank={self.tank_capacity})'
