
from kivy.lang import Builder
from kivy.properties import StringProperty,ObjectProperty

from kivymd.uix.chip import MDChip
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers.datepicker import MDDatePicker
from kivymd.uix.pickers.timepicker import MDTimePicker
from kivymd.uix.menu import MDDropdownMenu

Builder.load_file("componants/styles/comps.kv")


class CommonAssistChip(MDChip):
    text = StringProperty()
    icon = StringProperty()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Contener(MDBoxLayout):

    infoText = StringProperty()
    startTime = StringProperty("10:00")
    endTime = StringProperty("11:00")
    taskBloc = ObjectProperty()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.login = True
    
    def on_parent(self, widget, parent):
        if self.login:
            if isinstance(self.taskBloc, CommonAssistChip):
                self.ids['chiplace'].add_widget(self.taskBloc)
        
        self.login = not self.login

class ActivityChip(MDChip):
    text = StringProperty("Activité")
    icon = StringProperty()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class DatePicker(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def select_action(self,x):
        if x.focus:
            self.open()
    
    def open(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        
        date_dialog.open()
    
    def on_save(self, instance, value, date_range):
        text = instance.set_text_full_date(int(str(value).split('-')[0]),int(str(value).split('-')[1]),int(str(value).split('-')[2]),'portrai')
        self.ids['date_input'].text = str(text)
        instance.dismiss()
    
    def on_cancel(self, instance, value):
        instance.dismiss()

class TimePicker(MDBoxLayout):
    htext = StringProperty('Début')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def select_action(self,x):
        if x.focus:
            self.open()
    
    def open(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        
        time_dialog.open()
    
    def on_save(self, instance, value):
        self.ids['time_input'].text = str(value)
        instance.dismiss()
    
    def on_cancel(self, instance, value):
        instance.dismiss()
    
class CustomeDropOptions(MDBoxLayout):
    htext = StringProperty("Répéter")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def open_options(self, item):
        menu_items = [
            {
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in ["Ne pas répéter","Quotidiennement","Hebdomadaire","Mensuellement","Annuellement"]
        ]
        self.menu = MDDropdownMenu(caller=item, items=menu_items)
        
        self.menu.open()

    def menu_callback(self, text_item):
        self.ids.option_input.text = text_item
        self.menu.dismiss()
        
    def select_action(self,x):
        if x.focus:
            self.open_options(x)