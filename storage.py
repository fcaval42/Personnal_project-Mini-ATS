# **************************************************************************** #
#                                                                              #
#      Auteur : fcaval <fcaval@student.42lehavre.fr                            #
#      Projet personnel débuté le 14/02/2026                                   #
#                                                                              #
# **************************************************************************** #

import json
import os
import models

def sauvegarder_candidat(nouveau_candidat, filename="data.json"):
    liste_candidats = []

    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            try:
                liste_candidats = json.load(f)
            except json.JSONDecodeError:
                # Si le fichier est vide ou corrompu, on repart d'une liste vide
                liste_candidats = []

    liste_candidats.append(nouveau_candidat.transformer_en_dico())

    # On réécrit le fichier avec la liste complète mise à jour
    try:
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(liste_candidats, f, indent=4, ensure_ascii=False)

        print(f"\n === Candidat ajouté avec succès ! ===")

    except Exception as e:
        print(f"Echec de l'enregistrement du candidat': {e}")
