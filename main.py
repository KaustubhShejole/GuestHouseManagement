from cProfile import label
from cgitb import text
from faulthandler import disable
from itertools import tee
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.core.window import Window
class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.l1 = Button(
            text="SigInWindow",
            background_color="pink"
        )
        self.l1.bind(on_press = self.button_action)
        self.title = "SignInWindow"
        self.add_widget(self.l1)

    def button_action(self,instance):
        pass
class ThirdWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.l1 = Button(
            text="SigUpWindow",
            background_color="pink"
        )
        self.l1.bind(on_press = self.button_action)
        self.title = "SignUpWindow"
        self.add_widget(self.l1)

    def button_action(self,instance):
        pass
class Manager(ScreenManager):
    pass
kv = Builder.load_file('MyRoot.kv')

class MyRootApp(App):
    def build(self):
        self.title = "Guest House Management System"
        return kv
if __name__ =='__main__':
    MyRootApp().run()