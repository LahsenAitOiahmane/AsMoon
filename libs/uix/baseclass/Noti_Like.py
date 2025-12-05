from kivymd.uix.screen import MDScreen
import json
from kivy.properties import ListProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

# import utils


class NotiLike(MDScreen):
    
    def on_tab_switch(self, *args):
        if args[3] == "[b]CHATS[/b]":
            self.ids.float_btn.icon = "message"
        elif args[3] == "[b]STATUS[/b]":
            self.ids.float_btn.icon = "camera"
        elif args[3] == "[b]CALLS[/b]":
            self.ids.float_btn.icon = "phone-plus"





class StatusTab(FloatLayout, MDTabsBase):
    pass



class ChatsTab(FloatLayout, MDTabsBase):

    users_data = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open("assets/users.json") as f:
            data = json.load(f)

        for i in data:
            user_data = {
                "text": i,
                "secondary_text": data[i]["message"],
                "time": data[i]["time"],
                "image": data[i]["image"],
            }
            self.users_data.append(user_data)
