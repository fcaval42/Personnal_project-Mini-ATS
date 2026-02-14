# **************************************************************************** #
#                                                                              #
#      Auteur : fcaval <fcaval@student.42lehavre.fr                            #
#      Projet personnel débuté le 14/02/2026                                   #
#                                                                              #
# **************************************************************************** #

from models import Candidat

def ajouter_candidat():
    try:
        print()
        nom_saisi = input("Nom: ")
        prénom_saisi = input("Prénom: ")
        poste_saisi = input("Poste visé: ")
        date_saisi = input("Date (YYYY-MM-DD): ")

        nouveau = Candidat(nom_saisi, prénom_saisi, poste_saisi, date_saisi)

        print(f"\n === Candidat ajouté avec succès ! ===")

    except ValueError as e:
        print(f"❌ {e}")