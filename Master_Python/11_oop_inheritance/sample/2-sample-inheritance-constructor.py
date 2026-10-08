from course.sample.oop.inheritance.models.international_student import InternationalStudent
from course.sample.oop.inheritance.models.person import Person
from course.sample.oop.inheritance.models.student import Student
from course.sample.oop.inheritance.models.subject import Subject
from course.sample.oop.inheritance.models.teacher import Teacher

def printPerson(person: Person):

    print('Impriendo datos en comun del tipo Persona:')
    print(f'Nombre: {person.first_name}, apellido: {person.last_name}, email: {person.email}')

    if isinstance(person, Student):
        print('Impriendo datos del tipo Student:')
        print(f'Institucion: {person.institution}')
        print(f'Nota Matematicas: {person.math_grade}')
        print(f'Nota Historia: {person.history_grade}')
        print(f'Nota Lenguaje: {person.language_grade}')

        if isinstance(person, InternationalStudent):
            print('Imprimiendo los datos del tipo estudiante Internacional:')
            print(f'Nota idiomas: {person.foreign_language_grade}')
            print(f'Pais:  {person.country}')
        print('============================ sobre escritura metodo calculate_average ============================')
        print(f'Promedio: {person.calculate_average():.2f}')
        print('============================ sobre escritura metodo write_blackboard ============================')
        print(person.write_blackboard())

    if isinstance(person, Teacher):
        print('Imprimiendo los datos del tipo Teacher: ')
        print(f'Asignatura: {person.subject}')

    print('============================ sobre escritura metodo greet ============================')
    print(person.greet())
    print('============================ sobre escritura metodo speek ============================')
    print(person.speak())

student = Student('Andres', 'Guzman')
student.email = 'andres@correo.com'
student.institution = 'Instituto Nacional'
student.language_grade = 9.00
student.history_grade = 7.85
student.math_grade = 8.3

international_student = InternationalStudent('John', 'Doe', 'peter@correo.com',
                                             'Instituto Internacional',
                                             8.00, 6.00, 10,
                                             'Australia',
                                             8.97)

teacher = Teacher('Maria', 'Roe', 'profe@correo.com', Subject.FISICA)

persons = [student, international_student, teacher]
for p in persons:
    printPerson(p)
    print('==================================================')

# print('Estudiante', student.first_name, student.last_name, student.email, student.institution)
# print(f'Profesor {teacher.first_name} {teacher.last_name}: {teacher.subject.value}')
