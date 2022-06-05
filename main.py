from cProfile import label
from cgitb import text
from faulthandler import disable
from itertools import tee
from unicodedata import name
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
from kivymd.app import MDApp
from kivy.uix.image import Image, AsyncImage
from kivy.graphics import Color, Rectangle
class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class ThirdWindow(Screen):
    '''def validate(self):
        pname=ObjectProperty('')
        number=ObjectProperty(None)
        aadhar=ObjectProperty(None)
        address=ObjectProperty(None)
        if(str(pname).strip()!='' and str(pname).strip()!='<ObjectProperty name=>'):
            print(str(pname).strip())
            return True
        else:
            return False'''
class Manager(ScreenManager):
    pass
kv = Builder.load_file('MyRoot.kv')

class MyRootApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Blue"
        self.title = "Guest House Management System"
        return kv
if __name__ =='__main__':
    MyRootApp().run()