import random
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
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ButtonBehavior



   
KV = '''

<PostItem>
    id:postitems
    md_bg_color:[0,0,0,0]
    width:root.managr.width 
    height: bx.height+bx1.height+ bx2.height+ bx3.height+ bx4.height
    size_hint: None, None
    orientation: 'vertical'
    
    MDBoxLayout:
        id:bx1
        md_bg_color:[1,1,0,0]
        width:postitems.width 
        height:prof.height 
        orientation: 'horizontal'
        size_hint: None, None
        MDBoxLayout:
            md_bg_color:[1,1,0,0]
            width:prof.width 
            size_hint_x:None
           
            
            MDIconButton:
                id:prof
                icon:root.profile_image
                size_hint_x:1
                pos_hint: {'center_x':1,'center_y':0.5}
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex('#416d6d')
                rgba: 0,0,0,0
                line_color: 0,0,0, 0
                icon_size: dp(30)
                font_size: dp(30)
        Box:
            radius:[0,]
            md_bg_color:[0,0,0,0]
            width:postitems.width - prof.width - det.width
            orientation: 'vertical' 
            pos_hint: {'center_y': .58}
            size_hint_x: None
            MDLabel:
                id:fname
                text:root.fname
                
                font_name: 'assets/fonts/Lexend-Medium.ttf'
                font_size:'14sp'
                adaptive_height:True
                markup:True
                shorten:True
                shorten_from:'right'
                mipmap:True
                color: [0,0,0,.8]
                multiline:False
                pos_hint: {'left': -.2,'center_y': 0.4}
                  
            MDLabel:
                id:date
                text: ' '+root.date
                font_name: 'assets/fonts/Lexend-Light.ttf'
                font_size:'12sp'
                markup:True
                shorten:True
                shorten_from:'right'
                mipmap:True
                color:[0,0,0,.8]
                adaptive_height:True
                mipmap:True
                pos_hint: {'left': 1,'center_y': 0.5}
                
            
            
        MDBoxLayout:
            md_bg_color:[0,1,1,0]
            width:det.width
            pos_hint: {'center_y': 0.65}
            size_hint_x:None
            orientation: 'vertical'
            MDIconButton:
                id:det
                icon:'dots-vertical'
                
                pos_hint: {'right':1,'center_y':0.5}
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex('#416d6d')
                rgba: 0,0,0,0
                line_color: 0,0,0, 0
                icon_size: dp(20)
                font_size: dp(30)
        
    MDBoxLayout:
        id:bx2
        md_bg_color:[1,0,0,0]
        width:postitems.width 
        height:text.texture_size[1]
        size_hint_y:None
        size_hint_x:None
        padding: ('5dp', '10dp', '5dp','0dp')
        # spacing: '10dp'
        on_touch_down: if self.collide_point(*args[1].pos):root.to_txt()
       
        Label:
            id:text
            text:root.txxt
            text2:root.txt
            # font_name: 'assets/fonts/Lexend-Regular.ttf'
            font_size:'14sp'
            text_size: postitems.width, None
            size: self.texture_size
            haling:'left'
            multiline:True
            # strip:True
            size_hint: None,None
            # strikethrough:True
            markup:True
            # allow_selection:True
            # on_selection:self.text = 'empty'
            # allow_copy: True
            multiline:True
            # max_lines:3
            # is_shortened:True
            # shorten:True 
            mipmap:True
            shorten_from:'right'
            color:[0,0,0,.8]
            # on_copy:print('copied')
    
            
    MDBoxLayout:
        id:bx3
        md_bg_color:[0,1,0,0]
        width:postitems.width 
        height:img.height 
        orientation: 'horizontal'
        padding:0
        # MDSmartTile:
        size_hint: None, None
        FitImage:
            # radius:[0,]
            id:img
            source:  root.image
            size_hint_y: None
            size_hint_x: None
            width: postitems.width 
            height: 0 if self.source=='' else self.parent.width/img1.image_ratio  if (dp(self.parent.width/img1.image_ratio))<root.managr.height/1.5 else (root.managr.height/1.5)
            on_touch_down: if self.collide_point(*args[1].pos):root.to_post_screen()
        Image:
            # radius:16
            id:img1
            source: img.source
            size_hint_y: None
            size_hint_x: None
            width: postitems.width  
            height:0
      
           
    MDBoxLayout:
        id:bx4
        md_bg_color:[1,0,1,0]
        width:postitems.width 
        height:dp(40)+com.texture_size[1]+bx5.height
        size_hint_x:None
        size_hint_y: None
        orientation: 'vertical'
        
        MDBoxLayout:
            pos_hint: {'center_y': 0.5}
            md_bg_color:[1,0,0,0]
            width:postitems.width 
            spacing: '10dp'
            height:com.texture_size[1]
            size_hint_y:1
            orientation: 'horizontal'
            MDBoxLayout:
                pos_hint: {'center_y': 0.5}
                md_bg_color:[1,0,0,0]
                width:likes.texture_size[0]
                height:likes.texture_size[1]
                size_hint_y:None
                orientation: 'horizontal'
                MDLabel:
                    id:likes
                    text: f' {root.likes} likes'
                    font_name: 'assets/fonts/Lexend-Medium.ttf'
                    font_size:'11sp'
                    pos_hint: {'left':1,'center_y': 0.5}
                    color:[0,0.1,0.1,.7]
                    
            MDBoxLayout:
           
                md_bg_color:[1,1,0,0]
                width:postitems.width/2
                height:com.texture_size[1]
                pos_hint: {'center_y': 0.5}
                size_hint_y: None
                orientation: 'vertical'
                MDLabel:
                    id:com
                    text: f'{root.coments} comments 1 repost '
                    font_name: 'assets/fonts/Lexend-Medium.ttf'
                    font_size:'11sp'
                    adaptive_size:True,True
                    pos_hint: {'right': 1,'center_y': .5}
                    color:[0,0.1,0.1,.7]
            
        MDBoxLayout:
            id:bx5
            md_bg_color:[0,0,0,.5]
            width:postitems.width/1.05
            height:dp(0.5)
            pos_hint: {'center_x': 0.5}
            radius:[6,6,0,0]
        
            size_hint_y:None
            size_hint_x:None
            orientation: 'horizontal'              
        
        MDBoxLayout:
           
            md_bg_color:[0,0,1,0]
            width:postitems.width 
            height:dp(30)
            size_hint_y:None
            size_hint_x:None
            orientation: 'horizontal'
            MDBoxLayout:
                md_bg_color:[1,0,1,0]
                height:lic.height
                size_hint_y:None
                MDIconButton:
                    id:lic
                    # lkd: root.liked
                    icon:'heart-outline' #if  root.liked == False else 'heart'
                    size_hint_x:1
                    pos_hint: {'center_x':1,'center_y':0.5}
                    theme_icon_color: "Custom"
                    
                    icon_color:get_color_from_hex('#416d6d')[:3]+[.8]
                    rgba: 0,0,0,0
                    line_color: get_color_from_hex('#416d6d')[:3]+[.8]
                    icon_size: '20sp'    
                    on_release: root.like()
                    
                
            MDBoxLayout:

                md_bg_color:[1,1,1,0]
                height:cic.height
                size_hint_y:None
                MDIconButton:
                    id:cic
                    icon:'comment-outline'
                    size_hint_x:1
                    pos_hint: {'center_x':1,'center_y':0.5}
                    theme_icon_color: "Custom"
                    icon_color:[0,0,0,.5]
                    rgba:[0,0,0,0]
                    icon_color:get_color_from_hex('#416d6d')[:3]+[.8]
                    icon_size: '20sp'
                    on_press: root.to_post_screen()
       
            MDBoxLayout:
                md_bg_color:[0,1,0,0]
                height:ric.height
                size_hint_y:None
                MDIconButton:
                    id:ric
                    icon:'repeat'
                    size_hint_x:1
                    pos_hint: {'center_x':1,'center_y':0.5}
                    theme_icon_color: "Custom"
                    icon_color:[0,0,0,.5]
                    rgba: 0,0,0,0
                    icon_color: get_color_from_hex('#416d6d')[:3]+[.8]
                    line_color: get_color_from_hex('#416d6d')[:3]+[.8]
                    icon_size: '20sp'
            MDBoxLayout:
                md_bg_color:[0,0,0,0]
                height:sic.height
                size_hint_y:None
                # line_color:[1,0,1,1]
                MDIconButton:
                    id:sic
                    idd:str(root.idd)
                    icon:'send-outline'
                    size_hint_x:1
                    pos_hint: {'center_x':1,'center_y':0.5}
                    halign:'center'
                    valing:'center'
                    theme_icon_color: "Custom"
                    icon_color:[0,0,0,.5]
                    rgba: 0,0,0,0
                    icon_color: get_color_from_hex('#416d6d')[:3]+[.8]
                    icon_size: '20sp'
                    
                    
    MDBoxLayout:
        id:bx
        md_bg_color:[0,0,0,.1]
        width:postitems.width 
        height:dp(3)
        
        
       
        size_hint_y:None
        size_hint_x:None
        orientation: 'horizontal'        
        
'''
Builder.load_string(KV)
from kivy.animation import Animation
from kivymd.uix.screen import MDScreen
# from libs.uix.Root import root
import json
from kivy.uix.screenmanager import ScreenManager
# from libs.uix.baseclass.info_screen import InfoScreen
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from kivy.clock import Clock

