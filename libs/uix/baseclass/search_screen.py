from kivy.animation import Animation
from kivy.properties import DictProperty, ListProperty, StringProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivy.lang import Builder
import json



class Search(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def on_start(self):
        self.ids.txtfield.focus = True
    def to_home_screen(self):
        self.manager.set_screen("info",'up')