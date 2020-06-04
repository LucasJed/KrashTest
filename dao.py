import json

def import_fichier():
    with open("data_file.json",'r',encoding='utf-8') as sauv:
        return(json.loads(sauv.read()))

def liste_parametres_administrateur():
    print(import_fichier())



liste_parametres_administrateur()