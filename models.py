# **************************************************************************** #
#                                                                              #
#      Auteur : fcaval <fcaval@student.42lehavre.fr                            #
#      Projet personnel débuté le 14/02/2026                                   #
#                                                                              #
# **************************************************************************** #

class Candidat:
    def __init__(self, nom: str, prénom: str, poste: str, date: int):

        self.nom = nom.upper()
        self.prénom = prénom.capitalize()
        self.poste = poste
        self.date = date

    def get_info(self):
        return f"| {self.nom} | {self.prénom} | {self.poste} | {self.date}"
