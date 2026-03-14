from grupo08.domain.models.user import User

class Acused(User):
    """Classe responsável por receber dados de pessoa acusada"""
    def __init__(self, name, document, telephone, birth):
        super().__init__(name, document, telephone, birth)

