from course.sample.oop.inheritance.models.international_student import InternationalStudent
from course.sample.oop.inheritance.models.person import Person
from course.sample.oop.inheritance.models.student import Student
from course.sample.oop.inheritance.models.subject import Subject
from course.sample.oop.inheritance.models.teacher import Teacher

def printPerson(person: Person):
    print(person)


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

