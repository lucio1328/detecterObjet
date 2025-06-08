import cv2
import numpy as np

def preprocess_image(image, target_size=(224, 224)):
    # Redimensionner l'image
    image = cv2.resize(image, target_size)

    # Normalisation des pixels
    image = image.astype('float32') / 255.0

    return image

def augment_image(image):
    # Exemple d'augmentation (rotation aléatoire)
    rows, cols, _ = image.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    return cv2.warpAffine(image, M, (cols, rows))

# Exemple d'utilisation
processed_image = preprocess_image(images[0])
augmented_image = augment_image(processed_image)
