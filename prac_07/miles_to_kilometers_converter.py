from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

KILOMETERS_CONVERSION = 1.60934


class MilesConverter(App):
    message = StringProperty()

    def build(self):
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('miles_to_kilometers_converter.kv')
        return self.root

    def calculate(self, value):
        value = self.valid_input(value)
        result = value * KILOMETERS_CONVERSION
        self.root.ids.output_label.text = str(result)

    def increment(self, value, change):
        value = self.valid_input(value)
        miles = value + change
        self.root.ids.input_number.text = str(miles)

    def valid_input(self, value):
        try:
            number = float(value)
            return number
        except ValueError:
            return 0.0


MilesConverter().run()
