from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

labels = ["One", "Two", "Three", "Four"]


class DynamicLabel(App):

    def build(self):
        self.title = "Create dynamic label from a list"
        self.root = Builder.load_file('dynamic_label.kv')
        self.generate_label()
        return self.root

    def generate_label(self):
        for label in labels:
            temp_label = Label(text=label)
            self.root.ids.label_box.add_widget(temp_label)


DynamicLabel().run()
