from course.sample.oop.abstractclass.form.form_element import FormElement

class Option:
    def __init__(self, value: str = None, name: str = None):
        self.value = value
        self.name = name
        self.selected = False

    def set_selected(self) -> 'Option':
        self.selected = True
        return self

class SelectForm(FormElement):

    def __init__(self, name: str, options: list[Option] | None = None):
        super().__init__(name)
        self.options = options if options is not None else []

    def add_option(self, option: Option):
        self.options.append(option)

    def draw_html(self) -> str:
        html = f'<select name="{self._name}">'
        for option in self.options:
            selected_attr = ''
            if option.selected:
                selected_attr = 'selected'
                self._value = option.value

            html += f'\n<option value="{option.value}" {selected_attr}>{option.name}</option>'
        html += '</select>'
        return html