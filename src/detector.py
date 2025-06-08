import cv2
import tensorflow as tf

def detect_objects(model, image):
    # Prédire les objets dans l'image
    predictions = model.predict(np.expand_dims(image, axis=0))

    # Exemple simple : on suppose que l'objet le plus probable est celui de l'index 0
    label = np.argmax(predictions)
    confidence = np.max(predictions)

    # Afficher le résultat
    print(f"Objet détecté : {label} avec confiance {confidence:.2f}")
    return label, confidence

# Exemple d'utilisation
image = cv2.imread('data/raw/sample_image.jpg')
processed_image = preprocess_image(image)
detect_objects(model, processed_image)
