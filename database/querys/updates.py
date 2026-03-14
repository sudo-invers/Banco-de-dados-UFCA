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
    
#atualizar dados do acusado - usuario - email, senha, telefone
#atualizar dados do acusador - usuario - email, senha, telefone
#atualizar status do acordo
#atualizar status da audiencia
#atualizar status de mediador e do gestor 
