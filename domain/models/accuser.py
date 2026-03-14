from grupo08.domain.models.user import User
class Accuser(User):
    """Classe que recebe dados de pessoa que fará denúncia no sitema"""
    def __init__(self, name, document, telephone, birth):
        super().__init__(name, document, telephone, birth)