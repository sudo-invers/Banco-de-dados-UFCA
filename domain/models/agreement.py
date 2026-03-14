from datetime import date
from enums.status_agreement import StatusAgreement
class Agreement:
    """Classe que recebe dados de acordos"""
    def __init__(self, status:StatusAgreement.AGUARDANDO_AUDIENCIA, date_agreement: date):
        self.status = status
        self.date_agreement = date_agreement