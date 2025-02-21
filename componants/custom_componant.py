
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard


Builder.load_file("componants/styles/custom_style.kv")

class CustomTextField(MDTextField):
    pass

class CustomIconVeiw(MDCard):
    source = StringProperty()
    OnSelect = ObjectProperty()
    
    def isselect(self):
        self.OnSelect(self.source)
    