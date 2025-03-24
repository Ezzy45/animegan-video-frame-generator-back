from flask import Flask, request, jsonify, render_template
from animegan import generate_frames
from PIL import Image
import os
from config import Config

app = Flask(__name__)

@app.route("/")
def home():
    """ Page principale avec le formulaire de téléversement d'image """
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_image():
    """ Endpoint pour téléverser une image et générer des frames """
    if "file" not in request.files:
        return jsonify({"error": "Aucun fichier trouvé"}), 400
    
    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Aucun fichier sélectionné"}), 400

    image = Image.open(file)  # Ouvrir l'image
    frames = generate_frames(image)  # Générer les frames stylisées

    return jsonify({"frames": frames})  # Retourner les chemins des frames

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Utilise le port spécifié par Render, ou 5000 par défaut
    app.run(host='0.0.0.0', port=port)
