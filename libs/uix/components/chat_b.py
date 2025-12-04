from kivy.lang import Builder
from kivy.properties import DictProperty, ListProperty, StringProperty, ObjectProperty, NumericProperty, BooleanProperty
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.button import MDFlatButton
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.card import MDCard

KV='''
#:import get_color_from_hex kivy.utils.get_color_from_hex
<ChatBubble>:
    id:mainbox
    md_bg_color: [0, 1, 0, 0]
    size_hint_y: None
    size_hint_x: None
    height:posbox.height+timebox.height#+ref_box1.height+spacebox.height
    width: root.myself.width
    orientation: 'vertical'
    MDBoxLayout:
        id:posbox
        # height: msg_content.height + timed.height + 10
        # width: msg_content.width + wid1.width + wid2.width
        size_hint: None, None
        pos_hint: {'right': .97} if root.send_by_user else {'x': .03}
        radius: [4,0,4,4] if root.send_by_user and not root.fromthesame  else [0,4,4,4] if not root.send_by_user and not root.fromthesame else [4,4,4,4] if root.send_by_user and root.fromthesame else [4,4,4,4] if not root.send_by_user and root.fromthesame else [4,4,4,4]
        md_bg_color: get_color_from_hex('#c5d0d3')[:3]+[1] if root.send_by_user else get_color_from_hex('#416d6d')[:3]+[.5]
        width:msgbox.width+ dp(20) #if msgbox.width < 5*root.width/6 else root.width/6
        elevation:9
        height:msgbox.height+dp(10)
        padding: ('5dp', '5dp', '5dp', '5dp')
        MDBoxLayout:
            id:msgbox
            size_hint_x: None
            size_hint_y: None
            orientation: 'horizontal'
            pos_hint: {'center_y': 0.5,'center_x':.5}
            size:msg_content.size
            size_hint_y:None
            size_hint_x:None
            padding: ('5dp', '0dp', '5dp', '0dp')
            # MDLabel:
            #     id: msg_content
            #     text: root.text
            #     width: timebox.width if self.texture_size[0] < timebox.width else self.texture_size[0]
            #     height: self.texture_size[1]
            #     size_hint_y: None
            #     text_size: mainbox.width-30 if self.width >= mainbox.width-30 else None, None
            #     halign: 'left'
            #     # color: app.theme_cls.opposite_bg_normal
            
            Label:
                id: msg_content
                text: root.text
                size_hint_x:None
                size_hint_y: None
                # font_name: 'assets/fonts/arabic/Ar.otf'
                text_size: (None , None)  if (self.texture_size[0])< mainbox.width-(70) else (mainbox.width-(70),None)
                size: self.texture_size
                halign: 'left'
                color: [0,0,0,.8]
                multiline: True
                # on_touch_down: if self.collide_point(*args[1].pos):root.ontouch()
        
    MDBoxLayout:
        id: timebox
        size_hint_y: None
        size_hint_x: None
        height: time.height
        width: time.width + reciepticon.width 
        orientation: 'horizontal'
        pos_hint: posbox.pos_hint
        spacing: '2dp'
        Label:
            id: time
            text: root.time
            size_hint_x:None
            size_hint_y: None
            pos_hint: {'x': 0}
            text_size: (None,None) if  not root.nextsame else (0,0)
            size: (0,0) if  root.nextsame else self.texture_size
            halign: 'right'
            font_size: '10sp' if  not root.nextsame else '0sp'
            color: [0,0,0,0] if  root.nextsame else [0,0,0,.5]
            multiline: False
            # on_touch_down: if self.collide_point(*args[1].pos):root.ontouch()
    
        MDIcon:
            id: reciepticon
            #: set iconds {'read': 'check-all', 'waiting': 'clock-time-three-outline','delivered': 'check'}
            theme_text_color: 'Custom'
            icon: 'check-all'
            size_hint: None, None
            font_size: 0 if  root.nextsame else 12
            size:(0,0) if  root.nextsame else (12, 12)
            color: time.color
    # MDBoxLayout:
    #     id:ref_box1
    #     md_bg_color:[0,.6,0,0]
    #     size:input_label.texture_size
    #     size_hint_y:None
    #     size_hint_x:None
    #     pos_hint: {'center_y': 0.5}
    #     # x:msg_input.x
    #     MDLabel:
    #         id:input_label
    #         text:root.text
    #         size_hint_x:None
    #         text_size:( dp(300) ,None) #if self.width<(mainbox.width-70) else( mainbox.width-70, None)
    #         size: self.texture_size
    #         color:[0,0,0,0]   
    #         font_size:'16sp' 
    #         pos_hint: {'center_x': 0.5,'center_y': 0.5}
    
    # MDBoxLayout:
    #     id:spacebox
    #     # height: msg_content.height + timed.height + 10
    #     # width: msg_content.width + wid1.width + wid2.width
    #     size_hint: None, None
    #     # pos_hint: {'right': 1}# if root.send_by_user else {'left': 1}
    #     radius: [0,]# if self.pos_hint == {'right': 1} else [10, 10, 10, 5]
    #     md_bg_color: [1,1,0,0]
    #     size:root.myself.width ,dp(5) if   root.nextsame else dp(0)
        
'''


