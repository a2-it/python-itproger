from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Container(BoxLayout):
    texts = ObjectProperty
    labels = ObjectProperty

    def changes(self):
        self.labels.text = self.texts.text

class DuckyApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    DuckyApp().run()












#////////////////////////////////////////////////////////////////////
# from lesson 1
# class DuckyApp(App):
#     def build(self):
#         box = BoxLayout()
#         b1 = Button(text='Привет Всем')
#         box.add_widget(b1)
#         box.add_widget(Button(text='Привет Всем2'))
#         return box
#
# if __name__ == '__main__':
#     DuckyApp().run()
#//////////////////////////////////////////////////////////////////////