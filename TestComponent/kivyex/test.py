# import datetime 
# import emoji
# datetime_object = datetime.datetime.today()

# date = datetime.datetime.strftime(datetime_object, '%m/%d/%Y %I:%M %p')
# x = ' is the {}'.format('time')
# date = date + x
# print(date)
# def tri_a_bulle(liste):
#     n = len(liste)

#     for i in range(n):
#         # Le dernier i éléments sont déjà triés, donc on n'a pas besoin de les vérifier
#         for j in range(0, n-i-1):
#             # Traverse la liste de 0 à n-i-1
#             # Swap si l'élément trouvé est plus grand que le suivant
#             if liste[j] > liste[j+1]:
#                 liste[j], liste[j+1] = liste[j+1], liste[j]

# # Exemple d'utilisation
# ma_liste = [64, 34, 25, 12, 22, 11, 90]
# tri_a_bulle(ma_liste)

# print("Liste triée:", ma_liste)

# print(emoji.emojize(":grinning_face_with_big_eyes:"))
# print(emoji.emojize(":winking_face_with_tongue:"))
# print(emoji.emojize(":zipper-mouth_face:"))

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import ILeftBodyTouch, OneLineIconListItem
from kivymd.theming import ThemeManager
from kivymd.utils import asynckivy

Builder.load_string('''
<ItemForList>
    text: root.text

    IconLeftSampleWidget:
        icon: root.icon


<Example@MDFloatLayout>

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: app.title
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            elevation: 4
            left_action_items: [['menu', lambda x: x]]

        MDScrollViewRefreshLayout:
            id: refresh_layout
            refresh_callback: app.refresh_callback
            root_layout: root

            MDGridLayout:
                id: box
                adaptive_height: True
                cols: 1
''')


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class ItemForList(OneLineIconListItem):
    icon = StringProperty()


class Example(MDApp):
    title = 'Example Refresh Layout'
    screen = None
    x = 0
    y = 15

    def build(self):
        self.screen = Factory.Example()
        self.set_list()

        return self.screen

    def set_list(self):
        async def set_list():
            names_icons_list = list(md_icons.keys())[self.x:self.y]
            for name_icon in names_icons_list:
                await asynckivy.sleep(0)
                self.screen.ids.box.add_widget(
                    ItemForList(icon=name_icon, text=name_icon))
        asynckivy.start(set_list())

    def refresh_callback(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            self.screen.ids.box.clear_widgets()
            if self.x == 0:
                self.x, self.y = 15, 30
            else:
                self.x, self.y = 0, 15
            self.set_list()
            self.screen.ids.refresh_layout.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)


Example().run()
