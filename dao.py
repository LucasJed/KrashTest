import json
import os


def import_fichier():
    with open("data_file.json", 'r', encoding='utf-8') as sauv:
        return (json.loads(sauv.read()))


def liste_parametres_administrateur():
    print(import_fichier())


def ajouter_parametre(dictionary):
    print(dictionary["nom"])
    nom = "sauvegardes/"+dictionary["nom"]+".json"
    with open(nom, "w") as outfile:
        json_object = json.dumps(dictionary, indent=4)

        outfile.write(json_object)

def liste_sauvegardes():
    arr = os.listdir("sauvegardes")
    print(arr)
    return (arr)

dictionaire ={
    "nom": "parametre3",
    "diametre_fut": "2",
    "hauteur_fut": "2",
    "x_fenetre": "12",
    "y_fenetre": "2",
    "nb_pose": "3"
}

ajouter_parametre(dictionaire)
liste_parametres_administrateur()
liste_sauvegardes()