import os
import json
import cv2
import numpy as np

def load_data(data_dir, annotation_file):
    # Charger les annotations
    with open(annotation_file, 'r') as file:
        annotations = json.load(file)

    images = []
    labels = []

    for annotation in annotations:
        img_path = os.path.join(data_dir, annotation['image'])
        image = cv2.imread(img_path)
        images.append(image)

        label = annotation['labels']
        labels.append(label)

    return np.array(images), np.array(labels)

images, labels = load_data('data/raw/', 'data/annotations.json')
