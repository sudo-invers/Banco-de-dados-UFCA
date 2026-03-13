from datetime import date, time
class Audience:
    """Classe que recebe dados de audiência"""
    def __init__(self, date_audience: date, hour: time, status):
        self.date_audience = date_audience
        self.hour = hour
        self.status = status