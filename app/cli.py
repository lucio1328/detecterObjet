import argparse
import cv2
import tensorflow as tf

def detect_from_cli(model, image_path):
    image = cv2.imread(image_path)
    processed_image = preprocess_image(image)
    label, confidence = detect_objects(model, processed_image)
    print(f"Objet détecté : {label} avec une confiance de {confidence:.2f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Détection d'objets via CLI")
    parser.add_argument("image_path", help="Chemin de l'image à traiter")
    args = parser.parse_args()

    model = tf.keras.models.load_model('models/my_model.h5')
    detect_from_cli(model, args.image_path)
