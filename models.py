# **************************************************************************** #
#                                                                              #
#      Auteur : fcaval <fcaval@student.42lehavre.fr                            #
#      Projet personnel débuté le 14/02/2026                                   #
#                                                                              #
# **************************************************************************** #

from datetime import datetime

class Candidate:
    
    "represents a candidate in the recruitment process "

    valid_status = ["reçu", "préqualification", "entretien", "refusé", "accepté"]

    def __init__(self, last_name: str, first_name: str, status: str, date: int, 
                 id: int = None):

        """
        Initializes a candidate.
        
        Args:
            last_name: Candidate's last name
            first_name: Candidate's first name
            status: Current status of the candidate
            date: Application date (YYYY-MM-DD)
            id: Unique ID (auto-generated if None)
        """

        self.id = id
        self.last_name = last_name.upper()
        self.first_name = first_name.capitalize()
        self.status = status
        self.date = Candidate.validate_date(date)
        self.status = "reçu"
        self.note = ""

    @staticmethod
    def validate_date(date_str: str) -> str:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")

    def modify_status(self, new_status: str) -> bool:
        if new_status in Candidate.valid_status:
            self.status = new_status
            return True
        else:
            print(f"Invalid status. Valid options are: {Candidate.valid_status}")
            return False

    def add_note(self, note: str):
        try:
            if isinstance(note, str) and not note == "":    
                self.note = note
        except (ValueError, TypeError):
            print("Error: the note must be a non-empty string")

    def transform_to_dict(self) -> dict:
        return {
            "id": self.id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "status": self.status,
            "date": self.date,
            "note": self.note
        }
    
    def __str__(self):
        return f"ID: {self.id} | Name: {self.first_name} {self.last_name} | Status: {self.status} | Date: {self.date} | Note: {self.note}"
    