from datetime import date
from enums.cause_complaint import ComplaintCause

class Complaint:
    """Classe que recebe dados de denuncia"""
    def __init__(self, cause:ComplaintCause, detailing: str, date_conflict: date):
        self.cause = cause
        self.detailing = detailing
        self.date_conflict = date_conflict
        