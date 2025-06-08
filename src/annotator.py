import cv2
import json

annotations = []

def annotate_image(image_path):
    img = cv2.imread(image_path)
    # Supposons que tu cliques pour définir les coins des boîtes de détection
    # (L'implémentation de l'annotation graphique est plus complexe, ici c'est un exemple simple)
    # Tu peux utiliser une interface graphique pour collecter les coordonnées
    print("Cliquez pour définir une boîte de détection")
    # Annotation avec des boîtes manuelles
    # Exemple : Enregistre l'annotation dans un fichier JSON
    annotations.append({'image': image_path, 'labels': [{'bbox': [50, 50, 100, 100], 'label': 'object'}]})

    # Sauvegarde les annotations
    with open('annotations.json', 'w') as f:
        json.dump(annotations, f)

# Exemple d'utilisation
annotate_image('data/raw/sample_image.jpg')
