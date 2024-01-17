import cv2
from datetime import datetime
import keyboard
import evaluate_image



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

def traiter_image(nom_fichier):
    # Charger l'image depuis le fichier
    image = cv2.imread(nom_fichier)

    # Appliquer un traitement d'image (par exemple, convertir en niveaux de gris)
    image_traitee = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Enregistrer l'image traitée
    nom_fichier_traite = "img/image_traitee.jpg"
    cv2.imwrite(nom_fichier_traite, image_traitee)

    print(f"Image traitée enregistrée sous {nom_fichier_traite}")



def init_photo():
    

    now = datetime.now()
    time_now = now.strftime("%Y%m%d_%H%M%S")

    nom_fichier_photo = "img/photo_" + str(time_now) + ".jpg"
    prendre_photo(nom_fichier_photo)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    is_rotten = evaluate_image.evaluate_rotten_vs_fresh(nom_fichier_photo)
    print(f'Prediction: {is_rotten}', evaluate_image.print_fresh(is_rotten))



if __name__ == "__main__":
    keyboard.on_press_key("enter", lambda e: init_photo())

    # Maintenez le programme en cours d'exécution
    keyboard.wait("esc")  # Attend la touche "esc" pour quitter le programme

    # Libérez les ressources après avoir terminé
    keyboard.unhook_all()

    # traiter_image(nom_fichier_photo)
