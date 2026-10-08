from course.sample.oop.abstractclass.form.input_form import InputForm
from course.sample.oop.abstractclass.form.select_form import SelectForm, Option
from course.sample.oop.abstractclass.form.textarea_form import TextareaForm
from course.sample.oop.abstractclass.validator.email_validator import EmailValidator
from course.sample.oop.abstractclass.validator.length_validator import LengthValidator
from course.sample.oop.abstractclass.validator.not_none_validator import NotNoneValidator
from course.sample.oop.abstractclass.validator.number_validator import NumberValidator
from course.sample.oop.abstractclass.validator.required_validator import RequiredValidator

username = InputForm('username')
username.add_validator(RequiredValidator())

password = InputForm('password', 'password')
password.add_validator(RequiredValidator())
password.add_validator(LengthValidator(6, 12))
email = InputForm('email', 'email')
email.add_validator(RequiredValidator())
email.add_validator(EmailValidator())
age = InputForm('age', 'number')
age.add_validator(NumberValidator())
experience = TextareaForm('experience', 5, 9)

programming = SelectForm('programming')
programming.add_validator(NotNoneValidator())
programming.add_option(Option('1', 'Java'))

programming.add_option(Option('2', 'Python').set_selected())
programming.add_option(Option('3', 'JavaScript'))
programming.add_option(Option('4', 'TypeScript'))

username.set_value('johndoe')
password.set_value('fjasljdo1212')
email.set_value('john.doe@correo.es')
age.set_value('25')
experience.set_value('Hola tengo mas de 20 años de experiencia ...')

elements = [
    username,
    password,
    email,
    age,
    experience,
    programming
]

for e in elements:
    print(e.draw_html())
    print('<br>')

print('# Validando y mostrando errores en los elementos del formulario:')
for e in elements:
    if not e.is_valid():
        for err in e.errors:
            print(err)