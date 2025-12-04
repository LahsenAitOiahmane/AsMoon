from kivy.app import Builder
from kivy.animation import Animation
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex
import json
import datetime
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

        
class ClickableTextFieldRound1(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    def delete_all(self):
        self.ids.text_field.text = ''
    def printf(self):
        print(self.ids.text_field.text)

class HomeScreen(MDScreen, ThemableBehavior):
    users_data = ListProperty()
    group_data = ListProperty()
    title = StringProperty()
    msg = StringProperty()
    # ///////////
    pre_scr = ' '
    # /////////
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.anim(0)
        self.users_data = []
        self.ids.title_top_bar.text = 'Chats'
        self.load_users_data()
                
        items = [
            "New Group",
            "New Chat",
            'New Statu'
        ]
        menu_items = [
            {
                "text": item,
                'md_bg_color':[1,1,1,1],
                "viewclass": "OneLineListItem",
                "height": dp(54),
                "divider": None,
                "on_release":lambda *args: self.to_settings()
            }
            for item in items
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.dots,
            items=menu_items,
            width_mult=3,
            radius=[20,0,20,20],
        )
    def anim(self,n):
        Animation(md_bg_color= [1,1,1,n], d=.8).start(self.ids.hid_box)    
    def load_users_data(self):
        self.rd = BooleanProperty()
        self.group_data = []
        self.users_data = []
        conn = sqlite3.connect('assets/DataBases/Contact_data.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM CHAT_LIST_DATA ")
        records = c.fetchall()
        conn.commit()
        async def load_users_data():
            for i in records:
       
                name = "WITH_ID_"+str(i[0])
                conn1 = sqlite3.connect('assets/DataBases/OnePersMsgByID.db')
                c1 = conn1.cursor()
                
                c1.execute('''CREATE TABLE IF NOT EXISTS '''+name+'''(
                    MSG_Id INTEGER PRIMARY KEY,
                    Message text,
                    date text,
                    Liked bool,
                    From_Me bool,
                    Read bool
                    );
                    '''
                )
                conn1.commit()
                conn1.close()
                
            for i in records:
                await asynckivy.sleep(0)
                name = "WITH_ID_"+str(i[0])                
                conn1 = sqlite3.connect('assets/DataBases/OnePersMsgByID.db')
                c1 = conn1.cursor()
                c1.execute("SELECT *, oid FROM "+name)
                mt= c1.fetchall()
                conn1.commit()
                conn1.close()
                
                self.msg=''
                self.dt = ' '
                self.tm = ' '
                self.rd = 0
                
                for j in mt:
                    self.msg = j[1]
                    if (j[2] is not None) :
                        date = datetime.datetime.strptime(j[2], '%m/%d/%Y %I:%M%p')
                       
                        self.tm = datetime.datetime.strftime(date,'%I:%M %p')
                        self.dt = datetime.datetime.strftime(date,'%m/%d/%Y %I:%M %p')
                        
                    self.rd = j[5]
                    
                conn2 = sqlite3.connect('assets/DataBases/Contact_data.db')
                c2 = conn2.cursor()
                c2.execute("UPDATE CHAT_LIST_DATA SET Last_Message = "+"'"+self.msg+"'"+"WHERE Id = "+str(i[0]))
                c2.execute("UPDATE CHAT_LIST_DATA SET Time = "+"'"+str(self.dt)+"'"+" WHERE Id = "+str(i[0]))
                c2.execute("UPDATE CHAT_LIST_DATA SET Read = "+"'"+str(self.rd)+"'"+" WHERE Id = "+str(i[0]))
                c2.execute("UPDATE CHAT_LIST_DATA SET Time = "+"'"+str('00/00/0000 00:00 PM')+"'"+" WHERE Time = ' ' ")
                conn2.commit()
                conn2.close()
               
                if not self.msg == '':
                    lstmsg = self.msg.split('\n')
                    self.msg = ' '.join(lstmsg)
                nl= 12
                
                print(self.msg)
                l = len(self.msg)
                self.rd = i[5]
                if l == 0 :
                    self.msg= 'Hey There...'
                    self.rd = 0
                elif l > nl:
                    
                    self.new_text = ''
                    for k in range(nl):
                        self.new_text = self.new_text + self.msg[k]
                    self.msg = self.new_text+'...'
                else:
                    self.msg = self.msg
                    
           
                user_data = {
                    "id":i[0],
                    "name": i[1],
                    "last_msg":self.msg,
                    "time": self.tm ,
                    "date":self.dt,
                    "image": i[4],
                    "read": self.rd,
                    "on_release": lambda x=i[0]: self.to_chat_bub(x),
                    }
                
                self.users_data.append(user_data)


            leng = len(self.users_data)
            for l in range(leng):
                if self.users_data[l]['last_msg'] is not None:
                    for m in range(0, leng-l-1):
                        if self.users_data[m+1]["date"] == ' ':
                            self.users_data[m+1]["date"] = '01/12/1111 11:11 PM'
                        n = datetime.datetime.strptime(self.users_data[m]["date"], '%m/%d/%Y %I:%M %p')
                        n1 = datetime.datetime.strptime(self.users_data[m+1]["date"], '%m/%d/%Y %I:%M %p')
                        
                        if n<n1:
                            self.users_data[m],self.users_data[m+1]=self.users_data[m+1],self.users_data[m]
            '''         
            for i in range(leng):
                if self.users_data[i]["time"] == '01/12/1111 11:11 PM':
                    self.users_data[i]["time"] = ' '
                else:
                    obj = datetime.datetime.strptime(self.users_data[i]['time'], '%m/%d/%Y %I:%M %p')
                    st = datetime.datetime.strftime(obj, '%I:%M %p')
                    self.users_data[i]['time']=st
            '''
        
            with open("assets/groups.json") as g:
                self.grps_data = json.load(g)

            for i in self.grps_data:
                await asynckivy.sleep(.1)
                grp_data = {
                    "name": i,
                    "last_msg": self.grps_data[i]["message"],
                    "time": self.grps_data[i]["time"],
                    "image": self.grps_data[i]["image"],
                    
                    
                }
                self.group_data.append(grp_data)
                    
        asynckivy.start((load_users_data()))
        conn.close()
        
    def to_chat_bub(self,id):
        self.anim(1)
        self.manager.set_screen('chat_bub','right')
        self.manager.get_screen('chat_bub').load_data(id)
    def callback_for_menu_items(self, *args):
        toast(args[0])
        
    def to_settings(self):
        self.manager.set_screen("settings",'right')
    def to_nlike(self,scr):
        self.manager.set_screen('ntlike')
        
    def to_search(self):
        if self.ids.boxlay.one == [1,1,1, .7]:
            self.pre_scr = 'chats'
        elif self.ids.boxlay.two == [1, 1, 1, .7]:
            self.pre_scr = 'groups'
        elif self.ids.boxlay.three == [1,1,1, .7]:
            self.pre_scr = 'status'
        else:
            pass
            
        # ///////////////////
        
        self.ids.topp_box.md_bg_color = get_color_from_hex("#3c5148")
        Animation(y=self.height + self.ids.top_box.height, d=0.35).start(self.ids.title_top_bar)
        Animation(y=self.height + self.ids.top_box.height, d=0.35).start(self.ids.s_box)
        Animation(y=self.ids.top_box.y + self.ids.top_box.height/5, d=0.35).start(self.ids.search_input)
        Animation(pos_hint= {'center_y': 0.95}, d=1).start(self.ids.r_box)
        # //////////////////////////
        Animation(x=self.ids.left_bar.width , d=0.35).start(self.ids.search_screen)
        Animation(x=self.width, d=0.35).start(self.ids.chat_screen)
        Animation(x=2*self.width , d=0.35).start(self.ids.grp_screen)
        Animation(x=3*self.width , d=0.35).start(self.ids.status_screen)
        self.ids.boxlay.one = [1, 1, 1, .7]
        self.ids.boxlay.two = [1, 1, 1, .7]
        self.ids.boxlay.three = [1, 1, 1, .7]
        self.ids.search.disabled =True
        # ////////////////////////////
    
    def back_to_search(self):
        ClickableTextFieldRound1.delete_all(self.ids.search_input)
        self.ids.topp_box.md_bg_color = get_color_from_hex("#3c5148")[:3]+[.0]
        self.ids.topp_boxx.md_bg_color = get_color_from_hex("#3c5148")
        Animation(y=self.ids.top_box.y + self.ids.top_box.height/3, d=0.35).start(self.ids.title_top_bar)
        Animation(y=self.ids.top_box.y + self.ids.top_box.height/3 - self.ids.title_top_bar.height/1.9, d=0.35).start(self.ids.s_box)
        Animation(y=self.ids.top_box.y + self.ids.top_box.height, d=0.35).start(self.ids.search_input)
        Animation(pos_hint={'center_y': 1.5}, d=0.5).start(self.ids.r_box)
        self.ids.topp_boxx.md_bg_color = get_color_from_hex("#3c5148")[:3]+[.0]
        # /////////////////////////////////
        if self.pre_scr == 'chats':
            self.show_chat_screen()
        elif self.pre_scr == 'status':
            self.show_status_screen()
        elif self.pre_scr=='groups':
            self.show_grp_screen()
        else:
            pass       

    def show_chat_screen(self):
        self.title = 'Chats'
        self.pre_scr=' '
        Animation(x=-self.width , d=0.35).start(self.ids.search_screen)
        Animation(x=self.ids.left_bar.width, d=0.35).start(self.ids.chat_screen)
        Animation(x=self.width , d=0.35).start(self.ids.grp_screen)
        Animation(x=2*self.width , d=0.35).start(self.ids.status_screen)
        self.ids.boxlay.one = [1, 1, 1, .7]
        self.ids.boxlay.two = get_color_from_hex("#3c5148")
        self.ids.boxlay.three = get_color_from_hex("#3c5148")  
        self.ids.search.disabled =False 
        #self.load_users_data()
        
    def show_grp_screen(self):
        self.title = 'Groups'
        self.pre_scr=' '
        Animation(x=-2*self.width , d=0.35).start(self.ids.search_screen)
        Animation(x=-self.width , d=0.35).start(self.ids.chat_screen)
        Animation(x=self.ids.left_bar.width, d=0.35).start(self.ids.grp_screen)
        Animation(x=self.width , d=0.35).start(self.ids.status_screen)
        self.ids.boxlay.one = get_color_from_hex("#3c5148")  
        self.ids.boxlay.two = [1,1,1,.7]
        self.ids.boxlay.three = get_color_from_hex("#3c5148") 
        self.ids.search.disabled =False
        
        #self.load_users_data()
        
        
    def show_status_screen(self):
        self.title = 'Status'
        self.pre_scr=' '
        Animation(x=-3*self.width , d=0.35).start(self.ids.search_screen)
        Animation(x=-2*self.width , d=0.35).start(self.ids.chat_screen)
        Animation(x=-self.width, d=0.35).start(self.ids.grp_screen)
        Animation(x=self.ids.left_bar.width , d=0.35).start(self.ids.status_screen)
        self.ids.boxlay.one = get_color_from_hex("#3c5148")  
        self.ids.boxlay.two = get_color_from_hex("#3c5148")
        self.ids.boxlay.three = [1,1,1,.7]
        self.ids.search.disabled =True
        
        self.back_to_search()
        #self.load_users_data()
   