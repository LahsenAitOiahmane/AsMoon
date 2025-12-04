from kivy.animation import Animation
from kivy.lang import Builder
from kivy.utils import get_color_from_hex

from kivymd.app import MDApp
from kivymd.uix.list import TwoLineAvatarListItem

KV = '''
<MyItem>
    text: "Two-line item with avatar"
    secondary_text: "Secondary text here"
    _no_ripple_effect: True

    ImageLeftWidget:
        source: "data/logo/kivy-icon-256.png"


MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        id: toolbar
        title: "Inbox"
        left_action_items: [["menu"]]
        right_action_items: [["magnify"], ["dots-vertical"]]
        md_bg_color: 0, 0, 0, 1

    MDBoxLayout:
        padding: "24dp", "8dp", 0, "8dp"
        adaptive_size: True

        MDLabel:
            text: "Today"
            adaptive_size: True

    ScrollView:

        MDSelectionList:
            id: selection_list
            spacing: "12dp"
            overlay_color: app.overlay_color[:-1] + [.2]
            icon_bg_color: app.overlay_color
            on_selected: app.on_selected(*args)
            on_unselected: app.on_unselected(*args)
            on_selected_mode: app.set_selection_mode(*args)
'''


class MyItem(TwoLineAvatarListItem):
    pass


class Example(MDApp):
    overlay_color = get_color_from_hex("#6042e4")

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(10):
            self.root.ids.selection_list.add_widget(MyItem())

    def set_selection_mode(self, instance_selection_list, mode):
        if mode:
            md_bg_color = self.overlay_color
            left_action_items = [
                [
                    "close",
                    lambda x: self.root.ids.selection_list.unselected_all(),
                ]
            ]
            right_action_items = [["trash-can"], ["dots-vertical"]]
        else:
            md_bg_color = (0, 0, 0, 1)
            left_action_items = [["menu"]]
            right_action_items = [["magnify"], ["dots-vertical"]]
            self.root.ids.toolbar.title = "Inbox"

        Animation(md_bg_color=md_bg_color, d=0.2).start(self.root.ids.toolbar)
        self.root.ids.toolbar.left_action_items = left_action_items
        self.root.ids.toolbar.right_action_items = right_action_items

    def on_selected(self, instance_selection_list, instance_selection_item):
        self.root.ids.toolbar.title = str(
            len(instance_selection_list.get_selected_list_items())
        )

    def on_unselected(self, instance_selection_list, instance_selection_item):
        if instance_selection_list.get_selected_list_items():
            self.root.ids.toolbar.title = str(
                len(instance_selection_list.get_selected_list_items())
            )


Example().run()