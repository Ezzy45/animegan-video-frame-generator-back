import os

class Config:
    """ Configuration globale du projet """
    MODEL_PATH = os.path.join(os.getcwd(), "models/animegan_model")  # Chemin du modèle
    IMAGE_SIZE = (256, 256)  # Taille de l'image pour AnimeGAN
    NUM_FRAMES = 10  # Nombre de frames à générer
    OUTPUT_FOLDER = os.path.join(os.getcwd(), "frames")  # Dossier de sortie
    
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)  # Créer le dossier si inexistant
