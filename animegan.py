import tensorflow as tf
from utils import preprocess_image, postprocess_image, save_frame
from config import Config

# Charger le modèle AnimeGAN
model = tf.saved_model.load(Config.MODEL_PATH)

def generate_frames(image):
    """ Génère des frames stylisées à partir d'une image """
    frames = []

    for i in range(Config.NUM_FRAMES):
        img_input = preprocess_image(image)  # Prétraitement
        output = model(img_input)  # Application du modèle
        frame = postprocess_image(output)  # Post-traitement

        filename = save_frame(frame, i)  # Sauvegarde de la frame
        frames.append(filename)

    return frames  # Retourne la liste des chemins des frames
