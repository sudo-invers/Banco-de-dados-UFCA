from database.querys.sql_updates import SQLUpdate

class CLIUpdateCommand:

    def __init__(self):
        self.repo = SQLUpdate()

    def cli_update_compaint_on_audience(self):
        #atualiza o id da audiência na tabela da denúncia
        complaint_id = int(input("Id da denúncia: "))
        audience_id = int(input("Id da audiência: "))

        try:
            up = self.repo.update_complaint_on_audience(complaint_id=complaint_id, audience_id=audience_id)
        except Exception as error:
            return "Erro ao atualizar id"
        return "id da audiência atualizado com sucesso"

    def cli_update_person(self):
        #atualiza dados de qualquer pessoa do sistema
        name = str(input("Nome novo: "))
        phone = str(input("Telefone novo: "))
        pessoa_id = int(input("Digite seu identificador no sistema para confirmar as alterações: \n"))
        try:
             up = self.repo.update_person(name=name, phone=phone, pessoa_id=pessoa_id)
        except Exception as error:
            return "Erro ao atualizar dados"
        return "Dados atualizados."

    def cli_update_agreement(self):
        #atualiza dados do acordo como sua data e resolução
        status_acordo = str(input("Novo status: "))
        data_acordo = input("Data do acordo: ")
        acordo_id = int(input("Digite o id do acordo para confirmar as alterações: "))
        try:
            up = self.repo.update_agreement(status_acordo=status_acordo, data_acordo=data_acordo, acordo_id=acordo_id)
        except Exception as error:
            return "Erro ao atualizar informações do acordo"
        
        return "Dados atualizados com sucesso"
