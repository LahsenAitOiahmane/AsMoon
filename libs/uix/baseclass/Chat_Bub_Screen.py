import random
from turtle import width
from kivy.app import Builder
from kivy.animation import Animation
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex
import json
from kivy.clock import Clock
from kivy.core.window import Window
import datetime
from libs.uix.components.comment import CommentListItem
from libs.uix.components.chat_b import ChatBubble, ImageBub
from libs.uix.Root import root
from kivy.properties import DictProperty, ListProperty, StringProperty, ObjectProperty, NumericProperty, BooleanProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
import sqlite3
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.bottomsheet import MDGridBottomSheet,MDCustomBottomSheet
from kivy.factory import Factory 
from kivymd.utils import asynckivy
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDFlatButton

# Arabic Label will be fixed in the next version thank you
# import arabic_reshaper
# import bidi.algorithm
##########################################################

class Chat_Bub_Screen(MDScreen, ThemableBehavior):

    chatmsgdata = ListProperty()

    def ontext(self,txt):
        # reshaped_text = arabic_reshaper.reshape(txt)
        # bidi_text = bidi.algorithm.get_display(reshaped_text)
        
        
        if self.ids.msg_input.text  !='':
            
            self.ids.sent_msg_button.icon='send-outline'
        else:
            self.ids.sent_msg_button.icon='attachment'
       
    def previous_screen(self):

        self.manager.goto_previous_screen()
        Clock.schedule_once(self.toscrn1,1)
    def toscrn1(self,*args):
        self.ids.msgbox.clear_widgets()
        
    n = 0
    def sent_msg(self,msg):
        # msg = arabic_reshaper.reshape(msg)
        # msg = bidi.algorithm.get_display(reshaped_text)
        
        
        if self.ids.msg_input.text == '':
            self.ids.msgbox.add_widget(MDBoxLayout(
                size_hint_x= None,
                size_hint_y= None,
                width= self.width,
                height = dp(10)
                
            ))
            ImageBub.id = 0
    
            ImageBub.fromMe =self.n
            self.n+=1

            ImageBub.comment = 'What do you think ???'

            ImageBub.time = '00:00 AM'

            # ImageBub.profile_image = 'assets/icons/profile.png'

            ImageBub.image = 'assets/images/sunset.jpg'
    
            ImageBub.read = False
    
            ImageBub.managr = self
                
            self.ids.msgbox.add_widget(ImageBub())
            self.ids.msgbox.add_widget(MDBoxLayout(
                size_hint_x= None,
                size_hint_y= None,
                width= self.width,
                height = dp(10)
                ))
            
        else :
            self.load_data(msg)
            self.ids.msg_input.text = ''
    prv = False
    # nxt = False
    
    def load_data(self,msg=''):
        self.ids.mbox.md_bg_color = [0,0,0,0]
        # self.ids.list.remove_widget(ChatBubble())
        # self.prv = False
        
        if msg != '':
            
            ChatBubble.text = msg
            ChatBubble.send_by_user =True
            ChatBubble.time = '00:00 PM'
            ChatBubble.myself = self
            if self.prv == True :
                ChatBubble.fromthesame = True
            else :
                ChatBubble.fromthesame = False
            # if  self.nxt == False:
            #     ChatBubble.nextsame = True
            # else:
            #     ChatBubble.nextsame = False
            # self.nxt = True
            self.prv = True
            self.ids.msgbox.add_widget(ChatBubble())
                
            self.chatmsgdata.append({'text':msg,'send_by_user': True,'time': '00:00 AM', 'selfwidth':self})
        else:
            self.chatmsgdata = [{'text':"Hello",'send_by_user': False,'time': '00:00 AM', 'selfwidth':self},
                            {'text':"Hi how are you dada it's been a long time ago we talk",'send_by_user': False,'time' : '00:00 AM', 'selfwidth':self},
                            {'text':"yess ",'send_by_user': True,'time': '00:00 AM', 'selfwidth':self},
                            {'text':"Hi how are you dada its been",'send_by_user': True,'time' : '00:00 AM', 'selfwidth':self},
                            
                            {'text':"i'm good and you",'send_by_user': False,'time': '00:00 AM', 'selfwidth':self}
                            ]
            l=len(self.chatmsgdata)
            for i in range(l):
                ChatBubble.text = self.chatmsgdata[i]['text']
                ChatBubble.send_by_user = self.chatmsgdata[i]['send_by_user']
                ChatBubble.time = self.chatmsgdata[i]['time']
                ChatBubble.myself = self
                ChatBubble.fromthesame = False
                ChatBubble.nextsame = False
                if i > 0:
                    if self.chatmsgdata[i]['send_by_user'] == self.chatmsgdata[i-1]['send_by_user']:
                        ChatBubble.fromthesame = True
                    else:
                        ChatBubble.fromthesame = False
                if i < l-2 :
                    if  self.chatmsgdata[i]['send_by_user'] == self.chatmsgdata[i+1]['send_by_user']:
                            ChatBubble.nextsame = True
                    else:
                        ChatBubble.nextsame = False
                    
                
                self.ids.msgbox.add_widget(ChatBubble())
            