Builder.load_string(KV)

from kivy.uix.recycleview.views import RecycleDataViewBehavior

class ChatBubble(RecycleDataViewBehavior, MDBoxLayout):
    text = StringProperty()
    send_by_user = BooleanProperty()
    time = StringProperty()
    myself = ObjectProperty()
    fromthesame = BooleanProperty()
    nextsame = BooleanProperty()
    # text_length = NumericProperty()

        
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
<ImageBub>
    id:mybox
    height:hole_box.height + timebox.height
    orientation: 'vertical'
    width:root.managr.width
    radius:[0,]
    md_bg_color: [0,0,0,0]
    size_hint_x: None
    size_hint_y: None

    MDBoxLayout:
        id:hole_box
        md_bg_color:get_color_from_hex('#c5d0d3')[:3]+[.7]
        width:root.managr.width - dp(50)
        height:text.texture_size[1]+img.height+dp(10) 
        orientation: 'vertical' 
        pos_hint: {'x': 0.03} if not root.fromMe else {'right':.97}
        size_hint_x: None
        size_hint_y: None
        radius:[4,]
        padding:  ('0dp', '0dp', '0dp', '10dp')
        spacing: '5dp'
        MDBoxLayout:
            id:imgbx
            md_bg_color:[0,1,0,0]
            width:root.width-dp(50)
            height:img.height
            orientation: 'vertical'
            size_hint: None, None
            pos_hint: {'top': 0}
            radius:[36,]
            # MDSmartTile:
            Image:
                radius:16
                id:img1
                source: img.source
                size_hint_y: None
                size_hint_x: None
                width: hole_box.width  
                height:0
            FitImage:
                radius:[4,4,0,0]
                id:img
                source: root.image
                size_hint_y: None
                size_hint_x: None
                width: hole_box.width 
                height: self.parent.width/img1.image_ratio  if (dp(self.parent.width/img1.image_ratio))<root.managr.height/1.5 else (root.managr.height/1.5)
                # on_touch_down: if self.collide_point(*args[1].pos):root.to_post_screen()
        MDLabel:
            id:text
            text:root.comment
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
            # on_touch_down: if self.collide_point(*args[1].pos):root.to_post_screen()
            
            # strip:True
            # size_hint_x: None
            # strikethrough:True
            # max_lines:3
            # is_shortened:True
            # shorten:True 
            # allow_selection:True
            # on_selection:self.text = 'empty'
            # allow_copy: True
            # on_copy:print('copied')
            # MDLabel:
        #     id:textpoint
        #     text: "..."
        #     font_name: 'assets/fonts/Lexend-Regular.ttf'
        #     font_size:'14sp'
            
        #     color:[0,0.1,0.1,.9]        
        # MDLabel:
        #     id:lname
        #     text: root.last_msg
        #     font_name: 'assets/fonts/Lexend-Light.ttf'
        #     font_size:'12sp'
        #     markup:True
        #     mipmap:True
        #     shorten_from:'right'
        #     shorten:True
        #     bold:True
        #     # ellipsis_options: {'text':'more...','color':(1,0.5,0.5,1),'underline':True}
        #     color:[0,0,0,1]
        #     adaptive_height:True
        #     multiline:False
    MDBoxLayout:
        id: timebox
        size_hint_y: None
        size_hint_x: None
        height: time.height
        width: time.width + reciepticon.width 
        orientation: 'horizontal'
        pos_hint: hole_box.pos_hint
        spacing: '2dp'
        Label:
            id: time
            text: root.time
            size_hint_x:None
            size_hint_y: None
            pos_hint: {'x': 0}
            text_size: (None,None) #if  not root.nextsame else (0,0)
            size: self.texture_size #//(0,0) if  root.nextsame else //
            halign: 'right'
            font_size: '10sp' #if  not root.nextsame else '0sp'
            color:  [0,0,0,.5] #//[0,0,0,0] if  root.nextsame else
            multiline: False
            # on_touch_down: if self.collide_point(*args[1].pos):root.ontouch()
    
        MDIcon:
            id: reciepticon
            #: set iconds {'read': 'check-all', 'waiting': 'clock-time-three-outline','delivered': 'check'}
            theme_text_color: 'Custom'
            icon: 'check-all'
            size_hint: None, None
            font_size:  12 #//0 if  root.nextsame else
            size:(12, 12) #//(0,0) if  root.nextsame else 
            color: time.color        
            
   
       
     
                    
                        
''' 

Builder.load_string(KV)
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    DeclarativeBehavior,
    RectangularRippleBehavior,
)

from kivymd.theming import ThemableBehavior

class ImageBub(MDBoxLayout):

    id = NumericProperty()
    
    fromMe = StringProperty()

    comment = StringProperty()

    time = StringProperty()

    # profile_image = StringProperty()

    image = StringProperty()
    
    read = BooleanProperty()
    
    managr = ObjectProperty()
    
    def like(self):
        self.read = False if self.read == True else True
    def to_post_screen(self):
        self.managr.manager.set_screen('post','up')
        self.managr.manager.get_screen('post').post_data(8)
  
        
        
        
                 