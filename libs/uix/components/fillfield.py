from kivymd.uix.textfield import MDTextField
from kivy.utils import get_color_from_hex
KV='''

'''
class FillField(MDTextField):
    """It is just a base class for a text field with common parameters."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = None
        self.width = "320dp"
        # self.hint_text = 'Rectangle mode'
        # self.mode = "fill"
        self.text_color_focus = get_color_from_hex('#feada6')
        self.text_color_normal = get_color_from_hex('#feada6')[:3] + [.7]
        self.line_color_normal = get_color_from_hex('#feada6')[:3] + [.5]
        self.line_color_focus = get_color_from_hex('#feada6')
        self.icon_left_color_focus = get_color_from_hex('#feada6')[:3] + [.5]
        self.icon_left_color_normal = get_color_from_hex('#feada6')[:3] + [.3]
        self.hint_text_color_focus = get_color_from_hex('#feada6')[:3] + [.5]
        self.hint_text_color_normal = get_color_from_hex('#feada6')[:3] + [.5]
        
        self.fill_color_normal = (1, 1, 1, 0.1)
        self.fill_color_focus = (1, 1, 1, 0.3)