class PostItem(RecycleDataViewBehavior,MDBoxLayout):
    idd= NumericProperty()
    fname=StringProperty()
    date=StringProperty()
    likes=NumericProperty()
    coments=NumericProperty()
    profile_image=StringProperty()
    image=StringProperty()
    liked = BooleanProperty()
    txxt = StringProperty()
    txt = StringProperty()
    managr = ObjectProperty()
    
    
    def like(self):
        self.ids.lic.icon = 'heart' if self.ids.lic.icon == 'heart-outline' else 'heart-outline'
        self.likes = self.likes + 1  if  self.liked else self.likes-1
        lst = self.ids.likes.text.split(' ')
        self.ids.likes.text = f' {int(lst[1]) + 1} likes' if self.ids.lic.icon == 'heart' else f' {int(lst[1]) - 1} likes'
    def to_post_screen(self):
       
        Clock.schedule_once(self.tscrn,.3)
     
    def tscrn(self,*args):

        self.managr.manager.set_screen('post','up')
   
        self.managr.manager.get_screen('post').post_data(int(self.ids.sic.idd))

    def to_txt(self):
        #if len(self.ids.text.text)< len(self.ids.text.text2):
        t = self.ids.text.text
        self.ids.text.text = self.ids.text.text2
        self.ids.text.text2 = t
