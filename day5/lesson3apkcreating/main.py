#from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
# from kivy.config import Config
from kivymd.app import MDApp
# from kivymd.theming import ThemeManager
#
# Config.set('kivy', 'keyboard_mode', 'systemanddock')
from kivy.lang import Builder
Window.size = (360, 640)

Builder.load_string('''

<MyOwnLabel@MDLabel>
    font_size: '25sp'
    halign: 'left'
    valign: 'middle'
    text_size: self.size



<Container>
    rows: 3
    inputs: text_input
    hours: label_hours
    minutes: label_minutes
    seconds: label_seconds
    mseconds: label_mseconds
    weeks: label_weeks

    AnchorLayout:
        anchor_y: 'top'
        size_hint: 1,0.15
        padding: 30

        MDTextField:
            id: text_input
            text: ''
            font_size: '45sp'
            input_filter: 'int'
            input_type: 'number'
            multiline: False
            hint_text: "Введите число"

    GridLayout:
        cols: 2
        padding: [20, 0, 0, 0]


        BoxLayout:
            orientation: 'vertical'
            MyOwnLabel:
                text: 'Часы'

            MyOwnLabel:
                text: 'Минуты'

            MyOwnLabel:
                text: 'Секунды'

            MyOwnLabel:
                text: 'МилиСекунды'

            MyOwnLabel:
                text: 'Недели'

        BoxLayout:
            size_hint: 0.5, 1
            orientation: 'vertical'
            MyOwnLabel:
                text: '0'
                id: label_hours

            MyOwnLabel:
                text: '0'
                id: label_minutes

            MyOwnLabel:
                text: '0'
                id: label_seconds

            MyOwnLabel:
                text: '0'
                id: label_mseconds

            MyOwnLabel:
                text: '0'
                id: label_weeks

    BoxLayout:
        size_hint: 0.9, 0.15
        pos_hint: {'x':0.5, 'y': 0}
        padding: [30, 20, 30, 20]
        MDRaisedButton:
            text: 'Convert dat time'
            font_size: '25sp'
            on_release:
                root.convert()

''')

class Container(GridLayout):
    def convert(self):
        try:
            number = int(self.inputs.text)
        except Exception:
            number = 0
        self.hours.text = str(number*24)
        self.minutes.text = str(number * 24*60)
        self.seconds.text = str(number * 24*60*60)
        self.mseconds.text = str(number * 24*60*60*60)
        try:
            self.weeks.text = str(number//7)
        except Exception:
            self.weeks.text = 'Ошибка'

class TConverterApp(MDApp):

    def __init__(self, **kwargs):
        self.title = "itproger"
        self.theme_cls.theme_style = "Light"
        super().__init__(**kwargs)

    def build(self):
        return Container()

if __name__ == '__main__':
    TConverterApp().run()