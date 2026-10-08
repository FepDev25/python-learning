from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    Clase base abstracta (Interfaz) que define operaciones comunes
    para archivos y directorios.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def show(self, level: int = 0):
        """Muestra el nombre del componente con una indentación."""
        pass

    @abstractmethod
    def search(self, name: str) -> bool:
        """Busca un componente por nombre y devuelve True si lo encuentra."""
        pass

class File(Component):
    """
    Clase 'Hoja' que representa un archivo. No tiene hijos.
    """

    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def show(self, level: int = 0):
        indent = "  " * level
        print(f"{indent}📄 {self.name} ({self.size} KB)")

    def search(self, name: str) -> bool:
        """En un archivo, la búsqueda solo comprueba su propio nombre."""
        return self.name == name

class Directory(Component):
    """
    Clase 'Composite' que representa un directorio.
    Puede contener componentes hijos (archivos u otros directorios).
    """

    def __init__(self, name: str):
        super().__init__(name)
        self._children: List[Component] = []

    def add(self, component: Component):
        """Añade un componente (archivo o directorio) a este directorio."""
        self._children.append(component)

    def remove(self, component: Component):
        """Elimina un componente de este directorio."""
        self._children.remove(component)

    def show(self, level: int = 0):
        """
        Muestra el nombre del directorio y luego llama recursivamente a 'show'
        en cada uno de sus hijos con mayor indentación.
        """
        indent = "  " * level
        print(f"{indent}📁 {self.name}/")
        for child in self._children:
            child.show(level + 1)

    def search(self, name: str) -> bool:
        """
        Comprueba si el nombre del directorio actual coincide. Si no,
        llama recursivamente a 'search' en cada hijo.
        """
        # Primero, comprueba si el nombre del directorio actual es el que buscamos
        if self.name == name:
            return True

        # Si no, busca en cada uno de los hijos
        for child in self._children:
            if child.search(name):
                return True  # Si un hijo lo encuentra, devolvemos True inmediatamente

        # Si el bucle termina y ningún hijo lo encontró, devolvemos False
        return False

# --- Creación y uso de la estructura ---

if __name__ == "__main__":
    # 1. Crear el directorio raíz
    root = Directory("Documentos")

    # 2. Crear subdirectorios
    work_dir = Directory("Trabajo")
    personal_dir = Directory("Personal")
    projects_dir = Directory("Proyectos")

    # 3. Añadir subdirectorios a la raíz
    root.add(work_dir)
    root.add(personal_dir)

    # 4. Añadir archivos y directorios a 'Trabajo'
    work_dir.add(File("reporte_anual.docx", 120))
    work_dir.add(File("presentacion.pptx", 350))
    work_dir.add(projects_dir)  # Anidamos 'Proyectos' dentro de 'Trabajo'

    # 5. Añadir archivos a 'Proyectos'
    projects_dir.add(File("diagrama_arquitectura.png", 80))
    projects_dir.add(File("main.py", 15))

    # 6. Añadir archivos a 'Personal'
    personal_dir.add(File("foto_vacaciones.jpg", 2500))
    personal_dir.add(File("lista_compras.txt", 2))

    # 7. Crear y añadir un archivo directamente en la raíz
    root.add(File("notas_generales.txt", 5))

    # 8. Mostrar toda la estructura desde la raíz
    print("Estructura del sistema de archivos:")
    root.show()

    print("\n" + "=" * 30)
    print("🔎 Realizando búsquedas...")
    print("=" * 30)

    # 9. Ejemplos de búsqueda
    search_terms = [
        "Proyectos",  # Un directorio anidado
        "main.py",  # Un archivo muy anidado
        "foto_vacaciones.jpg",  # Un archivo en otra rama
        "Documentos",  # El propio directorio raíz
        "archivo_inexistente.zip"  # Un archivo que no existe
    ]

    for term in search_terms:
        # Iniciamos la búsqueda siempre desde el directorio raíz 'root'
        found = root.search(term)
        print(f"¿Se encontró '{term}'? -> {'Sí ✅' if found else 'No ❌'}")