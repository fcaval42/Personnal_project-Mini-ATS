# **************************************************************************** #
#                                                                              #
#      Auteur : fcaval <fcaval@student.42lehavre.fr                            #
#      Projet personnel débuté le 14/02/2026                                   #
#                                                                              #
# **************************************************************************** #

from models import Candidat
import json
import os

def ajouter_candidat():
    try:
        print()
        nom_saisi = input("Nom: ")
        prénom_saisi = input("Prénom: ")
        poste_saisi = input("Poste visé: ")
        date_saisi = input("Date (YYYY-MM-DD): ")

        nouveau = Candidat(nom_saisi, prénom_saisi, poste_saisi, date_saisi)

        return nouveau

    except ValueError as e:
        print(f"Erreur: {e}")


def modifier_candidat():
    if not os.path.exists("data.json"):
        print("\n Le fichier candidat n'a pas été trouvé")
        return 
    
    try:
        with open("data.json", 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Erreur : fichier JSON corrompu.")
        return
    
    if not data:
        print("Aucun candidat enregistré")
        return
    
    recherche_nom = input("Nom du candidat: ").upper().strip()
    recherche_prénom = input("Prénom du candidat: ").capitalize().strip()
    modification = input("Que souhaitez-vous modifier ?: ")
    candidat_trouvé = False

    for candidat in data:
        if candidat["nom"] == recherche_nom and candidat["prenom"] == recherche_prénom:
            candidat_trouvé = True
            if candidat["nom"] == modification:
                nouveau_nom = input("Rentrez le nouveau nom: ").upper
                candidat["nom"] = nouveau_nom
                break
            elif candidat["prenom"] == modification:
                nouveau_prénom = input("Rentrez le nouveau prénom: ").capitalize
                candidat["prenom"] = nouveau_prénom
                break

    if not candidat_trouvé:
        print("Le candidat n'a pas été trouvé")
        return

    try:
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Statut mis à jour et sauvegardé.")
    except Exception as e:
        print("Erreur lors de la sauvegarde :", e)