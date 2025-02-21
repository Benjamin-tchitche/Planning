

from utils.model import Model


activites_fields = [
                ('id','INTEGER PRIMARY KEY'),('name','TEXT','UNIQUE'),('color','TEXT'),
                ('icon','TEXT')
            ]

active_settings_fields = [
                ('id','INTEGER PRIMARY KEY'),('activity','TEXT','UNIQUE'),('date','TEXT'),
                ('time_start','TEXT'),('time_end','TEXT'),('title','TEXT'),('description','TEXT'),
                ('repete_id','INTEGER'),('notif','INTEGER')
            ]

repete_settings_fields = [
                ('id','INTEGER PRIMARY KEY'),('active','INTEGER','UNIQUE'),('repete_status','TEXT'),
                ('repete_day_freq','TEXT'),('repete_week_freq','TEXT'),('repete_days_lsit','TEXT'),
                ('categorie','INTEGER')
            ]

notification_fields = [
                ('id','INTEGER PRIMARY KEY'),('time_before','TEXT','UNIQUE')
            ]

base_name = 'databases/planning.db'

Activites = Model(fields=activites_fields, base_name = base_name, name="activite")
Task = Model(fields=active_settings_fields, base_name = base_name, name="task")
Repetition = Model(fields=repete_settings_fields, base_name = base_name, name="repete")
Notification = Model(fields=notification_fields, base_name = base_name, name="notif")
