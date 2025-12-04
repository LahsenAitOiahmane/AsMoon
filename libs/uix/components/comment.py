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
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivy.uix.behaviors import ButtonBehavior

KV='''
<CommentListItem>
    height:hole_box.height
    orientation: 'horizontal'
    width:root.managr.width
    radius:[0,]
    md_bg_color: [0,0,0,0]
    size_hint_x: None
    size_hint_y: None
    
    
    MDBoxLayout:
        pos_hint: {'center_y': 0.45}
        md_bg_color:[1,1,0,0]
        width:icprof.width
        height:hole_box.height 
        orientation: 'vertical'
        size_hint: None, None
        MDBoxLayout:
            md_bg_color:[1,1,0,0]
            width:icprof.width 
            size_hint_x:None
           
            
            MDIconButton:
                id:icprof
                icon:(root.profile_image)
                size_hint_x:1
                pos_hint: {'center_x':1,'center_y':1.05}
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex('#416d6d')
                rgba: 0,0,0,0
                line_color: 0,0,0, 0
                icon_size: dp(30)
                font_size: dp(30)
        MDBoxLayout:
            
            md_bg_color:[1,1,0,0]
            width:licb.width 
            size_hint_x:1
            orientation: 'horizontal'
            
            MDIconButton:
                id:licb
                icon:'heart-outline' if root.read == True else 'heart'
                size_hint_x:2
                pos_hint: {'center_x':-1,'center_y':1}
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex('#416d6d')[:3]+[.7]
                rgba: 0,0,0,0
                line_color: 0,0,0, 0
                icon_size: dp(20)
                # font_size: dp(30)
                on_press: root.like()
        MDBoxLayout:
            
            md_bg_color:[1,1,0,0]
            width:licb1.width 
            size_hint_x:None
            pos_hint: {'x': -1}
            
            
            MDIcon:
                id:licb1
                icon:str(root.id)
                size_hint_x:None
                pos_hint: {'center_x':0}
                theme_icon_color: "Custom"
                icon_color: [0,0,0,0]
                rgba: 0,0,0,0
                line_color: 0,0,0, 0
                icon_size: 0
    MDBoxLayout:
        id:hole_box
        md_bg_color:get_color_from_hex('#c5d0d3')[:3]+[.7]
        width:root.managr.width - dp(50)
        height:text.texture_size[1]+name.texture_size[1]+img.height+dp(20)
        orientation: 'vertical' 
        size_hint_x: None
        size_hint_y: None
        radius:[0,16,16,16]
        padding: ('10dp', '5dp', '5dp', '10dp') if img.source=='' else ('0dp', '5dp', '0dp', '10dp')
        # spacing: '10dp'
        MDLabel:
            id:name
            text:' '+(root.fname) if not img.source=='' else (root.fname)
            font_name: 'assets/fonts/Lexend-Medium.ttf'
            font_size:'14sp'
            adaptive_height:True
            color: [0,0,0,.8]
            multiline:False
            pos_hint: {'top': 1}
            on_touch_down: if self.collide_point(*args[1].pos):root.to_post_screen()
        MDBoxLayout:
            id:imgbx
            md_bg_color:[0,1,0,0]
            width:root.managr.width-dp(50)
            height:img.height
            orientation: 'vertical'
            size_hint: None, None
            pos_hint: {'top': 0}
            radius:[36,]
            # MDSmartTile:
            Image:
                radius:16
                id:img1
                # radius: 0
                # box_radius: [0,]
                # box_color: 1, 1, 1, 0
                # fit_mode:'scale-down'
                # size_hint_x: None
                # size_hint_max_y: .4
                # size_hint_y: None
                # size_hint_x: None
                # on_touch_down: if self.collide_point(*args[1].pos):root.to_post_screen()
                source: img.source
                #height: (root.width*2-dp(145)) if root.image is not '' else 0#imgfit.texture_size[1] if (imgfit.texture_size[1]<(root.height-dp(145))) else
                # allow_stretch: True
                # height:dp(100)
                size_hint_y: None
                size_hint_x: None
                width: hole_box.width 
                
                            
                height:0
            FitImage:
                    
                radius:16
                id:img
                # radius: 0
                # box_radius: [0,]
                # box_color: 1, 1, 1, 0
                # fit_mode:'scale-down'
                # size_hint_x: None
                # size_hint_max_y: .4
                # size_hint_y: None
                # size_hint_x: None
                source: (root.image)
                # height: (root.width*2-dp(145)) if root.image is not '' else 0#imgfit.texture_size[1] if (imgfit.texture_size[1]<(root.height-dp(145))) else
                # allow_stretch: True
                # height:dp(100)
                size_hint_y: None
                size_hint_x: None
                width: hole_box.width 
                
                height:0 if self.source=='' else self.parent.width/img1.image_ratio  if (dp(self.parent.width/img1.image_ratio))<root.managr.height/2 else (root.managr.height/2)
                on_touch_down: if self.collide_point(*args[1].pos):root.to_post_screen()
       
                
        MDLabel:
            id:text
            text:(root.comment)
            font_name: 'assets/fonts/Lexend-Regular.ttf'
            font_size:'14sp'
            
            haling:'left'
            multiline:True
            markup:True
            multiline:True
            mipmap:True
            shorten_from:'right'
            color:[0,0,0,.8]
            pos_hint: {'center_x': 0.5,'top': 1}
            on_touch_down: if self.collide_point(*args[1].pos):root.to_post_screen()
          
                        
''' 

Builder.load_string(KV)
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    DeclarativeBehavior,
    RectangularRippleBehavior,
)

from kivymd.theming import ThemableBehavior

class CommentListItem(MDBoxLayout):

    id = NumericProperty()
    
    fname = StringProperty()

    comment = StringProperty()

    time = StringProperty()

    profile_image = StringProperty()

    image = StringProperty()
    
    read = BooleanProperty()
    
    managr = ObjectProperty()
    
    def like(self):
        self.read = False if self.read == True else True
    def to_post_screen(self):
        self.managr.manager.set_screen('post','up')
        id = int(self.ids.licb1.icon)
        # print(id - 1)
        self.managr.manager.get_screen('post').post_data(id-1, False)
  
        
        
        
                