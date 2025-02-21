
from kivy.lang import Builder
from kivy.properties import StringProperty,ObjectProperty,ListProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.button import MDFlatButton



KV = '''
<Item>

    ImageLeftWidget:
        source: root.source

'''

Builder.load_string(KV)

class Item(OneLineAvatarListItem):
    OnSelect = ObjectProperty()
    source = StringProperty()
    
    def on_press(self):
        self.OnSelect(self.text)
    
class DialogActivitySelector(MDBoxLayout):
    OnNewClick = ObjectProperty()
    OnActiveClick = ObjectProperty()
    data = ListProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None
        self.icon_to_show = []
        
    def open(self):
        self.dialog = MDDialog(
            title="Sélectioner une activité",
            size_hint = (0.7,0.6),
            type="simple",
            items=[
                Item(text= tp[1], source = tp[0],OnSelect = lambda x : self.OnActiveClick(x)) for tp in self.data
            ],
            buttons=[
                MDFlatButton(
                    text="Annuler",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = lambda x : self.cancel()
                ),
                MDFlatButton(
                    text="Nouvelle activité",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.on_new_click
                ),
                ],
            )
        self.dialog.open()
 
        
    def on_new_click(self,*args):
        self.OnNewClick()
    
    def cancel(self):
        self.dialog.dismiss()
        

