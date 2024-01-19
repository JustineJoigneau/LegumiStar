import os
import wave
from random import randint
import threading
import cv2
import pyaudio
from PIL import Image
import evaluate_image

from customtkinter import CTk, CTkFrame, CTkLabel, CTkOptionMenu, CTkImage, CTkButton, StringVar, CTkToplevel
from midi2audio import FluidSynth

capture = None

def get_camera_ids():
    camera_ids = []

    for i in range(10):
        try:
            cap = cv2.VideoCapture(i)
            if cap.read()[0]:
                camera_ids.append("Caméra " + str(i))
                cap.release()
        except:
            print("Error in camera " + str(i))
    return camera_ids


def change_camera(choice):
    global camera_choice, camera_frame, capture
    camera_choice = int(choice.split(" ")[1])
    capture = cv2.VideoCapture(camera_choice)
    prendre_photo("img.png", camera_choice)
    load_image()


def load_image():
    global camera_frame, window
    camera_frame.destroy()
    camera_frame = CTkFrame(window)
    camera_frame.grid(row=1, column=0, rowspan=4, sticky="nsew")
    camera_frame.grid_columnconfigure(0, weight=1)
    camera_frame.grid_rowconfigure(0, weight=1)
    image_frame = CTkFrame(camera_frame)
    image_frame.grid(row=0, column=0, sticky="nsew")
    image_frame.grid_columnconfigure(0, weight=1)
    image_frame.grid_rowconfigure(0, weight=1)
    img_path = "img.png"
    image = CTkImage(light_image=Image.open(img_path), dark_image=Image.open(img_path), size=(640, 360))
    image_label = CTkLabel(image_frame, image=image, text="")
    image_label.grid(row=0, column=0, sticky="nsew")


def prendre_photo(nom_fichier, index_webcam):
    global capture
    _, image = capture.read()
    cv2.imwrite(nom_fichier, image)


def take_photo():
    global camera_choice
    prendre_photo("img.png", camera_choice)
    load_image()


def analyse_photo():
    global type_star, freshness_star
    if not os.path.exists("img.png"):
        print("Pas d'image à analyser")
        return

    type_star.set(evaluate_image.evaluate_name("img.png"))
    freshness_star.set(evaluate_image.print_fresh(evaluate_image.evaluate_rotten_vs_fresh("img.png")))


def get_midi_files():
    files = []
    for file in os.listdir("midi_files"):
        if file.endswith(".mid"):
            files.append(file[:-4])
    return files


def error_window(text):
    toplevel = CTkToplevel()
    toplevel.title("Erreur")
    toplevel.geometry("500x150")
    toplevel.resizable(False, False)
    toplevel.grid_columnconfigure(0, weight=1)
    toplevel.grid_rowconfigure(0, weight=1)
    toplevel.grab_set()
    lbl = CTkLabel(toplevel, text=text)
    lbl.grid(row=0, column=0, padx=5, pady=5, sticky="we")
    btn = CTkButton(toplevel, text="Ok", command=toplevel.destroy)
    btn.grid(row=1, column=0, padx=5, pady=5, sticky="we")


def sing():
    global music_run, type_star, freshness_star, music_list, button_sing
    type_star_text = type_star.get()
    freshness_star_text = freshness_star.get()
    music_list_text = music_list.get()
    if type_star_text == "???" or freshness_star_text == "???":
        error_window("Veuillez analyser une photo avant de faire chanter la future star")
    else:
        # sf2_file = type_star_text.upper() + "_" + freshness_star_text.upper() + ".sf2" // Ligne quand on aura les sf2 (au bon format)
        sf2_file = "patate.sf2"
        fluidsynth = FluidSynth('sf2/' + sf2_file)
        midi_dir = os.path.join(os.getcwd(), 'midi_files')
        midi_file = os.path.join(midi_dir, music_list_text + '.mid')
        print(midi_file)
        out_dir = os.path.join(os.getcwd(), 'out')
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        out_file = os.path.join(out_dir, music_list_text + '.wav')
        fluidsynth.midi_to_audio(midi_file, out_file)
        t = threading.Thread(target=play_audio, args=(music_list_text,))
        t.start()


def play_audio(music_list_text):
    global stop_thread
    fichier_wav = wave.open('out/' + music_list_text + '.wav', 'rb')
    p = pyaudio.PyAudio()
    flux = p.open(format=p.get_format_from_width(fichier_wav.getsampwidth()),
                  channels=fichier_wav.getnchannels(),
                  rate=fichier_wav.getframerate(),
                  output=True)
    data = fichier_wav.readframes(1024)
    stop_thread = False
    while data and not stop_thread:
        print("play")
        flux.write(data)
        data = fichier_wav.readframes(1024)
    flux.close()
    p.terminate()
    fichier_wav.close()


