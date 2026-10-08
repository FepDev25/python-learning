from course.sample.oop.abstractclass.form.form_element import FormElement


class InputForm(FormElement):

    def __init__(self, name: str, type_: str = 'text'):
        super().__init__(name)
        self._type: str = type_

    def draw_html(self) -> str:
        return f'<input type="{self._type}" name="{self._name}" value="{self._value}">'