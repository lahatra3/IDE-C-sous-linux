#!/usr/bin/python3
import os
from tkinter import *


fenetre = Tk()
fenetre.title("Develop C")
fenetre.geometry("1200x695")


def lancer():
    nomFile = filename.get() 
    with open("/home/kali/Documents/lahatra_studies/ProjetsTsioryLahatra/Develop-C/files/" + nomFile, "w") as save:
        save.write(editeurTexte.get(1.0, END))
        save.close()
    for item in os.listdir("/home/kali/Documents/lahatra_studies/ProjetsTsioryLahatra/Develop-C/files/"):
        if item == nomFile:
            os.system("x-terminal-emulator && cd /home/kali/Documents/lahatra_studies/ProjetsTsioryLahatra/Develop-C/files/ && gcc " + nomFile + " -o " + "../executables/" + nomFile[:-2] + " -lm && cd ../executables/ && ./" + nomFile[:-2])


champsLabel =  Label(fenetre, text = "Veuillez entrer ici le nom du fichier: ", fg = "green")
champsLabel.pack()

filename = Entry(fenetre, width = 77)
filename.pack(fill = BOTH)

titreEditeur = Label(fenetre, text = "Programme en C", fg = "green", bg = "black")
titreEditeur.pack(fill =  BOTH)

editeurTexte = Text(fenetre, width = 200, height =35)
editeurTexte.pack()

bouttonQuit = Button(fenetre, text = "Quitter", command = fenetre.quit)
bouttonQuit.pack(padx = 10, pady = 0, side = "left")

bouttonCompilation = Button(fenetre, text = "lancer", command = lancer, fg = "green", bg = "black")
bouttonCompilation.pack(side = "right", padx = 10, pady = 0)

fenetre.mainloop()
fenetre.destroy()

