from grupo08.domain.models.user import User
class Mediator(User):
    """Classe responsável por receber dados de mediador"""
    def __init__(self, name, document, telephone, birth, cod_mediador):
        super().__init__(name, document, telephone, birth)