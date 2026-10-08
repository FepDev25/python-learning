from pathlib import Path

class FileService:

    def create(self, name: str):
        file = Path(name)

        try:
            with open(file, 'a', encoding='utf-8') as writer:
                writer.write('Hola que tal amigo!\n')
                writer.write('Todo bien? yo aca escribiendo textos en un archivo...\n')
                writer.write('Hasta luego Lucas!\n')
            print(f'El archivo se ha creado con exito: {name}')

        except IOError as e:
            print(f"Error: {e}")

    def read(self, name: str) -> str:
        sb = []
        file = Path(name)
        try:
            with open(file, 'r', encoding='utf-8') as reader:
                for line in reader:
                    sb.append(line)
        except IOError as e:
            print('Error', e)

        return "".join(sb)
