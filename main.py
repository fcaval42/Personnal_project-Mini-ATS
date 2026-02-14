# **************************************************************************** #
#                                                                              #
#      Auteur : fcaval <fcaval@student.42lehavre.fr                            #
#      Projet personnel débuté le 14/02/2026                                   #
#                                                                              #
# **************************************************************************** #

import models
import manager

def main():
    print("\n ======== MINI ATS - 42 EDITION =========\n")

    print("1. Ajouter un candidat")
    print("2. Modifier un statut")
    print("3. Ajouter/modifier une note")
    print("4. Supprimer un candidat")
    print("5. Afficher tous les candidats")
    print("6. Filtrer par statut")
    print("7. Quitter")

    choix = input("\n Choix: ")

    if choix == "1":
        print("\n choix: 1")
        manager.ajouter_candidat()

    elif choix == "2":
        print("\n choix 2")

    elif choix == "3":
        print("\n choix 3")

    elif choix == "4":
        print("\n choix 4")

    elif choix == "5":
        print("\n choix 5")

    elif choix == "6":
        print("\n choix 6")

    elif choix == "7":
        print("\n Ok bye !")
    
    else:
        print()
        print("ATTENTION : Votre choix doit être un chiffre compris entre 1 et 7 \n")
        main()


if __name__ == "__main__":
    main()