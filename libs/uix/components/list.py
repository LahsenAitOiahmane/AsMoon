from kivy.app import Builder
from kivy.properties import StringProperty,NumericProperty, BooleanProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.uix.behaviors import ButtonBehavior

KV='''
<ChatListItem>
    height:dp(60)
    orientation: 'horizontal'
    width:root.width
    radius:[0,]
    md_bg_color: [1,0,1,0]
    size_hint_x: None
    size_hint_y: None
   
    
    MDBoxLayout:
        pos_hint: {'center_y': 0.5}
        md_bg_color:[1,1,0,0]
        width:root.width - t.width
        height:icprof.height 
        orientation: 'horizontal'
        size_hint: None, None
        MDBoxLayout:
            md_bg_color:[1,1,0,0]
            width:icprof.width 
            size_hint_x:None
           
            
            MDIconButton:
                id:icprof
                icon:'assets/icons/profile.png'
                size_hint_x:1
                pos_hint: {'center_x':1,'center_y':0.5}
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex('#416d6d')
                rgba: 0,0,0,0
                line_color: 0,0,0, 0
                icon_size: dp(30)
                font_size: dp(30)
        MDBoxLayout:
            md_bg_color:[0,0.5,0,0]
            width:root.width - icprof.width - t.width
            orientation: 'vertical' 
            pos_hint: {'center_y': .58}
            size_hint_x: None
            MDLabel:
                id:name
                text:root.name
                font_name: 'assets/fonts/Lexend-Medium.ttf'
                font_size:'14sp'
                adaptive_height:True
                color: [0,0,0,.8]
                multiline:False
                pos_hint: {'left': -.2,'center_y': 0.4}
                  
            MDLabel:
                id:lname
                text: root.last_msg
                font_name: 'assets/fonts/Lexend-Light.ttf'
                font_size:'12sp'
                markup:True
                mipmap:True
                shorten_from:'right'
                shorten:True
                bold:True
                # ellipsis_options: {'text':'more...','color':(1,0.5,0.5,1),'underline':True}
                color:[0,0,0,1]
                adaptive_height:True
                multiline:False
                pos_hint: {'left': 1,'center_y': 0.5}
                
            
   
       
    MDBoxLayout:
        pos_hint: {'center_y': 0.5}
        width:t.width 
        height:(icprof.height+dp(5))
        orientation: 'vertical'
        size_hint: None, None
        md_bg_color: [0,0,0,0]
       
        
        MDBoxLayout:
            width:t.width 
            height:(icprof.height+dp(5))/2
            size_hint_y: None
            md_bg_color: [1,1,0,0]
        
            MDLabel:
                id:t
                text: root.time 
                font_style: 'Caption'
                mipmap:True
                font_size:'11sp'
                adaptive_size:True, False
                size_hint_y:None
        MDBoxLayout:
        
            width:t.width 
            height:(icprof.height+dp(5))/2
            orientation: 'horizontal'
            size_hint: None, None
            md_bg_color: [0,0,0,0]       
            MDBoxLayout:
                width:t.width/2
                height: (icprof.height+dp(5))/2
                size_hint_y: None
                size_hint_x: None
                md_bg_color: [1,0,0,0]
                
            MDBoxLayout:
                width:t.width/2
                height: (icprof.height+dp(5))/2
                size_hint_y: None
                size_hint_x: None
                md_bg_color: [1,0,1,0]
                MDIcon:
                
                    icon:'numeric-1-circle'
                    size_hint_x:None
                    pos_hint: {'center_x':1,'center_y':0.5}
                    theme_icon_color: "Custom"
                    icon_color: get_color_from_hex('#416d6d')
                    rgba: 0,0,0,0
                    line_color: 0,0,0, 0
                    icon_size: dp(10)
                    font_size: dp(18)
                    
                    
                        
''' 

Builder.load_string(KV)
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    DeclarativeBehavior,
    RectangularRippleBehavior,
)

from kivymd.theming import ThemableBehavior

from kivymd.uix.card import MDCardSwipe
class ChatListItem(
    RectangularRippleBehavior,
    ButtonBehavior,
    
    MDBoxLayout
):

    id = NumericProperty()
    
    name = StringProperty()

    last_msg = StringProperty()

    time = StringProperty()

    image = StringProperty()
    
    read = BooleanProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
                