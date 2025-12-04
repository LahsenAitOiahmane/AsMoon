import asynckivy
from kivy.animation import Animation
from kivy.properties import DictProperty, ListProperty, StringProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
# from kivymd.toast import toast
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
import json
# from kivymd.utils import asynckivy
import asynckivy
from libs.uix.components.comment import CommentListItem
from libs.uix.baseclass.info_screen import InfoScreen
from libs.uix.components.hori_bub import PostItem
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
from kivy.clock import Clock,ClockBase

class LabBox(MDBoxLayout):
    pass
class PostScreen(MDScreen):
    id= NumericProperty()
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
    
    
    postdata = ListProperty()
    
    scroly=NumericProperty()
    scroly1 = NumericProperty()
    comments_list=ListProperty()
    screen_number = ListProperty()
    prv_id = ListProperty()
    def to_prv_screen(self):
        print(self.nb)
        if self.nb == 1:
            self.manager.set_screen('info','down')
            self.nb =0
        else:
            self.manager.goto_previous_screen()
            self.nb -= 1
        Clock.schedule_once(self.clearwidg,1)
        
    def clearwidg(self,dl):
        # for widget in self.lst:
        # self.ids.pbox.clear_widgets()
        self.ids.cbox.clear_widgets()
        if self.nb >= 1:
            self.load_post(0,True)
            print(self.nb)
        
        
        # self.lst = []
 
    lst=[]
    nb = 0
    def post_data(self,id=0,p_c=True):
        self.ids.post.managr = self
        if self.nb!=0:
            self.nb+=1
            Clock.schedule_once(self.clearwidg,-1)
        
        else:
            self.nb+=1
            self.load_post(id,p_c)
    
    def load_post(self,id,p_c):
        
        i =id
        txt = "Hello freinds it is my first time here and I'm so glad that I have this opportinity to share my thoughts and also to learn more in this platforme. thank you"
        
        txt=f"[font=assets/fonts/Lexend-Regular.ttf]{txt}[/font]"
        
        self.postdata = [{'id':1,'name':' lahsen wahmane','date':'08/09/2022','likes':25,'coments':145,'profile_image':'assets/icons/profile.png','image':'assets/images/sunset.jpg', 'liked':False,  'txxt':txt, 'managr':self},
                 {'id':2,'name':'Mouad Ait Oihmane','date':'08/09/2023','likes':5,'coments':295,'profile_image':'assets/icons/profile.png','image':'assets/images/peakpx.jpg', 'liked':False, 'txxt':txt, 'managr':self},
                 {'id':3,'name':'youssef Ait Oihmane','date':'02/02/2021','likes':1345,'coments':224,'profile_image':'assets/icons/profile.png','image':'assets/images/bgpic.png', 'liked':False,'txxt':txt, 'managr':self},
                 {'id':4,'name':'imik imik','date':'08/09/6022','likes':85,'coments':55,'profile_image':'assets/icons/profile.png','image':'','liked':False, 'txxt':txt, 'managr':self},
                 {'id':5,'name':'Mikell sco','date':'08/09/2024','likes':20,'coments':59,'profile_image':'assets/icons/profile.png','image':'assets/images/img.jfif','liked':False, 'txxt':txt, 'managr':self},
                 {'id':6,'name':'cr7','date':'08/09/2422','likes':295,'coments':15,'profile_image':'assets/icons/profile.png','image':'assets/images/peakpx.jpg','liked':False, 'txxt':txt, 'managr':self},
                 {'id':7,'name':'smiya o lkneya','date':'08/09/5022','likes':805,'coments':65,'profile_image':'assets/icons/profile.png','image':'assets/images/bgpic.png','liked':True, 'txxt':txt, 'managr':self},
                 {'id':8,'name':'wali bda','date':'08/09/6022','likes':85,'coments':55,'profile_image':'assets/icons/profile.png','image':'','liked':False, 'txxt':txt, 'managr':self},
                 {'id':9,'name':'hhhhhhh','date':'08/09/222','likes':45,'coments':25,'profile_image':'assets/icons/profile.png','image':'assets/images/peakpx.jpg','liked':False, 'txxt':txt, 'managr':self},
                 {'id':10,'name':'l9wada','date':'08/09/2722','likes':275,'coments':23,'profile_image':'assets/icons/profile.png','image':'assets/images/bgpic.png','liked':False,'txxt':txt, 'managr':self}
                ]
        
        self.fname = self.postdata[i]['name'] +( " post's" if p_c else " Comment's")
        
        self.id= self.postdata[i]['id']
        self.fname=self.postdata[i]['name']
        self.date=self.postdata[i]['date']
        self.likes=self.postdata[i]['likes']
        self.coments=self.postdata[i]['coments']
        self.profile_image=self.postdata[i]['profile_image']
        self.image=self.postdata[i]['image']
        self.liked=self.postdata[i]['liked']
        self.txxt=self.postdata[i]['txxt']
        self.txt=self.postdata[i]['txxt']
        self.managr=self.postdata[i]['managr']
        
        # self.ids.pbox.add_widget(PostItem())
        # self.ids.pbox.add_widget(LabBox())
            
        
        
        Clock.schedule_once(self.commments_data,1.2)
    def commments_data(self,*args):
        
        
        #////// load comments_data
        self.comments_list = []
     
        txt = "Hello freinds it is my first time here and I'm so glad that I have this opportinity to share my thoughts and also to learn more in this platforme. thank you"
        txxt = txt


        
        self.comments_list = [{'id':1,'fname':' lahsen wahmane','date':'08/09/2022','likes':25,'coments':145,'profile_image':'assets/icons/profile.png','image':'', 'liked':False,  'txxt':txt, 'txtt':txxt,'managr':self},
                              {'id':2,'fname':'Mouad Ait Oihmane','date':'08/09/2023','likes':5,'coments':295,'profile_image':'assets/icons/profile.png','image':'', 'liked':False, 'txxt':txt,'txtt':txxt,'managr':self},
                              {'id':3,'fname':'youssef Ait Oihmane','date':'02/02/2021','likes':1345,'coments':224,'profile_image':'assets/icons/profile.png','image':'', 'liked':False,'txxt':txt,'txtt':txxt,'managr':self},
                              {'id':5,'fname':'Mikell sco','date':'08/09/2024','likes':20,'coments':59,'profile_image':'assets/icons/profile.png','image':'','liked':False, 'txxt':txt,'txtt':txxt,'managr':self},
                              {'id':6,'fname':'cr7','date':'08/09/2422','likes':295,'coments':15,'profile_image':'assets/icons/profile.png','image':'','liked':False, 'txxt':txt,'txtt':txxt,'managr':self},
                              {'id':7,'fname':'smiya o lkneya','date':'08/09/5022','likes':805,'coments':65,'profile_image':'assets/icons/profile.png','image':'','liked':True, 'txxt':txt,'txtt':txxt,'managr':self},
                              {'id':8,'fname':'wali bda','date':'08/09/6022','likes':85,'coments':55,'profile_image':'assets/icons/profile.png','image':'','liked':False, 'txxt':txt,'txtt':txxt,'managr':self},
                              {'id':9,'fname':'hhhhhhh','date':'08/09/222','likes':45,'coments':25,'profile_image':'assets/icons/profile.png','image':'','liked':False, 'txxt':txt,'txtt':txxt,'managr':self},
                              {'id':10,'fname':'l9wada','date':'08/09/2722','likes':275,'coments':23,'profile_image':'assets/icons/profile.png','image':'','liked':False,'txxt':txt,'txtt':txxt,'managr':self}
                            ]

       
        l=len(self.comments_list)
        async def comment_load():
            for i in range(l):
                # await asynckivy.sleep(0)
                CommentListItem.id= self.comments_list[i]['id']
                CommentListItem.fname=self.comments_list[i]['fname']
                CommentListItem.time=self.comments_list[i]['date']
                CommentListItem.profile_image=self.comments_list[i]['profile_image']
                CommentListItem.image=self.comments_list[i]['image']
                CommentListItem.comment = self.comments_list[i]['txxt']
                CommentListItem.managr = self.comments_list[i]['managr']        
            
                
                self.ids.cbox.add_widget(CommentListItem())
        asynckivy.start((comment_load()))
        # for wgt in self.lst:
        #     self.ids.cbox.add_widget(wgt)
  
    
    def to_home_screen(self):
        l=len(self.screen_number)
        l_id = len(self.prv_id)
        if self.screen_number[l-1]==1:
            self.screen_number=[]
            self.manager.set_screen('info','down')
            self.manager.get_screen('info').strt()
        
        else:
           
            lst = []
            for i in range(l-1):
                lst.append(self.screen_number[i])
           
            self.screen_number = lst
            self.manager.set_screen('post','down')
            self.manager.get_screen('post').post_data(self.prv_id[l_id-2],2)
            lst = []
            for i in range(l_id-1):
                lst.append(self.prv_id[i])
            self.prv_id = lst
            
            
  
    b=False
    # def mv(self):
        
    #     if self.ids.scrv.scroll_y < self.scroly1 or self.ids.sv.scroll_y < self.scroly :
    #         Animation2=Animation(y=-self.ids.comment_input.height,d=.1)
    #         Animation2.start(self.ids.comment_input)

    #         Animation2=Animation(y=-self.ids.llin.height,d=.1)
    #      /-
    # 
    # /Animation2.start(self.ids.llin) 
    #         self.scroly1=self.ids.scrv.scroll_y 
    #         self.scroly1 = self.ids.sv.scroll_y 
            
    #     if self.ids.scrv.scroll_y >= self.scroly1 or self.scroly1 < self.ids.sv.scroll_y :

    #         Animation1=Animation(y=0,d=.1)
    #         Animation1.start(self.ids.comment_input)
    #         Animation1=Animation(y=self.ids.comment_input.height,d=.1)
    #         Animation1.start(self.ids.llin) 
    #         self.scroly1=self.ids.scrv.scroll_y
    #         self.scroly1 = self.ids.sv.scroll_y 
            
            
    #     if self.b==False :
    #         self.b=True
            
    #         Animation(scroll_y=0,d=1,t='in_out_quart').start(self.ids.sv)
            
    #     if self.ids.scrv.scroll_y>1.0 :
    #         Animation(scroll_y=1.0,d=1,t='in_out_quart').start(self.ids.sv)
    #         self.b=False
            
    