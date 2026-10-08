from course.sample.oop.abstractclass.form.form_element import FormElement

class TextareaForm(FormElement):

    def __init__(self, name: str, rows: int = 4, cols: int = 6):
        super().__init__(name)
        self.rows: int = rows
        self.cols: int = cols

    def draw_html(self) -> str:
        return (f'<textarea '
                f'name="{self._name}" '
                f'cols="{self.cols}" '
                f'rows="{self.rows}">'
                f'{self._value}'
                f'</textarea>')

