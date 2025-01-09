from perfis_usuarios import (
    LiderSociavel, CriativoIndependente, FlexivelHarmonizador, 
    OrganizadoPacifista, ExtrovertidoDescontraido, MediadorEmpatico, 
    OrganizadoExtrovertido, IntrovertidoFlexivel, SocialResolutivo
)
from formulario import determinar_personalidade, perguntas_formulario
from usuarios import Usuario

usuarios = []  # Simulação de banco de dados para usuários
republicas = []  # Simulação de banco de dados para repúblicas

def autenticar_usuario(login, senha):
    """
    Autentica um usuário com base no login e senha fornecidos.
    """
    for usuario in usuarios:
        if usuario.login == login and usuario.senha == senha:
            print(f"\nBem-vindo(a), {usuario.nome}!")
            print(usuario.visualizar_personalidade())
            buscar_republicas_recomendadas(usuario)
            return usuario
    print("\nUsuário ou senha inválidos. Tente novamente.")
    return None

def cadastrar_usuario():
    """
    Cadastra um novo usuário no sistema e permite responder ao formulário.
    """
    print("\n--- Cadastro de Usuário ---")
    login = input("Login: ")
    senha = input("Senha: ")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    instagram = input("Instagram: ")

    respostas = perguntas_formulario()
    categorias = determinar_personalidade(respostas)
    perfil = determinar_perfil(categorias)

    novo_usuario = perfil(
        login=login, senha=senha, nome=nome, 
        telefone=telefone, instagram=instagram, 
        respostas_formulario=respostas
    )

    usuarios.append(novo_usuario)
    print(f"\nUsuário cadastrado com sucesso no perfil: {perfil.descricao}\n")

def buscar_republicas_recomendadas(usuario):
    """
    Busca as repúblicas mais adequadas ao perfil do usuário.
    """
    if not republicas:
        print("\nNenhuma república cadastrada no momento.")
        return

    print("\n--- República Recomendadas ---")
    recomendacoes = []

    for republica in republicas:
        pontos = 0
        if usuario.respostas_formulario.get("Extroversão e Socialização", 0) >= 18 and republica.tipo == "Líder Social":
            pontos += 3
        if usuario.respostas_formulario.get("Organização e Responsabilidade", 0) >= 18 and republica.tipo == "Equilíbrio e Paz":
            pontos += 3
        if usuario.respostas_formulario.get("Tolerância e Flexibilidade", 0) >= 18 and republica.tipo == "Harmonia Flex":
            pontos += 2
        if usuario.respostas_formulario.get("Hábitos Diários e Estilo de Vida", 0) <= 8 and republica.tipo == "Relax Noturna":
            pontos += 2
        if usuario.respostas_formulario.get("Preferências Pessoais", 0) >= 18 and republica.tipo == "Criativa e Livre":
            pontos += 2

        recomendacoes.append((republica, pontos))

    recomendacoes.sort(key=lambda x: x[1], reverse=True)

    for republica, pontos in recomendacoes:
        print(f"{republica.nome} - Pontuação: {pontos}")
        print(f"Contato: {republica.telefone} | Instagram: {republica.instagram}\n")

def menu_principal():
    """
    Menu principal do sistema.
    """
    while True:
        print("\n--- Sistema de Usuários ---")
        print("1. Cadastrar novo usuário")
        print("2. Fazer login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            login = input("Login: ")
            senha = input("Senha: ")
            autenticar_usuario(login, senha)
        elif opcao == "3":
            print("\nObrigado por usar o sistema! Até logo.")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
