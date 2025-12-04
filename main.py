from turtle import clear
from kivy import Config
from kivymd.app import MDApp,Builder
from kivy.core.window import Window
from libs.uix.Root import root
import os
import sys
import json 
from kivy.clock import Clock
from kivy.factory import Factory 
import platform
import sqlite3

os.environ["KIVY_IMAGE"]="pil"
# sys.setrecursionlimit(2000)
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"
Config.set('graphics', 'resizable', False)
Window.size = (310, 620)
Clock.max_iteration = 1000000
root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "libs", "applibs")) 
__version__ = "0.1"
r = Factory.register

with open("factory_registers.json") as fd:
    custom_widgets = json.load(fd)
    for module, _classes in custom_widgets.items():
        for _class in _classes:
            r(_class, module=module)

colors = {
"Green": {
    "50": "000000",
    "100": "000000",
    "200": "000000",
    "300": "000000",
    "400": "000000",#ff4de679
    "500": "002408",#559683
    "600": "000000",
    "700": "000000",
    "800": "fe8700",
    "900": "00cc3f",#00cc3f
    "A100": "000000",
    "A200": "000000",
    "A400": "000000",
    "A700": "000000",
},
"Red": {
    "50": "000000",
    "100": "000000",
    "200": "000000",
    "300": "000000",
    "400": "000000",
    "500": "C6E2FF",
    "600": "000000",
    "700": "000000",
    "800": "000000",
    "900": "00cc3f",
    "A100": "000000",
    "A200": "000000",
    "A400": "000000",
    "A700": "000000",
},
"Light": {
    "StatusBar": "E0E0E0",
    "AppBar": "F5F5F5",
    "Background": "FAFAFA",
    "CardsDialogs": "999999",
    "FlatButtonDown": "cccccc",
},
"Dark": {
    "StatusBar": "000000",
    "AppBar": "212121",
    "Background": "303030",
    "CardsDialogs": "424242",
    "FlatButtonDown": "999999",
    
},
}
conn = sqlite3.connect('assets/DataBases/Contact_data.db')
c = conn.cursor()
c.execute(''' UPDATE CHAT_LIST_DATA
          SET Last_Message = 'Feen a bro'
          WHERE Name = 'youness'
          ''')
conn.commit()
conn.close()

conn = sqlite3.connect('assets/DataBases/Save&Noti.db')
cursor = conn.cursor()
update_query = '''
    CREATE TABLE IF NOT EXISTS Like (
        Ele_Id INTEGER PRIMARY KEY,
        Tab_Name TEXT,
        Message_Id INTEGER,
        Message TEXT,
        Time TEXT
    );
    '''
cursor.execute(update_query)
conn.commit()
conn.close()
# object oriented programming

from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import (
RectangularRippleBehavior,
BackgroundColorBehavior,
CommonElevationBehavior,
)
class ElevBox(MDBoxLayout, CommonElevationBehavior):
    pass

class Box(RectangularRippleBehavior, MDBoxLayout):
    pass
class LoginApplication(MDApp):
    
    def __init__(self, **kwargs):
        super(LoginApplication, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "AsMon"
        self.icon = "assets/images/icon.jpg"
        self.theme_cls.colors = colors
        
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Green"
        self.theme_cls.accent_hue = "900"
        self.theme_cls.theme_style = "Light"
        Window.keyboard_anim_args = {"d": .7, "t": "linear"}
        Window.softinput_mode = "below_target"
        
    def build(self):
        self.root = root()
        # Builder.load_file('libs/uix/kv/root.kv')
        # self.root.set_screen('post','up')
        # self.root.set_screen('post')
        # self.root.get_screen('post').post_data(0)
        # self.root.set_screen('_chat')
        # self.root.get_screen('_chat').load_data()
        self.root.set_screen('info')
        self.root.get_screen('info').strt()
        # return root()
        
   
LoginApplication().run()







'''
"app": {
    "import": "from libs.uix.baseclass.home_screen import HomeScreen",
    "object": "HomeScreen()",
    "kv": "libs/uix/kv/home_screen.kv"
},
"profil": {
    "import": "from libs.uix.baseclass.profil import Profil",
    "object": "Profil()",
    "kv": "libs/uix/kv/profil.kv"
},"settings": {
    "import": "from libs.uix.baseclass.settings_screen import SettingsScreen",
    "object": "SettingsScreen()",
    "kv": "libs/uix/kv/settings_screen.kv"
},
"ntlike": {
    "import": "from libs.uix.baseclass.Noti_Like import NotiLike",
    "object": "NotiLike()",
    "kv": "libs/uix/kv/Noti_Like.kv"
},
'''