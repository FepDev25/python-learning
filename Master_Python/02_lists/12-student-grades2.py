
subjects = ['Matematicas', 'Historia', 'Lenguaje']
students_count = 7
grades_by_subject = []

for subject in subjects:
    grades = [float(input(f'Nota {i + 1} {subject}: ')) for i in range(students_count)]
    grades_by_subject.append(grades)

print('Promedios por asignatura:')
subject_average = []
for subject, grades in zip(subjects, grades_by_subject):
    average = sum(grades)/len(grades)
    subject_average.append(average)
    print(f'{subject}: {average:.2f}')

overall_average = sum(subject_average)/len(subject_average)
print(f'Promedio total del curso: {overall_average:.2f}')

try:
    student_id = int(input('Ingrese el identificador de 1 a 7: ')) - 1
    if 0 <= student_id < students_count:
        student_grades = [grades[student_id] for grades in grades_by_subject]
        student_average = sum(student_grades)/len(student_grades)
        print(f'Promedio del alumno Nro: {student_id}: {student_average:.2f}')
    else:
        print('Fuera de Rango!')
except ValueError:
    print('Entrada invalida!. Debe ser un numero entero!')