# **************************************************************************** #
#                                                                              #
#      Auteur : fcaval <fcaval@student.42lehavre.fr                            #
#      Projet personnel débuté le 14/02/2026                                   #
#                                                                              #
# **************************************************************************** #


class Candidat:
    def __init__(self, nom: str, prenom: str, poste: str, date: int):

        self.nom = nom.upper()
        self.prenom = prenom.capitalize()
        self.poste = poste
        self.date = date

    def transformer_en_dico(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "poste": self.poste,
            "date": self.date
        }

    def get_info(self):
        return f"| {self.nom} | {self.prenom} | {self.poste} | {self.date}"
