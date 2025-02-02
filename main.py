

from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

from kivymd.app import MDApp

from componants.componants import *

Builder.load_file("templates/layout.kv")


    
class MainScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.login = True
    
    def on_parent(self, widget, parent):
        if self.login:
            cc = CommonAssistChip(
                    text = 'Travail',
                    icon = 'bat'
                )
            cont = Contener(
                infoText = "BU",
                startTime = "08:30",
                taskBloc = cc
            )
            self.ids['base'].add_widget(cont)
            
            cc = CommonAssistChip(
                    text = 'Télévision',
                    icon = 'youtube-tv'
                )
            cont = Contener(
                infoText = "Maison",
                startTime = "11:30",
                taskBloc = cc
            )
            self.ids['base'].add_widget(cont)
        
        self.login = not self.login
        

class ActiviteScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class PlaningApp(MDApp):
    
    
    def build(self):
        global screen_manager
        
        screen_manager = MDScreenManager()
        
        screen_manager.add_widget(ActiviteScreen(name='activite'))
        screen_manager.add_widget(MainScreen(name='main'))
        
        return screen_manager
    
    


if __name__ == "__main__":
    
    PlaningApp().run()