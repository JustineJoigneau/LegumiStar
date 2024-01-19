import cv2
import numpy as np
from keras.models import load_model
import tensorflow as tf
import keras.utils as image



def print_fresh(res):
    threshold_fresh = 0.50
    if res < threshold_fresh:
        return "fresh"
    else:
        return "not_fresh"


def pre_proc_img(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)
    img = cv2.resize(img, (100, 100))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Preprocess the image
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def evaluate_rotten_vs_fresh(image_path):
    # Load the trained model
    model = load_model('./rottenvsfresh98pval.h5')

    # Read and process and predict
    prediction = model.predict(pre_proc_img(image_path))

    return prediction[0][0]

def evaluate_name(image_path):

    model = tf.keras.models.load_model('finetuned_inceptionv3_model.h5')
    img_path = image_path
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.
    # Make a prediction
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    class_labels = ["apple", "banana", "beetroot", "bell pepper", "cabbage", "capsicum", "carrot", "cauliflower", "chilli pepper", "corn", "cucumber", "eggplant", "garlic", "ginger", "grapes", "jalepeno", "kiwi", "lemon", "lettuce", "mango", "onion", "orange", "paprika", "pear", "peas", "pineapple", "pomegranate", "potato", "raddish", "soy beans", "spinach", "sweetcorn", "sweetpotato", "tomato", "turnip", "watermelon"]

    predicted_class = class_labels[predicted_class_index] # assuming you have the train_generator
    return predicted_class
