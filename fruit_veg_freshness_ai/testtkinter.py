import tkinter as tk
from tkinter import filedialog as fd
import cv2
from PIL import ImageTk, Image
import evaluate_image


selected_webcam = 0

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
    is_rotten = evaluate_image.evaluate_rotten_vs_fresh(nom_fichier_photo)
    print(f'Prediction: {is_rotten}', evaluate_image.print_fresh(is_rotten))


def handle_click_photo(event):
    init_photo()

    img2 = ImageTk.PhotoImage(Image.open("img/photo_test.jpg"))
    panel.configure(image=img2)
    panel.image = img2

    window.update()

def handle_click_csv(event):
    filetypes = (
        ('csv files', '*.csv'),
    )
    filename = fd.askopenfilename(title='Open a file',
        initialdir='.',
        filetypes=filetypes )
    print(filename)

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


buttonTP.bind("<Button-1>", handle_click_photo)
buttonCSV.bind("<Button-1>", handle_click_csv)

buttonCSV.pack()
buttonTP.pack()
buttonFLC.pack()
window.mainloop()
