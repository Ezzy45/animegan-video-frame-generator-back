import os
import numpy as np
from PIL import Image
from config import Config

def preprocess_image(image):
    """ Prépare l'image pour AnimeGAN """
    img = image.convert("RGB").resize(Config.IMAGE_SIZE)
    img = np.array(img) / 127.5 - 1  # Normalisation [-1,1]
    img = np.expand_dims(img, axis=0).astype(np.float32)
    return img

def postprocess_image(output):
    """ Convertit la sortie d'AnimeGAN en image PIL """
    img = (output[0].numpy() + 1) * 127.5
    img = np.clip(img, 0, 255).astype(np.uint8)
    return Image.fromarray(img)

def save_frame(frame, index):
    """ Sauvegarde une frame stylisée """
    filename = os.path.join(Config.OUTPUT_FOLDER, f"frame_{index}.png")
    frame.save(filename, format="PNG")
    return filename
