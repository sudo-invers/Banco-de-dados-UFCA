from datetime import date
class Complaint:
    """Classe que recebe dados de denuncia"""
    def __init__(self, cause, detailing, date_conflict: date):
        self.cause = cause
        self.detailing = detailing
        self.date_conflict = date_conflict
        