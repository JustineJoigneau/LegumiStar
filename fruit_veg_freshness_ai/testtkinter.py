import tkinter as tk
import cv2
from PIL import ImageTk, Image

selected_webcam = 0

def select_webcam():
    for i in range(3):
        capture = cv2.VideoCapture(i)
        _, image = capture.read()
        cv2.imwrite("img/testcam" + str(i) , image)
        capture.release()
        img2 = ImageTk.PhotoImage(Image.open("img/testcam" + str(i) + ".jpg"))
        panel.configure(image=img2)
        panel.image = img2

        #afficher les 3 photos avec un bouton a coté de chacun avec les fonctions cami pour chaque bouton
def Cam1():
    return 1

def Cam2():
    return 2

def Cam3():
    return 3

def prendre_photo(nom_fichier):
    # Initialiser la capture vidéo
    capture = cv2.VideoCapture(1)

    # Lire une image depuis la webcam
    _, image = capture.read()

    # Enregistrer l'image
    cv2.imwrite(nom_fichier, image)

    # Libérer la ressource de la webcam
    capture.release()

    print(f"Photo enregistrée sous {nom_fichier}")

def init_photo():
    nom_fichier_photo = "img/photo_" + "test" + ".jpg"
    prendre_photo(nom_fichier_photo)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

def handle_click(event):
    init_photo()

    img2 = ImageTk.PhotoImage(Image.open("img/photo_test.jpg"))
    panel.configure(image=img2)
    panel.image = img2

    window.update()

print("Program started")

window = tk.Tk()
window.geometry("1280x720")

panel = tk.Label(window)
panel.pack(side="bottom", fill="both", expand="yes")

panel1 = tk.Label(window)
panel1.pack()
panel2 = tk.Label(window)
panel2.pack()
panel3 = tk.Label(window)
panel3.pack()

#Faire une liste de panel pour pour acceder a chacun dans select webcam



buttonCSV = tk.Button(text="importer le CSV")
buttonTP = tk.Button(text="Take Picture")

buttonFLC = tk.Button(text="Faites le chanter")


buttonTP.bind("<Button-1>", handle_click)

buttonCSV.pack()
buttonTP.pack()
buttonFLC.pack()
window.mainloop()
