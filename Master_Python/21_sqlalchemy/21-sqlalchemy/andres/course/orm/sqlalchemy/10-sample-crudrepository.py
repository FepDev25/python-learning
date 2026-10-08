from andres.course.orm.sqlalchemy.config.db import SessionLocal
from andres.course.orm.sqlalchemy.mapped.person import Person
from andres.course.orm.sqlalchemy.repositories.person_repository import PersonRepository

# -------------------------
# Ejemplo de uso (main)
# -------------------------
if __name__ == "__main__":
    repo = PersonRepository(SessionLocal)

    # 1) CREATE (save -> insert)
    print("== CREATE ==")
    p = Person(name="Juan", lastname="Pérez", email="juan.perez@example.com", age=30)
    try:
        p = repo.save(p)
        print("Creado:", p)
    except Exception as e:
        print("Error al crear:", e)

    # 2) READ ALL
    print("\n== FIND ALL ==")
    try:
        for person in repo.find_all():
            print(person)
    except Exception as e:
        print("Error al listar:", e)

    # 3) UPDATE (save -> update)
    print("\n== UPDATE ==")
    try:
        if p.id:
            p.age = 31
            p.name = "Juan Carlos"
            p = repo.save(p)
            print("Actualizado:", p)
        else:
            print("No hay id para actualizar.")
    except Exception as e:
        print("Error al actualizar:", e)

    # 4) DELETE
    print("\n== DELETE ==")
    try:
        ok = repo.remove(p.id if p.id else -1)
        print("Eliminado?" , ok)
    except Exception as e:
        print("Error al eliminar:", e)

    # Confirmación final
    print("\n== FIND ALL (final) ==")
    try:
        for person in repo.find_all():
            print(person)
    except Exception as e:
        print("Error al listar final:", e)