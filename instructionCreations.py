import math as math
import json


#def read_param_admin():
 #   fr



class Fraiseuse:
    def __init__(self, positionMax, positionMin):
        self.position = 0
        self.positionMax = positionMax
        self.positionMin = positionMin


class Chariot:
    def __init__(self, xmax):
        self.position = 0
        self.xMax = xmax

    def deplacement(self, distance, direction):
        if (direction == 0):
            self.position = self.position + distance
        else:
            self.position = self.position + distance


class Fut:
    def __init__(self):
        self.position = 0

    # methode de rotation d'angle fut, dependant de la précision

    def rotation(self, angle):
        self.position = self.position + angle


class Carter:
    def __init__(self):
        self.securite = 0

    def erreur_carter(self):
        self.securite = 1


class Machine:
    def __init__(self, fraiseuse, chariot, fut, carter):
        self.fraiseuse = fraiseuse
        self.chariot = chariot
        self.fut = fut
        self.carter = carter


class Empreinte:
    def __init__(self, diam_fut, hauteur_fut, diam_fraiseuse, x_fenetre, y_fenetre, nb_pose):
        self.diam_fut = float(diam_fut)
        self.diam_fraiseuse = float(diam_fraiseuse)
        self.x_fenetre = float(x_fenetre)
        self.y_fenetre = float(y_fenetre)
        self.nb_pose = float(nb_pose)
        self.hauteur_fut = float(hauteur_fut)

    def calcul(self):
        print(self.diam_fraiseuse)

    def surface(self):
        marge_x = float(1)
        marge_y = float(2)

        print("longueur")
        longueur = math.pi * self.diam_fut
        print(longueur)
        print("hauteur")
        print(self.hauteur_fut)
        print("Condition a valider: ")
        print(" ( largeur Y fenetre  + 2 marge Y)  < hauteur fut  ")
        print(self.y_fenetre + 2 * marge_y)
        print(self.hauteur_fut)
        conditionY = (self.y_fenetre + 2 * marge_y) < self.hauteur_fut
        print(conditionY)
        print("----------------------------------")
        print(" nb fenetre * ( largeur X fenetre  X 2 marge X)  < longueur fut  ")
        conditionX = (self.nb_pose * (self.x_fenetre + 2 * marge_x) < longueur)
        print(self.nb_pose * (self.x_fenetre + 2 * marge_x))
        print(longueur)
        print(conditionX)

    def tableau(self):
        i = 0

        while i < self.nb_pose:
            print("----------------------")
            i = i + 1


a = Empreinte(5, 10, 1, 5, 1, 2)
carter = Carter()
chariot = Chariot(10)
fraiseuse = Fraiseuse(1, 0)

fut = Fut()
machine = Machine(fraiseuse, chariot, fut, carter)

# a.calcul()
# a.surface()
a.tableau()
