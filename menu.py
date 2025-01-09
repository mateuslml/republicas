from cadastro import cadastrar_estudante, cadastrar_republica
from autenticacao import autenticar_usuario, autenticar_republica

def menu_principal():
    while True:
        print("\n--- Bem-vindo ao JUNTAI ---")
        print("1. Cadastrar como Estudante")
        print("2. Cadastrar como República")
        print("3. Login como Estudante")
        print("4. Login como República")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_estudante()
        elif opcao == "2":
            cadastrar_republica()
        elif opcao == "3":
            login = input("Login do usuário: ")
            senha = input("Senha: ")
            autenticar_usuario(login, senha)
        elif opcao == "4":
            login = input("Login da República: ")
            senha = input("Senha: ")
            autenticar_republica(login, senha)
        elif opcao == "5":
            print("\nObrigado por usar o JUNTAI! Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
