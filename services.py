# services.py
from models import Estudante, Republica
from persistence import PersistenceManager
from matcher import DataCollector, MatchMaker

class AuthService:
    """
    Serviço responsável por registrar e logar usuários
    (Estudantes ou Repúblicas).
    """
    def __init__(self, usuarios):
        # 'usuarios' é uma lista de objetos Estudante/Republica
        self.usuarios = usuarios

    def registrar(self):
        print("\n=== Registrar novo usuário ===")

        username = input("Digite o nome de usuário: ")
        # Verifica se já existe
        if any(u.username == username for u in self.usuarios):
            print("Usuário já existe! Tente outro nome.")
            return None
        
        password = input("Digite a senha: ")
        print("Você deseja se cadastrar como:")
        print("1 - Estudante")
        print("2 - República")
        opcao = input("Escolha (1/2): ")

        nome = input("Digite seu nome: ")
        telefone = input("Digite seu telefone: ")
        instagram = input("Digite seu Instagram: ")

        if opcao == "1":
            novo = Estudante(username, password, nome, telefone, instagram)
            print("Novo Estudante criado!")
        elif opcao == "2":
            novo = Republica(username, password, nome, telefone, instagram)
            print("Nova República criada!")
        else:
            print("Opção inválida.")
            return None

        self.usuarios.append(novo)
        print(f"Usuário '{username}' cadastrado com sucesso.")
        return novo

    def login(self):
        print("\n=== Login de usuário ===")
        username = input("Digite o nome de usuário: ")
        password = input("Digite a senha: ")

        for u in self.usuarios:
            if u.username == username and u.checar_senha(password):
                print(f"Bem-vindo, {username}!")
                return u
        print("Usuário ou senha incorretos!")
        return None


class Sistema:
    """
    Classe principal que orquestra o fluxo do programa:
    - Carrega usuários do JSON
    - Exibe o menu principal (Registrar, Login, Sair)
    - Coordena as ações
    """
    def __init__(self):
        self.pm = PersistenceManager("user_data.json")
        self.usuarios = self.pm.load_users()  # Lista de Estudante/Republica
        self.auth_service = AuthService(self.usuarios)

    def menu_principal(self):
        while True:
            print("\n=== Sistema de Login ===")
            print("1 - Registrar")
            print("2 - Login")
            print("3 - Sair")

            opc = input("Escolha uma opção: ")

            if opc == "1":
                user_created = self.auth_service.registrar()
                self.pm.save_users(self.usuarios)  # salva imediatamente
                
                
            elif opc == "2":
                user_logged = self.auth_service.login()
                if user_logged:
                    self.menu_pos_login(user_logged)
            elif opc == "3":
                # Salvar antes de sair
                self.pm.save_users(self.usuarios)
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_pos_login(self, usuario):
        """
        Menus específicos para Estudante ou República.
        """
        if isinstance(usuario, Estudante):
            self.menu_estudante(usuario)
        elif isinstance(usuario, Republica):
            self.menu_republica(usuario)

    def menu_estudante(self, estudante):
     while True:
        print(f"\n=== Menu Estudante ({estudante.username}) ===")
        print("1 - Preencher/Atualizar Formulário (30 perguntas)")
        print("2 - Determinar Personalidade e Ver Resultado")
        print("3 - Ver Perfil Final (se já calculado)")
        print("4 - Sair para o menu principal")
        print("5 - Ver Repúblicas Compatíveis")  

        opc = input("Escolha uma opção: ")
        if opc == "1":
            estudante.preencher_formulario()
            self.pm.save_users(self.usuarios)
        elif opc == "2":
            estudante.determinar_personalidade()
            self.pm.save_users(self.usuarios)
        elif opc == "3":
            if estudante.perfil_final:
                print(f"Perfil Final: {estudante.perfil_final}")
            else:
                print("Ainda não foi determinado um perfil final.")
        elif opc == "4":
            break
        elif opc == "5":
            self.ver_republicas_compativeis(estudante)
        else:
            print("Opção inválida.")


    def menu_republica(self, rep):
        while True:
            print(f"\n=== Menu República ({rep.username}) ===")
            print("1 - Escolher/Atualizar Tipo de República")
            print("2 - Ver Tipo escolhido")
            print("3 - Sair para o menu principal")

            opc = input("Escolha uma opção: ")
            if opc == "1":
                rep.preencher_formulario()
                self.pm.save_users(self.usuarios)
            elif opc == "2":
                if rep.tipo_escolhido:
                    print(f"Tipo escolhido: {rep.tipo_escolhido}")
                    print(f"Descrição: {rep.descricao_tipo}")
                else:
                    print("Ainda não escolheu o tipo de república.")
            elif opc == "3":
                break
            else:
                print("Opção inválida.")
    
    def ver_republicas_compativeis(self, estudante):
         if not estudante.perfil_final:
            print("\nVocê ainda não tem um perfil final. Selecione a opção 2 para determinar sua personalidade.")
            return
        
         # 1. Coletar dados do JSON
         collector = DataCollector(self.pm.file_path)  
         collector.collect_data()

         # 2. Criar o MatchMaker
         mm = MatchMaker(collector)

         # 3. Exibir repúblicas compatíveis
         mm.exibir_republicas_compat(estudante.perfil_final)
