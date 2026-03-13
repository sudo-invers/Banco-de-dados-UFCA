from datetime import date
class User:
    #Classe pai das classes de usuários
    def __init__(self, name: str, document: int, telephone: int, birth: date):
        self.name = name
        self.document = document
        self.telephone = telephone
        self.birth = birth

    @property
    def document(self):
        return self.__document
    @document.setter
    def document(self, valid_document):
        if len(self.document != 11):
            raise ValueError("cpf de comprimento invalido")
        else:
            self.__document = valid_document