from database.connect import ConnectDatabase
connect = ConnectDatabase()


#Atualização
#atualizar denuncia com dados da audiencia
class UpdateComplaintOnAudience():
    def __init__(self, complaint_id, audience_id):
        self.sql_audience_id_into_complaint = """UPDATE DENUNCIA 
        SET audiencia_id = %s 
        WHERE denuncia_id = %s"""
        self.complaint_id = complaint_id
        self.audience_id = audience_id
    
    def updt(self):
        connect.cur.execute(self.sql_audience_id_into_complaint, 
                            (self.audience_id, self.complaint_id))
        return True


#atualizar dados de qualquer pessoa - nome, telefone
class UpdatePerson():
    def __init__(self, name, phone, pessoa_id):
        self.sql_data_into_person = """UPDATE PESSOA
        SET nome = %s, telefone = %s
        WHERE pessoa_id = %s"""
        self.name = name
        self.phone = phone
        self.pessoa_id = pessoa_id

    def update(self):
        connect.cur.execute(self.sql_data_into_person,
                            (self.name, self.phone, self.pessoa_id))
        return True


#atualizar dados do endereço de qualquer pessoa
class UpdateAddress():
    def __init__(self, rua, bairro, cidade, numero, endereco_id):
        self.sql_data_into_address = """UPDATE ENDERECO
        SET rua = %s, bairro = %s, cidade = %s, numero = %s
        WHERE endereco_id = %s"""
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.numero = numero
        self.endereco_id = endereco_id

    def update(self):
        connect.cur.execute(self.sql_data_into_address,
                            (self.rua, self.bairro, self.cidade, self.numero, self.endereco_id))
        return True


#atualizar status do acordo
class UpdateAgreement():
    def __init__(self, status_acordo, data_acordo, acordo_id):
        self.sql_data_into_agreement = """UPDATE ACORDO
        SET status_acordo = %s, data_acordo = %s
        WHERE acordo_id = %s"""
        self.status_acordo = status_acordo
        self.data_acordo = data_acordo
        self.acordo_id = acordo_id

    def update(self):
        connect.cur.execute(self.sql_data_into_agreement,
                            (self.status_acordo, self.data_acordo, self.acordo_id))
        return True


#atualizar status da audiencia
class UpdateAudience():
    def __init__(self, status_audiencia, data_audiencia, audiencia_id):
        self.sql_data_into_audience = """UPDATE AUDIENCIA
        SET status_audiencia = %s, data_audiencia = %s
        WHERE audiencia_id = %s"""
        self.status_audiencia = status_audiencia
        self.data_audiencia = data_audiencia
        self.audiencia_id = audiencia_id

    def update(self):
        connect.cur.execute(self.sql_data_into_audience,
                            (self.status_audiencia, self.data_audiencia, self.audiencia_id))
        return True


#atualizar status do mediador 
class UpdateMediator():
    def __init__(self, status_mediador, mediador_id):
        self.sql_status_into_mediator = """UPDATE MEDIADOR
        SET status_mediador = %s
        WHERE mediador_id = %s"""
        self.status_mediador = status_mediador
        self.mediador_id = mediador_id

    def update(self):
        connect.cur.execute(self.sql_status_into_mediator,
                            (self.status_mediador, self.mediador_id))
        return True


#atualizar status do gestor 
class UpdateManager():
    def __init__(self, status_gestor, gestor_id):
        self.sql_status_into_manager = """UPDATE GESTOR
        SET status_gestor = %s
        WHERE gestor_id = %s"""
        self.status_gestor = status_gestor
        self.gestor_id = gestor_id

    def update(self):
        connect.cur.execute(self.sql_status_into_manager,
                            (self.status_gestor, self.gestor_id))
        return True