from database.connect import ConnectDatabase
connect = ConnectDatabase()
#inserçoes
class SaveBD:
    #classe de salvar no banco - faz commit no banco e fecha-o
    def __init__(self, query, data):
        self.query = query
        self.data = data

    def save(self):
        connect.cur.execute(self.query, self.data)
        connect.connect.commit()
        connect.close()
        return "Dados cadastrados com sucesso!"
   
#inserção de endereço
class InsertAdress:
    def __init__(self, rua, bairro, cidade, numero):
        self.sql_adress = """INSERT INTO ENDERECO(rua, bairro, cidade, numero) VALUES (%s, %s, %s, %s);"""
        self.adress = (rua, bairro, cidade, numero)
        
    def insert(self):
        dados = SaveBD(self.sql_adress, self.adress)
        return dados.save()
    
#inserção de pessoa 
class InsertPeople:    
    def __init__(self, id_endereco, nome, telefone, documento, nascimento):
        self.sql_insert = """INSERT INTO PESSOA(id_endereco, nome, telefone, n_inscricao_tributaria, data_nascimento) VALUES
        (%s, %s, %s, %s, %s)"""
        self.people = (id_endereco, nome, telefone, documento, nascimento)
    def insert(self):
        dados = SaveBD(self.sql_insert, self.people)
        return dados.save()
    
#cadastro de usuario 
class InsertUser:
    def __init__(self, email, senha, perfil):
        self.sql_insert = """INSERT INTO USUARIO(email, senha, tipo_usuario) VALUES(%s, %s, %s)"""
        self.user = (email, senha, perfil)

    def insert(self):
        dados = SaveBD(self.sql_insert, self.user)
        return dados.save()
        
#Cadastrar acusador
class InsertAccuser:
    def __init__(self, pessoa_id, usuario_id):
        self.sql_insert = """INSERT INTO ACUSADOR(pessoa_id, usuario_id) VALUES(%s, %s)"""
        self.accuser = (pessoa_id, usuario_id)

    def insert(self):
        dados = SaveBD(self.sql_insert, self.accuser)
        return dados.save()
#Cadastrar acusado
class InsertAccused:
    def __init__(self, pessoa_id):
        self.sql_insert = """INSERT INTO ACUSADO(pessoa_id,) VALUES(%s)"""
        self.accused = (pessoa_id)

    def insert(self):
        dados = SaveBD(self.sql_insert, self.accused)
        return dados.save()

#Cadastrar mediador
class InsertMediator:
    def __init__(self, pessoa_id, usuario_id, prefeitura_id, status):
        self.sql_insert = """INSERT INTO 
        MEDIADOR(pessoa_id, usuario_id, prefeitura_id, status_mediador)
        VALUES(%s, %s, %s, %s)"""
        self.mediator = (pessoa_id, usuario_id, prefeitura_id, status)

    def insert(self):
        dados = SaveBD(self.sql_insert, self.mediator)
        return dados.save()
    
#Cadastrar gestor
class InsertGestor:
    def __init__(self, pessoa_id, usuario_id, prefeitura_id, status):
        self.sql_insert = """INSERT INTO 
        GESTOR( prefeitura_id, usuario_id, pessoa_id, status_gestor)
        VALUES(%s, %s, %s, %s)"""
        self.gestor = (prefeitura_id, usuario_id, pessoa_id, status)

    def insert(self):
        dados = SaveBD(self.sql_insert, self.gestor)
        return dados.save()
    
#Cadastrar denúncia
class InsertComplaint:
    def __init__(self, audiencia_id, acusador_id, acusado_id, causa_denuncia, detalhamento, data):
        self.sql_insert = """INSERT INTO 
        DENUNCIA(audiencia_id, acusador_id, acusado_id, causa_denuncia, detalhamento, data_denuncia)
        VALUES(%s, %s, %s, %s, %s, %s)"""
        self.complaint = (audiencia_id, acusador_id, acusado_id, causa_denuncia, detalhamento, data)

    def insert(self):
        dados = SaveBD(self.sql_insert, self.complaint)
        return dados.save()
    
#Cadastrar audiencia
class InsertAudience:
    def __init__(self, id_mediador, id_endereco, status_audiencia, data):
        self.sql_insert = """INSERT INTO 
        AUDIENCIA(mediador_id, endereco_id, status_audiencia, data_audiencia)
        VALUES(%s, %s, %s, %s)"""
        self.audience = (id_mediador, id_endereco, status_audiencia, data)

    def insert(self):
        dados = SaveBD(self.sql_insert, self.audience)
        return dados.save()
    
#Cadastrar acordo
class InsertAgreement:
    def __init__(self, audiencia_id, status_acordo, data_acordo):
        self.sql_insert = """INSERT INTO 
        ACORDO(audiencia_id, status_acordo, data_acordo)
        VALUES(%s, %s, %s)"""
        self.agreement = (audiencia_id, status_acordo, data_acordo)

    def insert(self):
        dados = SaveBD(self.sql_insert, self.agreement)
        return dados.save()
    