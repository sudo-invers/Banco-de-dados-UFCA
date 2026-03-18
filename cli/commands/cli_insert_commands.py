import sys
from datetime import datetime, date
from database.querys.sql_inserts import SQLInsertion
from database.querys.sql_updates import SQLUpdate
from cli.curr_user import user, set_user

class CLIInsertCommand:
    """
    A classe ´CommandInsertCLI´ mostra os atributos que o usuário
    deve digitar na CLI para cadastrar os dados desejados,
    por meio de chamadas às funções de database.
    """
    def __init__(self):
        self.repo = SQLInsertion()
        self.update_repo = SQLUpdate()

    def _input_date(self, mensagem: str, obrigatorio: bool = True):
        data_input = input(mensagem)
        if not data_input and not obrigatorio:
            return None
        return datetime.strptime(data_input, "%Y-%m-%d").date()

    def _create_address(self) -> int | None:
        print("\n=== Endereço ===")
        cidade = input("Cidade: ")
        bairro = input("Bairro: ")
        rua = input("Rua: ")
        numero = input("Número: ")

        endereco_id = self.repo.insert_address(
            cidade=cidade,
            bairro=bairro,
            rua=rua,
            numero=numero,
        )

        if not endereco_id:
            print("Erro ao cadastrar endereço", file=sys.stderr)

        return endereco_id

    def _create_person(self, obrigatorio=True, endereco_id=None) -> int | None:
        nome = input("Nome: ")

        data_nascimento = self._input_date(
            "Data de nascimento (YYYY-MM-DD): ",
            obrigatorio=obrigatorio
        )

        telefone = input("Telefone: ") or None
        documento = input("CPF/CNPJ: ") or None

        pessoa_id = self.repo.insert_people(
            nome=nome,
            data_nascimento=data_nascimento,
            telefone=telefone,
            n_inscricao_tributaria=documento,
            endereco_id=endereco_id
        )

        if not pessoa_id:
            print("Erro ao cadastrar pessoa", file=sys.stderr)

        return pessoa_id

    def insert_user(self, tipo_usuario: str):
        try:
            print("\n=== Cadastro de Usuários ===")

            endereco_id: int = self._create_address()
            pessoa_id: int = self._create_person(endereco_id=endereco_id)

            email: str = input("Digite seu email: ")
            senha: str = input("Crie uma senha de acesso: ")

            usuario_id: int = self.repo.insert_user(
                email=email,
                senha=senha,
                tipo_usuario=tipo_usuario
            )

            acusador_id: int = self.repo.insert_accuser(
                pessoa_id=pessoa_id,
                usuario_id=usuario_id
            )

            set_user(
                {
                    "usuario_id": usuario_id,
                    "email": email,
                    "pessoa_id": pessoa_id,
                    "tipo_usuario": tipo_usuario,
                    "acusador_id": acusador_id
                }
            )




        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)


    def insert_complaint(self, acusador_id: int):
        if not acusador_id:
            print("Err: acusador_id não informado.\n(possivelmente por que você não está logado)", file=sys.stderr)
            return

        try:
            print("\n=== Cadastro de Denúncias ===")

            use_address = input("Deseja informar endereço do acusado? [s/n]: ")
            endereco_id = None

            if use_address and use_address.lower().startswith('s'):
                endereco_id = self._create_address()
                if not endereco_id:
                    return

            pessoa_id = self._create_person(obrigatorio=False, endereco_id=endereco_id)
            if not pessoa_id:
                return

            acusado_id = self.repo.insert_accused(pessoa_id)
            if not acusado_id:
                print("Erro ao cadastrar acusado", file=sys.stderr)
                return

            causa = input("Causa da denúncia: ")
            detalhamento = input("Detalhamento: ") or None

            data = self._input_date("Data (YYYY-MM-DD): ")

            result = self.repo.insert_complaint(
                audiencia_id=None,
                acusador_id=acusador_id,
                acusado_id=acusado_id,
                causa_denuncia=causa,
                detalhamento=detalhamento,
                data=data
            )

            if result:
                print(f"Denúncia cadastrada com ID {result}")
            else:
                print("Erro ao cadastrar denúncia", file=sys.stderr)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)


    def insert_mediator(self, prefeitura_id: int, usuario_id: int):
        try:
            print("\n=== Cadastro de Mediador ===")

            endereco_id = self._create_address()
            if not endereco_id:
                return

            pessoa_id = self._create_person(endereco_id=endereco_id)
            if not pessoa_id:
                return

            mediador_id = self.repo.insert_mediator(
                pessoa_id=pessoa_id,
                usuario_id=None,
                prefeitura_id=prefeitura_id,
                status_mediador="ATIVO"
            )

            if mediador_id:
                print(f"Mediador cadastrado com ID {mediador_id}")
            else:
                print("Erro ao cadastrar mediador", file=sys.stderr)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def insert_audience(self):
        try:
            print("\n=== Cadastro de Audiência ===")

            denuncia_id = int(input("ID da denúncia: "))
            mediador_id = int(input("ID do mediador: "))

            data = self._input_date("Data da audiência (YYYY-MM-DD): ")

            endereco_id = self._create_address()
            if not endereco_id:
                return

            audiencia_id = self.repo.insert_audience(
                mediador_id=mediador_id,
                endereco_id=endereco_id,
                status_audiencia='AGENDADA',
                data=data
            )

            if not audiencia_id:
                print("Erro ao cadastrar audiência", file=sys.stderr)
                return

            updated = self.update_repo.update_complaint_on_audience(
                complaint_id=denuncia_id,
                audience_id=audiencia_id
            )

            if not updated:
                print("Erro ao vincular audiência com denúncia", file=sys.stderr)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def insert_cityhall(self):
        try:
            print("\n=== Cadastro de Prefeitura ===")

            endereco_id = self._create_address()
            if not endereco_id:
                return

            cnpj = input("CNPJ: ")

            prefeitura_id = self.repo.insert_cityhall(
                endereco_id=endereco_id,
                cnpj=cnpj
            )

            if prefeitura_id:
                print(f"Prefeitura cadastrada com ID {prefeitura_id}")
            else:
                print("Erro ao cadastrar prefeitura", file=sys.stderr)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def insert_agreement(self):
        try:
            print("\n=== Cadastro de Acordo ===")

            audiencia_id = int(input("ID da audiência: "))

            status = input("Status do acordo: ")

            data_acordo = self._input_date("Data do acordo (YYYY-MM-DD): ")

            acordo_id = self.repo.insert_agreement(
                audiencia_id=audiencia_id,
                status_acordo=status,
                data_acordo=data_acordo
            )

            if acordo_id:
                print(f"Acordo cadastrado com ID {acordo_id}")
            else:
                print("Erro ao cadastrar acordo", file=sys.stderr)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)