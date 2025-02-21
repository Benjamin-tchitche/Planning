

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.utils import get_hex_from_color

from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.pickers.colorpicker import MDColorPicker
from kivymd.app import MDApp

from componants.componants import *
from componants.block_componants import *
from componants.custom_componant import *
from componants.dialog_activity_selector import *
from utils.icons_files import get_icons
from utils.databases import (
    Activites,
    Notification,
    Task,
    Repetition
)

from typing import Union
import os
import plyer


app_base_path = plyer.storagepath.get_application_dir()

Builder.load_file("templates/layout.kv")

# =======================================

Edit_data = {}

# =======================================
    
class MainScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.login = True
    
    def on_parent(self, widget, parent):
        if self.login:
            
            cont = Contener(
                infoText = "",
                startTime = "00:00",
                OnButtonClick = self.create
            )
            self.ids['task_creator'].add_widget(cont)
        
        
        self.login = not self.login
        
    def create(self):
        screen_manager.current = 'activite'
        
        
class ActiviteScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.login = True
        self.selector = None
        self.Activity_data = [("assets/icons/05.png",'Travail'),("assets/icons/02.png",'Diné'),
                              ('assets/icons/01.png','Sport'),('assets/icons/08.png','Docteur')
                             ]
    
    def on_parent(self, widget, parent):
        if self.login:
            pass
        
        self.login = not self.login
    
    
        
    def slect_activity(self):
        self.selector = DialogActivitySelector(data = self.Activity_data, OnNewClick=self.newActivity,
                                          OnActiveClick = self.IsSelected)
        self.selector.open()
    
    def IsSelected(self, name):
        self.selector.cancel()
        self.ids['active_act'].add_widget(ActivityChip(
            text=name,
            destroyed = True
        ))
    
    def newActivity(self):
        self.selector.cancel()
        screen_manager.current = "activitycreator"

    def load_data(self):
        activs = ''.join([ch.text + ',' for ch in self.ids['active_act'].children])
        Edit_data['activite_name'] = activs
        Edit_data['date'] = self.ids['date'].get_text()
        Edit_data['time_start'] = self.ids['time_start'].get_text()
        Edit_data['time_end'] = self.ids['time_end'].get_text()
        Edit_data['titre'] = self.ids['titre'].text
        Edit_data['description'] = self.ids['description'].text
        Edit_data.update(self.ids['repeter'].get_values())
        
        

        Task.add(activity = Edit_data['activite_name'],
                 date = Edit_data['date'],
                 time_start = Edit_data['time_start'],
                 time_end = Edit_data['time_end'],
                 title = Edit_data['titre'],
                 description = Edit_data['description'],
                 repete_id = 1,
                 notif = 1,
                 )
        
        id = Task.get(activity = Edit_data['activite_name'])[0].id
        Repetition.add(
            active = id,
            categorie = Edit_data['categorie'] ,
            repete_status = Edit_data['repete_status'],
            repete_day_freq = Edit_data['repete_day_freq'],
            repete_week_freq = Edit_data['repete_week_freq'],
            repete_days_lsit = ''.join([j + ',' for j in Edit_data['repete_days_lsit']])
        )
        
        screen_manager.current = 'main'
    
    
    def close(self):
        screen_manager.current = 'main'

class ActivityCreatorScreen(MDScreen):
    select_icon = StringProperty()
    select_color = StringProperty('teal')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.login = True 
    
    def on_parent(self, widget, parent):
        if self.login:
            icons = get_icons()
            for icon in icons:
                self.ids['icons_box'].add_widget(CustomIconVeiw(
                    source = icon,
                    OnSelect = lambda x : self.icon_selected(x)
                ))
            
        self.login = not self.login 

    def icon_selected(self, name):
        self.select_icon = name 
        
    def color_selector(self):
        color_picker = MDColorPicker(size_hint=(0.45, 0.85))
        color_picker.open()
        color_picker.bind(
            on_select_color=self.on_select_color,
            on_release=self.get_selected_color,
        )

    def update_color(self, color: list) -> None:
        self.root.ids.toolbar.md_bg_color = color

    def get_selected_color(
        self,
        instance_color_picker: MDColorPicker,
        type_color: str,
        selected_color: Union[list, str],
    ) -> None:

        self.select_color = get_hex_from_color(selected_color)
        instance_color_picker.dismiss()
        self.ids['color_flag'].md_bg_color = selected_color

    def on_select_color(self, instance_gradient_tab, color: list) -> None:
        '''Called when a gradient image is clicked.'''

    def validate(self):
        Edit_data['activite_name'] =  self.ids['name'].text
        Edit_data['activite_color'] = self.select_color
        Edit_data['activite_icon'] = self.select_icon
        
        Activites.add(
            name = Edit_data['activite_name'],
            color = Edit_data['activite_color'],
            icon = Edit_data['activite_icon']
        )
        
        self.cancel_and_back()
    
    def cancel_and_back(self):
        screen_manager.current = 'activite'
        screen_manager.transition.direction = 'right'

class PlaningApp(MDApp):
    
    
    def build(self):
        global screen_manager
        
        screen_manager = MDScreenManager()
        
        screen_manager.add_widget(MainScreen(name='main'))
        screen_manager.add_widget(ActiviteScreen(name='activite'))
        screen_manager.add_widget(ActivityCreatorScreen(name='activitycreator'))
        
        return screen_manager
    
    def on_start(self):
        if not os.path.exists(os.path.join(app_base_path, "databases/planning.db")):
            Task.create()
            Activites.create()
            Repetition.create()
            Notification.create()
            
            for tp in [("assets/icons/05.png",'Travail','#9f1bb9'),("assets/icons/02.png",'Diné','#179fa8'),('assets/icons/01.png','Sport','#fc5320'),('assets/icons/08.png','Docteur','#1bb95d')]:
                Activites.add(
                    name = tp[1],
                    color = tp[2],
                    icon = os.path.join(app_base_path, tp[0])
                )
                
    
    


if __name__ == "__main__":
    
    PlaningApp().run()