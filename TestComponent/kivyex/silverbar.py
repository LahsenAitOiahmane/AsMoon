from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.window import Window
Window.size = (350, 580)
KV = '''
#:import SliverToolbar __main__.SliverToolbar


<CardItem>
    size_hint_y: None
    width: dp(10)
    adaptive_height: True
    padding: "4dp"
    radius: [-5,16,16,16]
    size_hint:1,None
    size: self.minimum_size
    MDBoxLayout:
        id:boxlay1
        orientation: "vertical"
        adaptive_height: True
        width:dp(100)

        MDLabel:
            id: labb
            text: 'hi how are you leibbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaji'
            font_name: 'assets/fonts/Poppins/Poppins-Regular.ttf'
            font_size: 15
            size_hint_y: None
            multiline:False
            height: self.texture_size[1]  
            adaptive_height:True
            halign: 'left'
            valign: 'top'
           

        MDLabel:
            text: "12:12 AM"
            bold: False
            font_size: 9
            adaptive_height: True
            halign: 'right'
            valign: 'bottom'


MDScreen:

    MDSliverAppbar:
        background_color: "2d4a50"
        toolbar_cls: SliverToolbar()

        MDSliverAppbarHeader:

            MDRelativeLayout:

                FitImage:
                    source: "assets/images/sunset.jpg"

        MDSliverAppbarContent:
            id: content
            orientation: "vertical"
            padding: "12dp"
            spacing: "12dp"
            adaptive_height: True
'''


class CardItem(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.elevation = 0


class SliverToolbar(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.shadow_color = (0, 0, 0, 0)
        # self.type_height = "small"
        # self.title = "LAHSEN AIT OIHMANE"
        # self.font_size = 8
        # self.left_action_items = [["arrow-left", lambda x: x]]
        # self.right_action_items = [
        #     ["attachment", lambda x: x],
        #     ["calendar", lambda x: x],
        #     ["dots-vertical", lambda x: x],
        # ]


class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def on_start(self):
        for x in range(10):
            self.root.ids.content.add_widget(CardItem())


Example().run()