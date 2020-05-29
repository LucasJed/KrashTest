import math as math


class Empreinte:
    def __init__(self, diam_fut, hauteur_fut, diam_fraiseuse,x_fenetre,y_fenetre,nb_pose ):
        self.diam_fut=float(diam_fut)
        self.diam_fraiseuse=float(diam_fraiseuse)
        self.x_fenetre=float(x_fenetre)
        self.y_fenetre=float(y_fenetre)
        self.nb_pose=float(nb_pose)
        self.hauteur_fut=float(hauteur_fut)

    def calcul(self):
        print(self.diam_fraiseuse)

    def surface(self):
        marge_x=float(1)
        marge_y=float(2)

        print ("longueur")
        longueur = math.pi * self.diam_fut
        print(longueur)
        print("hauteur")
        print(self.hauteur_fut)
        print("Condition a valider: ")
        print(" ( largeur Y fenetre  + 2 marge Y)  < hauteur fut  ")
        print(self.y_fenetre + 2 *marge_y )
        print(self.hauteur_fut)
        conditionY=  (self.y_fenetre + 2 *marge_y ) < self.hauteur_fut
        print(conditionY)
        print("----------------------------------")
        print(" nb fenetre * ( largeur X fenetre  X 2 marge X)  < longueur fut  ")
        conditionX= ( self.nb_pose * (self.x_fenetre + 2 *marge_x ) < longueur)
        print(self.nb_pose * (self.x_fenetre + 2 *marge_x ))
        print(longueur)
        print(conditionX)




a = Empreinte(5, 10, 1, 5, 1, 2)



a.calcul()
a.surface()