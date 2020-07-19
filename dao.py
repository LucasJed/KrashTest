import json
import os
import tinydb


def init_parametre_admin():
    db_admin = tinydb.TinyDB('sauvegardes/admin.json')
    print(db_admin)
    if (db_admin):
        print("okay")
    else:
        print("init db")
        db_admin.insert(
            {
                'nom': "adminBasic",
                'tailleFraise': 0.5
            }

        )

    return db_admin


def init_parametre_empreinte():
    db_empreinte = tinydb.TinyDB('sauvegardes/empreinte.json')
    if (db_empreinte):
        print("okay")
    else:
        print("init db")
        db_empreinte.insert(
            {
                'nom': "basicTest",
                'diam_fut': 65,
                'hauteur_fut': 111,
                'x_fenetre' : 45,
                'y_fenetre' :100,
                'nb_pose':3
            }

        )
    return db_empreinte


def get_specific_parameter_admin():
    db_admin = init_parametre_admin()
    recherche = tinydb.Query()
    return (db_admin.all())


def get_specific_parameter_empreinte(nom):
    db_empreinte = init_parametre_empreinte()
    recherche = tinydb.Query()
    return db_empreinte.search(recherche.nom == nom)


def get_all_parameter_admin():
    db_admin = init_parametre_admin()
    return db_admin.all()


def get_all_parameter_empreinte():
    db_empreinte = init_parametre_empreinte()
    return db_empreinte.all()


def update_db_admin(selector, param, updated_value):
    '''
    Test so
    '''
    db_admin = init_parametre_admin()
    print(db_admin)
    Admin = tinydb.Query()

    # db.update({'count': 10}, Fruit.type == 'apple')
    db_admin.update({str(param): int(updated_value)}, Admin.nom == str(selector))


dictionaire = {
    "nom": "parametre3",
    "diametre_fut": "2",
    "hauteur_fut": "2",
    "x_fenetre": "12",
    "y_fenetre": "2",
    "nb_pose": "3"
}

db = init_parametre_admin()
db.all()
init_parametre_empreinte()
print(get_all_parameter_admin())
print(get_specific_parameter_admin())
print("laaaaaa")
print(db.tables())
print(db.__getattr__)
update_db_admin( "adminBasic", "tailleFraise",1)
