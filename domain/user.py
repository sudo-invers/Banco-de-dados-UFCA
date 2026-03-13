class User:
    #Classe pai das classes de usuários
    def __init__(self, name, document, telephone, birth):
        self.name = name
        self.document = document
        self.telephone = telephone
        self.birth = birth