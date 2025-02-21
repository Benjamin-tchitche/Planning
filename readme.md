
# Chailler de charge 
-[x] création des écrans
    
    [] MainScreen
        ¤ creation de nouveau blocks (tâche)
        ¤ Options
        ¤ Bouton pour revenir à la date du actuelle 
        ¤ parcourir les jours avenir ou passés
        ¤ couleur différent pour le jours J

    [] ActiviteScreen
        ¤ remplir les information automatique (date, heure, notification)

    [x] ActivityCreatorScreen
    
    [] SettingsScreen
        ¤ parametre sur théme
        ¤ parametre sur les notifications 
        ¤ sauvegarde
        
[] création de la base de donnés

[] Effet visuelle de survole et click des composents

## hirarchie

### fichiers

package  componants

| module | class |
|:--------:|:-----:|
|**block_componants**| |
| |Quotidien|
| |Hebdomadaire|
| |Mensuelle|
| |RepeteBlock (main class)|
|-|-|
|**componants**| |
| |CommonAssistChip|
| |Contener|
| |ActivityChip|
| |DatePicker|
| |TimePicker|
| |CustomeDropOptions|
|-|-|
|**custom_componants**| |
| |CustomTextField|
| |CustomIconVeiw|
|-|-|
|**dialog_activity_selector**| |
| |DialogActivitySelector|


* utils.icons_files
    * get_icons() -> return icons images in assets/icons

* utils.path_manager
    * get_asset_path() -> return projet assets path
    * get_icons_path() -> return projet assets icon path
    * get_assets(path) > return absolute for reletive assets directories


## les parametres d'une activité
* activite_name
* activite_color
* activite_icon

## les parametres de l'activité programée

* activite_name 
* date
* time_start
* time_end
* titre
* description
* repeter 
    * repete_status
    * repete_day_freq
    * repete_week_freq
    * repete_days_lsit
    * categorie

## base de données
* activites 

    id | name | color | icon 

* active_settings

    id | activity | date | time_start | time_end | titre | description | repete_id | notif

* repete_settings

    id | active | repete_status | repete_day_freq | repete_week_freq | repete_days_lsit | categorie

* notification

    id | time_before | 