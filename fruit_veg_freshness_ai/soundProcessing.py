import csv
from scipy.io.wavfile import write
import numpy as np
from pydub import AudioSegment
import librosa
import librosa.display
import soundfile as sf
import os

def csv_to_wav(csv_file, raw_number, wav_file, frequency=1000):
    """
    Convertit une colonne spécifique d'un fichier CSV en un fichier WAV.
    :param csv_file: Chemin vers le fichier CSV.
    :param raw_number: Index de la colonne à convertir (indexation à partir de 0).
    :param wav_file: Nom du fichier WAV de sortie.
    :param frequency: Fréquence d'échantillonnage pour le fichier WAV.
    """
    try:
        data = []
        with open(csv_file, 'r') as fichier:
            lecteur_csv = csv.reader(fichier)
            for i, line in enumerate(lecteur_csv):
                if i > 1:  # Ignorer les en-têtes
                    try:
                        value = float(line[raw_number])
                        data.append(value)
                    except ValueError:
                        raise ValueError(f"La valeur {line[raw_number]} n'est pas un nombre valide")

        data_np = np.array(data, dtype=np.float32)
        data_np = np.int16(data_np / np.max(np.abs(data_np)) * 32767)
        write(wav_file, frequency, data_np)

    except Exception as e:
        print(f"Une erreur est survenue : {e}")


def csv_to_wav_extract_sound(csv_file, raw_number1, raw_number2, wav_file, frequency=1000):
    """
    Calcul de la différence entre deux colonnes d'un fichier CSV et conversion en un fichier WAV.
    :param csv_file: Chemin vers le fichier CSV.
    :param raw_number1: Index de la première colonne (indexation à partir de 0).
    :param raw_number2: Index de la colonne deuxième colonne à soustraire (indexation à partir de 0).
    :param wav_file: Nom du fichier WAV de sortie.
    :param frequency: Fréquence d'échantillonnage pour le fichier WAV.
    """
    try:
        data = []
        with open(csv_file, 'r') as fichier:
            lecteur_csv = csv.reader(fichier)
            for i, line in enumerate(lecteur_csv):
                if i > 1:  # Ignorer les en-têtes
                    try:
                        value = float(line[raw_number1])-float(line[raw_number2])
                        data.append(value)
                    except ValueError:
                        raise ValueError(f"Une des valeurs n'est pas un nombre valide")

        data_np = np.array(data, dtype=np.float32)
        data_np = np.int16(data_np / np.max(np.abs(data_np)) * 32767)
        write(wav_file, frequency, data_np)

    except Exception as e:
        print(f"Une erreur est survenue : {e}")


def extend_audio(input_file, output_file, target_duration):
    """
    Permet d'étendre la durée d'un fichier audio.
    :param input_file: Fichier d'entrée.
    :param output_file: Fichier de sortie.
    :param target_duration: Durée supplémentaire de l'audio souhaitée.
    """
    audio = AudioSegment.from_file(input_file)
    # Calculer le nombre de répétitions nécessaires pour atteindre la durée cible
    num_repetitions = int(target_duration / (len(audio) / 1000)) + 1
    # Répéter le fichier audio
    extended_audio = audio * num_repetitions
    # Tronquer le fichier audio à la durée cible
    extended_audio = extended_audio[:target_duration * 1000]
    extended_audio.export(output_file, format="wav")


def mix_audio_librosa(file1, file2, output_file, mix_ratio=0.5):
    """
    Modification d'un fichier audio à partir d'un autre avec la bibliothèque librosa.
    :param file1: Fichier son à modifier.
    :param file2: Fichier bruit.
    :param output_file: Fichier de sortie.
    :param mix_ratio: Ratio de modification compris entre 0 et 1.
    """
    # Charger les fichiers audio avec une fréquence d'échantillonnage spécifiée 
    audio1, sr = librosa.load(file1, sr=11025)
    audio2, sr = librosa.load(file2, sr=11025)

    # Ajuster la longueur des deux tableaux pour qu'ils aient la même longueur
    min_length = min(len(audio1), len(audio2))
    audio1 = audio1[:min_length]
    audio2 = audio2[:min_length]

    # Mélanger les signaux
    mixed_audio = mix_ratio * audio1 + (1 - mix_ratio) * audio2

    # Normaliser le résultat entre -1 et 1
    mixed_audio /= np.max(np.abs(mixed_audio))

    # Exporter le fichier mixé
    sf.write(output_file, mixed_audio, sr)


def apply_phase_inversion(signal):
    """ Inverse la phase d'un signal audio. """
    return -signal

def apply_frequency_modulation(signal, rate, depth=0.01, freq=2):
    """ Applique une modulation de fréquence à un signal audio. """
    t = np.linspace(0, len(signal) / rate, num=len(signal))
    modulator = np.sin(2 * np.pi * freq * t) * depth
    modulated_signal = signal * modulator
    return modulated_signal



def convertPianoNote(noise_file, note_directory, legume, ratio):
    """
    Crée les notes modifiées à partir d'un bruit de légume.
    :param noise_file: Fichier audio contennat le bruit.
    :param note_directory: Répertoire contenant les notes de piano. Attention bien ajouter "/" à la fin.
    :param legume: Nom du légume utilisé.
    :param ratio: Ratio de modification compris entre 0 et 1.
    """
    index = 21
    for i in range(88):
        note = index+i
        filename = str(note_directory) + str(note) + ".mp3"
        output_directory = str(legume) + "/"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        output_filename = output_directory + str(note) + ".mp3"
        mix_audio_librosa(filename, noise_file, output_filename, ratio)
    print(f"Conversion des notes de piano terminée pour le légume {legume}!")
