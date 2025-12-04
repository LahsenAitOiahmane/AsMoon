from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.utils import get_hex_from_color, get_color_from_hex
#import kivymd_extensions.akivymd.uix.selectionlist
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.screen import MDScreen
from kivy.properties import DictProperty, ListProperty, StringProperty, ObjectProperty, NumericProperty, BooleanProperty
class Container(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True

class Profil(MDScreen):
    name = StringProperty()
    image = StringProperty()
    gmail = StringProperty()
    def load_data(self, name, image, gmail):
        self.name = name
        self.image = image
        self.gamil = gmail
    def go_to_pre_scr(self):
        
        self.manager.goto_previous_screen()