import json
import os
import tinydb


def init_parametre_admin():
    db_admin = tinydb.TinyDB('sauvegardes/admin.json')
    db_admin.insert({"title":

        {
            "nom": "adminBasic",
            "tailleFraise ": 0.5
        }}

    )
    return db_admin


def init_parametre_empreinte():
    db_empreinte = tinydb.TinyDB('sauvegardes/empreinte.json')
    return db_empreinte


def get_specific_parameter_admin(nom):
    db_admin = init_parametre_admin()
    recherche = tinydb.Query()
    print(db_admin.all())
    return db_admin.search(recherche.nom == nom)

def get_specific_parameter_empreinte(nom):
    db_empreinte=init_parametre_empreinte()
    recherche=tinydb.Query()
    return db_empreinte.search(recherche.nom==nom)

def get_all_parameter_admin():
    db_admin=init_parametre_admin()
    return db_admin.all()

def get_all_parameter_empreinte():
    db_empreinte = init_parametre_empreinte()
    return db_empreinte.all()

dictionaire = {
    "nom": "parametre3",
    "diametre_fut": "2",
    "hauteur_fut": "2",
    "x_fenetre": "12",
    "y_fenetre": "2",
    "nb_pose": "3"
}

init_parametre_admin()
init_parametre_empreinte()
print(get_all_parameter_admin())
print(get_specific_parameter_admin("adminBasic"))
