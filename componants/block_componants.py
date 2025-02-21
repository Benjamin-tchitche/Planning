
from kivy.lang import Builder
from kivy.properties import StringProperty,ObjectProperty, ListProperty

from kivymd.uix.boxlayout import MDBoxLayout


Builder.load_file("componants/styles/block_componant.kv")

class Quotidien(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_text(self) -> str:
        return self.ids["freq_day"].text
    
class Hebdomadaire(MDBoxLayout):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.days_list = {'l': False, 'm': False, 'me': False, 'j':False, 'v': False, 's': False,'d': False}
    
    def ispressed(self,x,id):
        self.days_list[id] = not self.days_list[id]
        self.colorate()
    
    def colorate(self):
        for l in self.days_list:
            if self.days_list[l]:
                self.ids[l].md_bg_color = "#1bb95d"
            else:
                self.ids[l].md_bg_color = "brown"
    
    def get_select_days(self):
        return [j for j in self.days_list if self.days_list[j]== True]
        
    def get_text(self) -> str:
        return self.ids["freq_week"].text
        
class Mensuelle(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
class RepeteBlock(MDBoxLayout):
    repeteOptions = {}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.categorie = ''
    
    def get_values(self) -> dict:
        self.repeteOptions["repete_status"] = self.ids.repeter_status.get_text()
        
        if self.categorie == 'quotidien':
            self.repeteOptions["repete_day_freq"] = self.ids['dynamic_inputer'].ids['quotidien'].get_text()
            self.repeteOptions["repete_week_freq"] = ''
            self.repeteOptions["repete_days_lsit"] = []
            
        elif self.categorie == 'hebdomadaire':
            self.repeteOptions["repete_week_freq"] = self.ids['dynamic_inputer'].ids['hebdomadaire'].get_text()
            self.repeteOptions["repete_days_lsit"] = self.ids['dynamic_inputer'].ids['hebdomadaire'].get_select_days()
            self.repeteOptions["repete_day_freq"] = ''
            
        return self.repeteOptions
        
    def check_reload(self,x):
        self.ids['dynamic_inputer'].clear_widgets()
        
        if x.text == "Quotidiennement":
            q = Quotidien()
            self.ids['dynamic_inputer'].add_widget(q)
            self.ids['dynamic_inputer'].ids['quotidien'] = q
            self.categorie = "quotidien"
        elif x.text == "Hebdomadaire":
            h = Hebdomadaire()
            self.ids['dynamic_inputer'].add_widget(h)
            self.ids['dynamic_inputer'].ids['hebdomadaire'] = h
            self.categorie = "hebdomadaire"
            
        self.repeteOptions["categorie"] = self.categorie
            