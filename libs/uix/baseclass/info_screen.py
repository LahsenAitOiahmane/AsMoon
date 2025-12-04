import random
from time import time
from kivy.app import Builder
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.clock import Clock
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ButtonBehavior

from kivymd.uix.label import MDLabel
from kivy.animation import Animation
from kivymd.uix.screen import MDScreen
# from questionary import password
# from libs.uix.Root import root
import json
from kivy.uix.screenmanager import ScreenManager

from ast import Lambda
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, NumericProperty, StringProperty, BooleanProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.relativelayout import MDRelativeLayout
# from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.button import MDIconButton
from kivy.utils import get_color_from_hex
# import akivymd.uix.bottomnavigation2
from kivy.animation import Animation
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
# from kivymd.uix.tab import MDTabsBase
import datetime
import sqlite3,json
# from kivymd.utils import asynckivy

from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from libs.uix.components.hori_bub import PostItem
class SelectableRecycleGridLayout(
    FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout
):
    pass



current_screen = StringProperty('home')    
class InfoScreen(MDScreen):
    users_chat = ListProperty()
    postdata = ListProperty()
    def to_chat_bub(self,id):
        
        Clock.schedule_once(self.toscrn,.5)
        
    def toscrn(self,*args):
        self.manager.set_screen('_chat','up')
        self.manager.get_screen('_chat').load_data()
        # Clock.schedule_once(self.toscrn3,0)
    def toscrn3(self,*args):
        pass
    def strt(self):
        self.scroly=self.ids.scrovw.scroll_y
        self.scroly1=self.ids.scrovw1.scroll_y
        self.scrolymax=self.ids.scrovw.scroll_y
        self.scrolymax1=self.ids.scrovw1.scroll_y
        self.current_screen = 'home'
        self.bxy = self.ids.searchbxlay.y
        self.screen = 'home'
        self.home=True
        self.users_data = []
        self.postdata = []
        self.users_chat=[]
        self.load_data()
        print('yess')
    def load_data(self):
        txt = "Hello freinds it is my first time here and I'm so glad that I have this opportinity to share my thoughts and also to learn more in this platforme. thank you"
        txxt = f"[font=assets/fonts/Lexend-Regular.ttf]{txt}[/font]"
        # t=''
        # for i in range(len(txt)):
        #     t+=txt[i].upper()
        # txt = t
        t=''
        l = len(txt)
        ll=0
        if l >= 109:
            l = 109
            ll=100
        
            for i in range(l):
                if i <= ll:
                    t += txt[i]
                else:
                    if txt[i]==' ':
                    
                        break
                    
                    else:
                        t += txt[i]
        
            t=f"[font=assets/fonts/Lexend-Regular.ttf]{t}[/font]"
            t+='    [color=#416d6d] [i]see more...[/i] [/color]'
            txt = t 
        else:
            txt=f"[font=assets/fonts/Lexend-Regular.ttf]{txt}[/font]"

        self.postdata = [{'id':1,'fname':' lahsen wahmane','date':'08/09/2022','likes':25,'coments':145,'profile_image':'assets/icons/profile.png','image':'assets/images/sunset.jpg', 'liked':False,  'txxt':txt, 'txtt':txxt,'managr':self},
                 {'id':2,'fname':'Mouad Ait Oihmane','date':'08/09/2023','likes':5,'coments':295,'profile_image':'assets/icons/profile.png','image':'assets/images/peakpx.jpg', 'liked':False, 'txxt':txt,'txtt':txxt,'managr':self},
                 {'id':3,'fname':'youssef Ait Oihmane','date':'02/02/2021','likes':1345,'coments':224,'profile_image':'assets/icons/profile.png','image':'assets/images/bgpic.png', 'liked':False,'txxt':txt,'txtt':txxt,'managr':self},
                 {'id':5,'fname':'Mikell sco','date':'08/09/2024','likes':20,'coments':59,'profile_image':'assets/icons/profile.png','image':'assets/images/img.jfif','liked':False, 'txxt':txt,'txtt':txxt,'managr':self},
                 {'id':6,'fname':'cr7','date':'08/09/2422','likes':295,'coments':15,'profile_image':'assets/icons/profile.png','image':'assets/images/peakpx.jpg','liked':False, 'txxt':txt,'txtt':txxt,'managr':self},
                 {'id':7,'fname':'smiya o lkneya','date':'08/09/5022','likes':805,'coments':65,'profile_image':'assets/icons/profile.png','image':'assets/images/bgpic.png','liked':True, 'txxt':txt,'txtt':txxt,'managr':self},
                 {'id':8,'fname':'wali bda','date':'08/09/6022','likes':85,'coments':55,'profile_image':'assets/icons/profile.png','image':'','liked':False, 'txxt':txt,'txtt':txxt,'managr':self},
                 {'id':9,'fname':'hhhhhhh','date':'08/09/222','likes':45,'coments':25,'profile_image':'assets/icons/profile.png','image':'assets/images/peakpx.jpg','liked':False, 'txxt':txt,'txtt':txxt,'managr':self},
                 {'id':10,'fname':'l9wada','date':'08/09/2722','likes':275,'coments':23,'profile_image':'assets/icons/profile.png','image':'assets/images/bgpic.png','liked':False,'txxt':txt,'txtt':txxt,'managr':self}
                ]

       
        l=len(self.postdata)
        for i in range(l):
            PostItem.id= self.postdata[i]['id']
            PostItem.fname=self.postdata[i]['fname']
            PostItem.date=self.postdata[i]['date']
            PostItem.likes=self.postdata[i]['likes']
            PostItem.coments=self.postdata[i]['coments']
            PostItem.profile_image=self.postdata[i]['profile_image']
            PostItem.image=self.postdata[i]['image']
            PostItem.liked =self.postdata[i]['liked']
            PostItem.txxt = self.postdata[i]['txxt']
            PostItem.txt = self.postdata[i]['txtt']
            PostItem.managr = self.postdata[i]['managr']
            
            self.ids.list1.add_widget(PostItem())
            
  
        
        
        with open("assets/groups.json") as g:
            self.grps_data = json.load(g)

        for i in self.grps_data:
            grp_data = {
                "id":1,
                "name": i,
                "last_msg": self.grps_data[i]["message"],
                "time": self.grps_data[i]["time"],
                "image": self.grps_data[i]["image"],
                "read":True,
                "on_press":lambda x=2:self.to_chat_bub(x)
                
            }
            for j in range(1):
                self.users_chat.append(grp_data)
        
    def on_start(self):
        self.to_screen('chat')
    def move1(self):
        
        if self.ids.scrovw1.scroll_y < self.scroly1 or self.ids.scrovw1.scroll_y==0:
            Animation2=Animation(y=-self.ids.botombar.height,d=.1)
            Animation2.start(self.ids.botombar)
            Animation2=Animation(y=-self.ids.line.height,d=.1)
            Animation2.start(self.ids.line) 
            Animation2=Animation(y=-self.ids.lin.height,d=.1)
            Animation2.start(self.ids.lin) 
            self.scroly1=self.ids.scrovw1.scroll_y 
        
            
        else:
            Animation1=Animation(y=0,d=.1)
            Animation1.start(self.ids.lin)
            Animation1=Animation(y=0,d=.1)
            Animation1.start(self.ids.botombar)
            Animation1=Animation(y=dp(39),d=.1)
            Animation1.start(self.ids.line) 
            self.scroly1=self.ids.scrovw1.scroll_y 
    def move(self):
            
        if self.ids.scrovw.scroll_y < self.scroly or self.ids.scrovw.scroll_y==0:
            Animation2=Animation(y=-self.ids.botombar.height,d=.1)
            Animation2.start(self.ids.botombar)
            Animation2=Animation(y=-self.ids.line.height,d=.1)
            Animation2.start(self.ids.line) 
            Animation2=Animation(y=-self.ids.lin.height,d=.1)
            Animation2.start(self.ids.lin) 
            # self.ids.profile_bar.elevation = 2
            # Animation(elevaltion = 2, d=1,t='in_out_quart').start(self.ids.profile_bar)
            self.scroly=self.ids.scrovw.scroll_y 
        
            
        else:
            Animation1=Animation(y=0,d=.1)
            Animation1.start(self.ids.lin)
            Animation1=Animation(y=0,d=.1)
            Animation1.start(self.ids.botombar)
            Animation1=Animation(y=dp(39),d=.1)
            Animation1.start(self.ids.line) 
            self.scroly=self.ids.scrovw.scroll_y 
        
        if self.ids.scrovw.scroll_y < self.scrolymax and self.home:
            Animation(x=self.width+dp(5),d=1).start(self.ids.searchbxlay)
            Animation(height = self.ids.boxsc.height ,d=1,t='in_out_quart').start(self.ids.mainpost)
            Animation(height = dp(65) ,d=1,t='in_out_quart').start(self.ids.space)
            
        elif self.ids.scrovw.scroll_y >= self.scrolymax-dp(100) and self.home:
            Animation(x=self.width - self.ids.searchbx.width/2 ,d=1).start(self.ids.searchbxlay)
            # Animation(elevaltion = 0, d=1,t='in_out_quart').start(self.ids.profile_bar)
            # self.ids.profile_bar.elevation = 0
            Animation(height = self.ids.boxsc.height-dp(60) ,d=1,t='in_out_quart').start(self.ids.mainpost)
            Animation(height = dp(10) ,d=1,t='in_out_quart').start(self.ids.space)
            Animation1=Animation(y=0,d=.1)
            Animation1.start(self.ids.lin)
            Animation1=Animation(y=0,d=.1)
            Animation1.start(self.ids.botombar)
            Animation1=Animation(y=dp(39),d=.1)
            Animation1.start(self.ids.line) 
            self.scroly=self.ids.scrovw.scroll_y 
    elev = 0
    def to_screen(self,screen):
        
        self.screen = screen
        if screen == 'home':
            self.home=True
            Animation(x=0,d=1,t='in_out_quart').start(self.ids.home_screen)
            Animation(x=self.width,d=1,t='in_out_quart').start(self.ids.chat_screen)
            self.ids.searchbxlay.disabled=False
            self.ids.searchbxlay.opacity= 1.0
            Animation(opacity= 1.0,y=self.ids.searchbx.y,d=1,t='in_out_quart').start(self.ids.searchbxlay)
            
            Animation(y=self.ids.searchbx.y,d=1,t='in_out_quart').start(self.ids.searchbxlay)
            Animation1=Animation(x=0,d=1,t='in_out_quart')
            Animation1.start(self.ids.lin)
            Animation1=Animation(icon_color=get_color_from_hex('#416d6d')[:3]+[.8],line_color=get_color_from_hex('#416d6d')[:3]+[.8],d=1,t='in_out_quart')
            
            Animation1.start(self.ids.homeico)
            if self.current_screen == 'home':
                Animation(scroll_y = self.scrolymax, d=1,t='in_out_quart').start(self.ids.scrovw)
                Animation(x=self.width - self.ids.searchbx.width/2 ,d=1).start(self.ids.searchbxlay)
                Animation(height = self.ids.boxsc.height-dp(60) ,d=1,t='in_out_quart').start(self.ids.mainpost)
                Animation(height = dp(10) ,d=1,t='in_out_quart').start(self.ids.space)
                Animation(opacity= 1.0,x=self.ids.lname.x,d=1,t='in_out_quart').start(self.ids.lname)
                Animation(opacity= 1.0,x=self.ids.hello.x,d=1,t='in_out_quart').start(self.ids.hello)
                Animation(opacity= 1.0,x=self.ids.name.x,d=1,t='in_out_quart').start(self.ids.name)
            
            elif self.current_screen == 'chat':
                self.ids.chatico.icon = 'chat-outline'
                Animation1=Animation(icon_color=[0,0,0,.5],d=1,t='in_out_quart')
                Animation1.start(self.ids.chatico)
                Animation(opacity= 1.0,x=-self.ids.lname.x,d=1,t='in_out_quart').start(self.ids.lname)
                Animation(opacity= 1.0,x=-self.ids.hello.x,d=1,t='in_out_quart').start(self.ids.hello)
                Animation(opacity= 1.0,x=-self.ids.name.x,d=1,t='in_out_quart').start(self.ids.name)
            
            elif self.current_screen == 'freinds':
                self.ids.freindaico.icon = 'account-multiple-outline'
                Animation1=Animation(icon_color=[0,0,0,.5],d=1,t='in_out_quart')
                Animation1.start(self.ids.freindsico)
                Animation(opacity= 1.0,x=-self.ids.lname.x,d=1,t='in_out_quart').start(self.ids.lname)
                Animation(opacity= 1.0,x=-self.ids.hello.x,d=1,t='in_out_quart').start(self.ids.hello)
                Animation(opacity= 1.0,x=-self.ids.name.x,d=1,t='in_out_quart').start(self.ids.name)
            
            elif self.current_screen == 'noti':
                self.ids.notiico.icon = 'bell-outline'
                Animation1=Animation(icon_color=[0,0,0,.5],d=1,t='in_out_quart')
                Animation1.start(self.ids.notiico)
                Animation(opacity= 1.0,x=-self.ids.lname.x,d=1,t='in_out_quart').start(self.ids.lname)
                Animation(opacity= 1.0,x=-self.ids.hello.x,d=1,t='in_out_quart').start(self.ids.hello)
                Animation(opacity= 1.0,x=-self.ids.name.x,d=1,t='in_out_quart').start(self.ids.name)
            
            else:
                print('What the fuck is This Shit right here ')
            self.ids.homeico.icon = 'home'
            self.current_screen = 'home'
            
            # self.ids.profile_bar.elevation = self.elev
        elif screen == 'chat':
            self.home=False
            # self.elev = self.ids.profile_bar.elevation
            # self.ids.profile_bar.elevation = 0
            Animation(x=0,d=1,t='in_out_quart').start(self.ids.chat_screen)
            Animation(x=-self.width,d=1,t='in_out_quart').start(self.ids.home_screen)
            
            an = Animation(y=self.height+dp(10),d=.5,t='in_out_quart')
            
            an.start(self.ids.searchbxlay)
            
            Animation1=Animation(x=self.ids.lin.width,d=1,t='in_out_quart')
            Animation1.start(self.ids.lin)
            Animation1=Animation(icon_color=get_color_from_hex('#416d6d')[:3]+[.8],line_color=get_color_from_hex('#416d6d')[:3]+[.8],d=1,t='in_out_quart')
            Animation1.start(self.ids.chatico)
            
            if self.current_screen == 'chat':
                Animation(scroll_y = self.scrolymax1, d=1,t='in_out_quart').start(self.ids.scrovw1)
                
            elif self.current_screen == 'home':
                Animation(opacity= 0.0,x=-self.ids.lname.x,d=1,t='in_out_quart').start(self.ids.lname)
                Animation(opacity= 0.0,x=-self.ids.hello.x,d=1,t='in_out_quart').start(self.ids.hello)
                Animation(opacity= 0.0,x=-self.ids.name.x,d=1,t='in_out_quart').start(self.ids.name)
            
                self.ids.homeico.icon = 'home-outline'
                Animation1=Animation(icon_color=[0,0,0,.5],d=1,t='in_out_quart')
                Animation1.start(self.ids.homeico)
            elif self.current_screen == 'freinds':
                
                self.ids.freindsico.icon = 'account-multiple-outline'
                Animation1=Animation(icon_color=[0,0,0,.5],d=1,t='in_out_quart')
                Animation1.start(self.ids.freindsico)
            elif self.current_screen == 'noti':
                
                self.ids.notiico.icon = 'bell-outline'
                Animation1=Animation(icon_color=[0,0,0,.5],d=1,t='in_out_quart')
                Animation1.start(self.ids.notiico)
            else:
                print('What the fuck is This Shit right here ')
            self.ids.chatico.icon = 'chat'
            self.current_screen = 'chat'
        elif screen == 'freinds':
            
            Animation1=Animation(x=2*self.ids.lin.width,d=1,t='in_out_quart')
            Animation1.start(self.ids.lin)
            Animation1=Animation(icon_color=get_color_from_hex('#416d6d')[:3]+[.8],line_color=get_color_from_hex('#416d6d')[:3]+[.8],d=1,t='in_out_quart')
            Animation1.start(self.ids.freindsico)
            if self.current_screen == 'freinds':
                Animation(scroll_y = self.scrolymax, d=1,t='in_out_quart').start(self.ids.scrovw)
            elif self.current_screen == 'home':
                self.ids.homeico.icon = 'home-outline'
                Animation1=Animation(icon_color=[0,0,0,.5],d=1,t='in_out_quart')
                Animation1.start(self.ids.homeico)
            elif self.current_screen == 'chat':
                self.ids.chatico.icon = 'chat-outline'
                Animation1=Animation(icon_color=[0,0,0,.5],d=1,t='in_out_quart')
                Animation1.start(self.ids.chatico)
            elif self.current_screen == 'noti':
                self.ids.notiico.icon = 'bell-outline'
                Animation1=Animation(icon_color=[0,0,0,.5],d=1,t='in_out_quart')
                Animation1.start(self.ids.notiico)
            else:
                print('What the fuck is This Shit right here ')
            self.ids.freindsico.icon = 'account-multiple'
            self.current_screen = 'freinds'
        elif screen == 'noti':
            
            Animation1=Animation(x=3*self.ids.lin.width,d=1,t='in_out_quart')
            Animation1.start(self.ids.lin)
            Animation1=Animation(icon_color=get_color_from_hex('#416d6d')[:3]+[.8],line_color=get_color_from_hex('#416d6d')[:3]+[.8],d=1,t='in_out_quart')
            Animation1.start(self.ids.notiico)
            if self.current_screen == 'noti':
                Animation(scroll_y = self.scrolymax, d=1,t='in_out_quart').start(self.ids.scrovw)
            elif self.current_screen == 'home':
                self.ids.homeico.icon = 'home-outline'
                Animation1=Animation(icon_color=[0,0,0,.5],d=1,t='in_out_quart')
                Animation1.start(self.ids.homeico)
            elif self.current_screen == 'freinds':
                self.ids.freindsico.icon = 'account-multiple-outline'
                Animation1=Animation(icon_color=[0,0,0,.5],d=1,t='in_out_quart')
                Animation1.start(self.ids.freindsico)
            elif self.current_screen == 'chat':
                self.ids.chatico.icon = 'chat-outline'
                Animation1=Animation(icon_color=[0,0,0,.5],d=1,t='in_out_quart')
                Animation1.start(self.ids.chatico)
            else:
                print('What the fuck is This Shit right here ')
            self.ids.notiico.icon = 'bell'
            self.current_screen = 'noti'
        else:
            print('What the fuck is This Shit right here ')
    # def trn(self,*args):
    #     if self.screen == 'chat':
    #         self.ids.searchbxlay.disabled=True
    #         Animation(opacity= 0.0,d=5,t='in_out_quart').start(self.ids.searchbxlay)
    
    def to_search_screen(self,x=True):
        
        self.manager.set_screen("search",'down')

########################################################################################################################################################################################



