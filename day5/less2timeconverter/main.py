from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'systemanddock')
Window.size = (360, 640)



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

class TConverterApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    TConverterApp().run()