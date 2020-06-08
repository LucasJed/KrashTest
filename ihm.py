import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
import os
import instructionCreations
import dao


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # Liste des pages disponibles
        for F in (
                HomePage, RecentsPage, ParamsPage, AdminPage, ValidationPage, ProcessingPage, ErrorProcessPage,
                EndProcessPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    # Cette fonction permet d'ouvrir une nouvelle fenetre avec des parametres
    def show_frame_arg(self, page_name, arg):
        frame = self.frames[page_name]
        frame.tkraise()
        if arg:
            frame.arg = arg


# home -> (motifs recents, parametres, admin) (HomePage)

class HomePage(tk.Frame):

    def helloCallBack(self):
        # os.system('control.py')
        instructionCreations.a.tableau()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Bonjour ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Parametres récents",
                            command=lambda: controller.show_frame("RecentsPage"))
        button2 = tk.Button(self, text="Nouveaux parametres ",
                            command=lambda: controller.show_frame("ParamsPage"))
        button3 = tk.Button(self, text="Parametres administrateur",
                            command=lambda: controller.show_frame("AdminPage"))
        button4 = tk.Button(self, text="Parametres administrateur",
                            command=self.helloCallBack)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()


# motifs recents -> (validation + datas, home) (RecentsPage)

class RecentsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Parametres recents", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        lb1 = tk.Listbox(self)
        list_items = dao.liste_sauvegardes()
        j = 1
        for i in list_items:
            lb1.insert(j, i)
            j = j + 1

        self.selection=""
        validationButton = tk.Button(self, text="Valider les parametres",
                                     command=lambda: [print(lb1.get(lb1.curselection())),
                                                      self.controller.show_frame_arg("ValidationPage",
                                                                                     lb1.get(lb1.curselection()))])
        homeButton = tk.Button(self, text="Go to the start page",
                               command=lambda: controller.show_frame("HomePage"))
        lb1.pack()
        validationButton.pack()
        homeButton.pack()


# Parametres -> (validation + datas, home) (ParamsPage)


class ParamsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Entrer les parametres de la nouvelle emprunte", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        validationButton = tk.Button(self, text="Valider les parametres",
                                     command=lambda: controller.show_frame("ValidationPage"))
        homeButton = tk.Button(self, text="Retour menu",
                               command=lambda: controller.show_frame("HomePage"))
        validationButton.pack()
        homeButton.pack()


# Administrateur -> Home (AdminPage)

class AdminPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Parametres administrateur: \n Taille fraiseuse: \n ...",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Valider et retour au menu ",
                            command=lambda: controller.show_frame("HomePage"))
        button2 = tk.Button(self, text="Ne pas enregistrer",
                            command=lambda: controller.show_frame("HomePage"))
        button1.pack()
        button2.pack()


# Validation forme -> (process, home) (ValidationPage)
class ValidationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Validation en cours", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        #TODO
        #label = tk.Label(self,text=super.)
        button1 = tk.Button(self, text="Lancer l'impression",
                            command=lambda: controller.show_frame("ProcessingPage "))
        button2 = tk.Button(self, text="Erreur, retour au menu",
                            command=lambda: controller.show_frame("HomePage"))

        label.pack()
        button1.pack()
        button2.pack()


# Proccess -> (end process, error) (PrecessingPage)
class ProcessingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Arret machine: Erreur ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Une erreur s'est produite",
                            command=lambda: controller.show_frame("ErrorProcessingPage"))
        button2 = tk.Button(self, text="Fin de process",
                            command=lambda: controller.show_frame("EndProcessPage"))
        button1.pack()
        button2.pack()


# Error -> a definir  (ErrorProcessPage)
class ErrorProcessPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Impression de l'emprunte en cours", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Une erreur s'est produite",
                            command=lambda: controller.show_frame("Retour au menu"))

        button1.pack()


# EndProcessPage -> homepage (ErrorProcessPage)
class EndProcessPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="L'impression s'est bien passée. ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Retour au menu",
                            command=lambda: controller.show_frame("HomePage"))

        button1.pack()


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    root = tk.Tk()
    app = FullScreenApp(root)
    root.mainloop()