def stop():
    print("stop")
    global stop_thread
    stop_thread = True


camera_ids = get_camera_ids()
midi_files = get_midi_files()
camera_choice = None
if len(camera_ids) == 0:
    error_window("Aucune caméra détectée")
stop_thread = False
try:
    window = CTk()
    window.title("LegumiStar")
    window.geometry("1280x720")

    # Setup grids
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(4, weight=1)

    # Menu de la liste CTkOptionMenu des caméras
    camera_list_frame = CTkFrame(window)
    camera_list_frame.grid(row=0, column=0, sticky="nsew")
    camera_list_frame.grid_columnconfigure(0, weight=1)
    camera_list_frame.grid_columnconfigure(1, weight=1)
    camera_list_frame.grid_rowconfigure(0, weight=1)
    camera_list_label = CTkLabel(camera_list_frame, text="Choix de la caméra")
    camera_list_label.grid(row=0, column=0, sticky="nsew")
    camera_list = CTkOptionMenu(camera_list_frame, values=camera_ids, command=change_camera)
    camera_list.grid(row=0, column=1)

    # Image de la caméra
    camera_frame = CTkFrame(window)
    camera_frame.grid(row=1, column=0, rowspan=4, sticky="nsew")
    camera_frame.grid_columnconfigure(0, weight=1)
    camera_frame.grid_rowconfigure(0, weight=1)

    # Bouton pour prendre la photo
    button_frame = CTkFrame(window)
    button_frame.grid(row=5, column=0, sticky="nsew")
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_rowconfigure(0, weight=1)
    button = CTkButton(button_frame, text="Prendre la photo", command=take_photo)
    button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Bonton pour analyser la photo
    button_frame = CTkFrame(window)
    button_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_rowconfigure(0, weight=1)
    button = CTkButton(button_frame, text="Analyser la photo", command=analyse_photo)
    button.grid(row=0, column=0)

    # Label pour le type de star
    type_star = StringVar(value='???')
    label_frame = CTkFrame(window)
    label_frame.grid(row=2, column=1, sticky="nsew")
    label_frame.grid_columnconfigure(0, weight=1)
    label_frame.grid_columnconfigure(1, weight=1)
    label_frame.grid_rowconfigure(0, weight=1)
    label = CTkLabel(label_frame, text="Type de star : ")
    label.grid(row=0, column=0, sticky="nse")
    label = CTkLabel(label_frame, textvariable=type_star)
    label.grid(row=0, column=1, sticky="nsw")

    # Label pour la fraicheur
    freshness_star = StringVar(value='???')
    label_frame = CTkFrame(window)
    label_frame.grid(row=3, column=1, sticky="nsew")
    label_frame.grid_columnconfigure(0, weight=1)
    label_frame.grid_columnconfigure(1, weight=1)
    label_frame.grid_rowconfigure(0, weight=1)
    label = CTkLabel(label_frame, text="Etat : ")
    label.grid(row=0, column=0, sticky="nse")
    label = CTkLabel(label_frame, textvariable=freshness_star)
    label.grid(row=0, column=1, sticky="nsw")

    # Menu de la liste CTkOptionMenu pour le choix de la musique
    music_list_frame = CTkFrame(window)
    music_list_frame.grid(row=4, column=1, sticky="nsew")
    music_list_frame.grid_columnconfigure(0, weight=1)
    music_list_frame.grid_columnconfigure(1, weight=1)
    music_list_frame.grid_rowconfigure(0, weight=1)
    music_list_label = CTkLabel(music_list_frame, text="Choix de la musique")
    music_list_label.grid(row=0, column=0, sticky="nsew")
    music_list = CTkOptionMenu(music_list_frame, values=midi_files)
    music_list.grid(row=0, column=1)

    # Bouton faire chanter la future star
    button_frame = CTkFrame(window)
    button_frame.grid(row=5, column=1, sticky="nsew")
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)
    button_frame.grid_rowconfigure(0, weight=1)
    button_sing = CTkButton(button_frame, text="Faire chanter la future star", command=sing)
    button_sing.grid(row=0, column=0)
    button_stop = CTkButton(button_frame, text="Stop", command=stop)
    button_stop.grid(row=0, column=1)

    change_camera(camera_ids[0])
    load_image()
    window.mainloop()

except Exception as e:
    error_window("Une erreur est survenue")
    print(e)