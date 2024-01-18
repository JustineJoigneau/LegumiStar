import tkinter as tk
import cv2
from PIL import ImageTk, Image

selected_webcam = 0

INDEX = 0



def prendre_photo(nom_fichier, index_webcam):
    # Initialiser la capture vidéo
    capture = cv2.VideoCapture(index_webcam)

    # Lire une image depuis la webcam
    _, image = capture.read()

    # Enregistrer l'image
    cv2.imwrite(nom_fichier, image)

    # Libérer la ressource de la webcam
    capture.release()

    print(f"Photo enregistrée sous {nom_fichier}")

def init_photo():
    nom_fichier_photo = "img/photo_" + "test" + ".jpg"
    prendre_photo(nom_fichier_photo, INDEX)
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

def CamIndex():
    # vérifie les 10 premiers index et retourne une liste d'index qui sont associés à une webcam
    index = 0
    l = []
    i = 4
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            l.append(index)
            cap.release()
        index += 1
        i -= 1
    return l


def changeWebcam(event):
    global INDEX
    listIndex = CamIndex()
    for elt in listIndex:
        if INDEX == elt and INDEX != listIndex[-1]:
            INDEX = listIndex[listIndex.index(elt)+1]
            break
        else:
            INDEX = listIndex[0]
    print(INDEX)
    handle_click(None)


        



buttonCSV = tk.Button(text="importer le CSV")
buttonChangeWebcam = tk.Button(text="Changer la Webcam")
buttonTP = tk.Button(text="Prendre une photo")

buttonFLC = tk.Button(text="Faites le chanter")




buttonTP.bind("<Button-1>", handle_click)
buttonChangeWebcam.bind("<Button-1>", changeWebcam)
buttonChangeWebcam.bind("<Button-1>", print(INDEX))

buttonCSV.pack()
buttonChangeWebcam.pack()
buttonTP.pack()
buttonFLC.pack()

window.mainloop()
