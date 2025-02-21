
from kivy.lang import Builder
from kivy.properties import StringProperty,ObjectProperty, ListProperty, BooleanProperty

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
    startTime = StringProperty("")
    endTime = StringProperty("")
    taskBloc = ObjectProperty()
    OnButtonClick = ObjectProperty()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.login = True
    
    def on_parent(self, widget, parent):
        if self.login:
            if isinstance(self.taskBloc, CommonAssistChip):
                self.ids['chiplace'].add_widget(self.taskBloc)
        
        self.login = not self.login
    
    def onClick(self):
        if self.OnButtonClick:
            self.OnButtonClick()

class ActivityChip(MDChip):
    text = StringProperty("Activité")
    icon = StringProperty()
    destroyed = BooleanProperty(False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def close(self):
        if self.destroyed:
            self.parent.remove_widget(self)
    
        
class DatePicker(MDBoxLayout):
    text = StringProperty()
    htext = StringProperty('Date')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_text(self):
        return self.ids.date_input.text
        
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
    text = StringProperty()
    htext = StringProperty('Début')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_text(self,*args):
        return self.ids.time_input.text
        
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
    text = StringProperty("Ne pas répéter")
    options = ListProperty(["Ne pas répéter","Quotidiennement","Hebdomadaire","Mensuellement","Annuellement"])
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_text(self):
        return self.ids.option_input.text
        
    def open_options(self, item):
        menu_items = [
            {
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in self.options]
        self.menu = MDDropdownMenu(caller=item, items=menu_items)
        
        self.menu.open()

    def menu_callback(self, text_item):
        self.text = text_item
        self.ids.option_input.text = text_item
        self.menu.dismiss()
        
    def select_action(self,x):
        if x.focus:
            self.open_options(x)