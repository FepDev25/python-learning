from typing import cast, List

from course.sample.oop.inheritance.models.person import Person
from course.sample.oop.inheritance.models.student import Student
from course.sample.oop.inheritance.models.subject import Subject
from course.sample.oop.inheritance.models.teacher import Teacher

student: Person = Student()
student.first_name = 'Andres'
student.last_name = 'Guzman'
student.email = 'correo@email.com'
alumno = cast(Student, student)
alumno.institution = 'Universidad'

teacher = Teacher()
teacher.first_name = 'Maria'
teacher.last_name = 'Roe'
teacher.email = 'profe@correo.com'
teacher.subject = Subject.FISICA

print('Estudiante', student.first_name, student.last_name, student.email, student.institution)

print(f'Profesor {teacher.first_name} {teacher.last_name}: {teacher.subject.value}')

student.speak()
alumno.write_blackboard()
student.write_blackboard()
alumno.speak()

print(isinstance(student, Person))
print(isinstance(alumno, Person))
print(isinstance(teacher, Person))
print(isinstance(teacher, Student))

persons: List[Person] = [student, teacher]

for p in persons:
    if isinstance(p, Student):
        p.write_blackboard()
    else:
        print('No es alumno')