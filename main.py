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
num_floors=[0]
def init_rooms():
    with open('rooms.txt','w') as tf:
        for i in range(5):
            print('1 22',file=tf)
init_rooms()
l=[]
def get_rooms():
    with open('rooms.txt','r') as tf:
        for each_line in tf:
            [i,j]=(each_line.split(' ',1))
            i=int(i)
            j=int(j)
            l.append([i,j])
get_rooms()
free_floor=[]
def check_rooms():
    if(l!= [[],[],[],[],[]] and l!=[]):
        free_floor=[]
        i=1
        for each_list in l:
            if(each_list != []):
                free_floor.append(i)
                print(i)
            i=i+1
        num_floors[0] = i-1
        return str(free_floor).strip('[]')
    else:
        return ''

class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    def info_text(self):
        s = check_rooms()
        if(s != ''):
            return s+' Floors are available'
        else:
            return 'Floors are not available'
    def check_floors(self,n):
        if(n>=1 and n<=num_floors[0]):
            for each_item in free_floor:
                if n == each_item:
                    print('ki')
                    return 'green'
            return 'red'
        return 'red'
class ThirdWindow(Screen):
    pass
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