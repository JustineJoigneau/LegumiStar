import cv2
import numpy as np
from keras.models import load_model


def print_fresh(res):
    threshold_fresh = 0.50
    threshold_medium = 0.7
    if res < threshold_fresh:
        print("It is fresh!")
    elif threshold_fresh < res < threshold_medium:
        print("It is medium fresh")
    else:
        print("It is not fresh")


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
    model = load_model('/home/youssef/Documents/fruit-veg-freshness-ai/rottenvsfresh98pval.h5')

    # Read and process and predict
    prediction = model.predict(pre_proc_img(image_path))

    return prediction[0][0]


# Example usage:
img_path = '/home/youssef/Downloads/freshapple.jpeg'
is_rotten = evaluate_rotten_vs_fresh(img_path)
print(f'Prediction: {is_rotten}',print_fresh(is_rotten))
