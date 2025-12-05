import json
from kivy.app import Builder

from kivy.clock import Clock
from kivy.factory import Factory  # NOQA: F401
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.core.window import Window
# from kivymd.utils import asynckivy

from libs.uix.baseclass.post_screen import PostScreen
class root(ScreenManager):
    previous_screen = {'name':'','side':''}
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self._goto_previous_screen)
        with open("first_screens.json") as f:
            self.screens_data = json.load(f)
            for screen_name in self.screens_data:
                screen = self.screens_data[screen_name]
                Builder.load_file(screen["kv"])

                ns = {}
                exec(screen["import"], ns)
                screen_object = eval(screen["object"], ns)
                screen_object.name = screen_name
                self.add_widget(screen_object)
        self.set_screen('info')
        self.get_screen('info').strt()
    def set_screen(self, screen_name, side='left', quick=False):
    
        if not self.has_screen(screen_name):
            screen = self.screens_data[screen_name]
            Builder.load_file(screen["kv"])

            ns = {}
            exec(screen["import"], ns)
            screen_object = eval(screen["object"], ns)
            screen_object.name = screen_name
            self.add_widget(screen_object)
        
        
        
        self.previous_screen = {"name": self.current, "side": side}
        # self.transition.direction = side
        self.transition.duration = 0 if quick else .5
        self.transition.direction = side#FadeTransition()
        self.current = screen_name
        
        
        
    def to_ch(self,*args):
        # if self.previous_screen['name'] == 'post':
        #     for widget in PostScreen.lst:
        #         PostScreen().ids.lstt.remove_widget(widget)
        #     PostScreen.lst = []
        pass
        
        
    def _goto_previous_screen(self, instance, key, *args):
        if key == 27:
            self.goto_previous_screen()
            return True
        return False

    def goto_previous_screen(self):
        if self.previous_screen:
            
            self.set_screen(
                self.previous_screen["name"],
                side="right"
                if self.previous_screen["side"] == "left"
                else "left" 
                if self.previous_screen["side"] == "right"
                else "up"
                if self.previous_screen["side"] == "down"
                else "down",
            )
        # Clock.schedule_once(self.to_ch, 1)

     
