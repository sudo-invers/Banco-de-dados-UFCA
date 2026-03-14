class CityHall():
    def __init__(self, cnpj: int, manager: str, city: str):
        self.cnpj = cnpj
        self.manager = manager
        self.city = city
        self.tam_cnpj = 12
    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj_valid):
        if len(self.cnpj != self.tam_cnpj):
            raise ValueError("Comprimento de CNPJ inválido.")
        else:
            self.__cnpj = cnpj_valid
