from datetime import date, time
from enums.status_audience import StatusAudience
class Audience:
    """Classe que recebe dados de audiência"""
    def __init__(self, date_audience: date, hour: time, status: StatusAudience):
        self.date_audience = date_audience
        self.hour = hour
        self.status = status