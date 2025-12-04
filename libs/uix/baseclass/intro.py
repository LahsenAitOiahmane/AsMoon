from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import NumericProperty,BooleanProperty
from kivymd.uix.screen import MDScreen

import time
from libs.uix.components.fillfield import FillField
from libs.uix.components.common_label import CommonLabel
class Intro(MDScreen):
    """Implements the login start screen in the user application."""
    
    OPACITY = NumericProperty(0)
    SHIFT_Y = NumericProperty(dp(0))
    FIELD_WIDTH = NumericProperty(dp(320))
    FIELD_HEIGHT = NumericProperty(dp(52))
    PADDING = NumericProperty(dp(24))
    logsin = NumericProperty(1)
    x1 = NumericProperty(0)
    y1=NumericProperty(0)
    y2=NumericProperty(0)
    x2 = NumericProperty(0)
    def on_enter(self, *args):
        """
        Event called when the screen is displayed: the entering animation is
        complete.
        """
        
                
        
        animation = Animation(SHIFT_Y=dp(140), d=2, t="in_out_quart")
        animation.bind(on_complete=self.animation_bg_zoom)
        animation.start(self)
        Animation(OPACITY=1, d=3).start(self)
        if self.x2==0:    
            animation0 = Animation(x = self.ids.field_login.x - dp(30),y=self.ids.greating0.y -dp(140) ,d=2,t="in_out_quart")
            animation0.bind(on_complete=self.translation1)
            animation0.start(self.ids.greating0)
            annimation1 = Animation(y=self.ids.greating.y+ dp(330),d=2,t="in_out_quart")
            annimation1.start(self.ids.greating)
            self.x2=1
            
    def translation1(self,*args):
        animation0 = Animation(x = self.ids.field_login.x + dp(10),
                               d=1,
                               t="in_out_quart")
        animation0.bind(on_complete=self.translation2)
        animation0.start(self.ids.greating0)
        
    def translation2(self,*args):
        animation0 = Animation(x = self.ids.field_login.x + dp(10)+ self.ids.field_login.width/6,
                               d=.5,
                               t="in_out_quart")
        animation0.bind(on_complete=self.translation3)
        animation0.start(self.ids.greating1)
        
    def translation3(self,*args):
        animation0 = Animation(x = self.ids.field_login.x + dp(10) + self.ids.field_login.width/3,
                               d=.3,
                               t="in_out_quart")
        
        animation0.start(self.ids.greating2)
    def animation_bg_zoom(self, *args):
        Animation(height=self.ids.bg.height + self.SHIFT_Y, d=2, t="in_out_quart").start(
            self.ids.bg
        )
        if self.x1 == 0:
            self.y1=self.ids.greating0.y
            self.y2=self.ids.greating.y
            self.x1=1
       
    def animation_bg_zoom_out(self, *args):
        Animation(height=self.ids.bg.height - self.SHIFT_Y,
                  d=2,
                  t="in_out_quart"
                  ).start(
                      self.ids.bg
                      )
        annimation1 = Animation(y=0,
                                d=2,
                                t="in_out_quart"
                                )
        annimation1.start(self.ids.greating)
        animation0 = Animation(y=self.height,
                               d=2,
                               t="in_out_quart"
                               )
            
        animation0.start(self.ids.greating0)
        
    def blinkscreen(self):
        self.logsin +=1
        animation = Animation(SHIFT_Y=dp(0), d=2, t="in_out_quart")
        animation.bind(on_complete=self.go_to_sinup_screen)
        animation.start(self)
        animation1 = Animation(OPACITY=0, d=1.5)
        
        animation1.start(self)
        self.animation_bg_zoom_out()
        
    def go_to_sinup_screen(self, *args):
        if self.logsin%2 == 0 :
            animation = Animation(x=-self.width,d=0)
            animation.bind(on_complete=self.on_enter)
            animation.start(self.ids.signin)
            animation1 = Animation(x=0,d=0)
            animation1.bind(on_complete=self.signupscreen)
            animation1.start(self.ids.signup)
        else:
            animation = Animation(x=0,d=0)
            animation.bind(on_complete=self.on_enter)
            animation.start(self.ids.signin)
            animation1 = Animation(x=self.width,d=0)
            animation1.bind(on_complete=self.signupscreen)
            animation1.start(self.ids.signup)
    def signupscreen(self,*args):
        if self.logsin%2 == 0 :
            animation = Animation(y=self.y1 + dp(20) ,d=2,t="in_out_quart")
            # animation.bind(on_complete=self.on_enter)
            animation.start(self.ids.greating0)
            Animation(y=self.y2 + self.FIELD_HEIGHT/1.2 ,d=2,t="in_out_quart").start(self.ids.greating)
        else:    
            animation0 = Animation(y=self.y1 ,d=2,t="in_out_quart")
            # animation0.bind(on_complete=self.on_enter)
            animation0.start(self.ids.greating0)
            if  self.y2==0:
                annimation1 = Animation(y=self.y2,d=2,t="in_out_quart")
                annimation1.start(self.ids.greating)
            else:
                annimation1 = Animation(y=self.y2,d=2,t="in_out_quart")
                annimation1.start(self.ids.greating)
        

        