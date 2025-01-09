import json
from usuarios import Usuario
from republicas import Republica
from formulario import perguntas_formulario, selecionar_tipo_republica

USUARIOS_FILE = "usuarios.json"
REPUBLICAS_FILE = "republicas.json"

# Funções auxiliares para salvar e carregar dados
def salvar_dados(lista, arquivo):
    with open(arquivo, "w") as f:
        json.dump([item.to_dict() for item in lista], f, indent=4)

def carregar_dados(arquivo, classe):
    try:
        with open(arquivo, "r") as f:
            return [classe.from_dict(item) for item in json.load(f)]
    except FileNotFoundError:
        return []

usuarios = carregar_dados(USUARIOS_FILE, Usuario)
republicas = carregar_dados(REPUBLICAS_FILE, Republica)

def cadastrar_estudante():
    print("\n--- Cadastro de Estudante ---")
    login = input("Login do usuário: ")
    senha = input("Senha: ")
    nome = input("Nome do usuário: ")
    telefone = input("Telefone de contato: ")
    instagram = input("@Instagram: ")

    print("\nAgora, preencha o formulário para mapear seu perfil.")
    respostas_formulario = perguntas_formulario()

    usuario = Usuario(login, senha, nome, telefone, instagram, respostas_formulario)
    usuarios.append(usuario)
    salvar_dados(usuarios, USUARIOS_FILE)
    print("\nEstudante cadastrado com sucesso!")

def cadastrar_republica():
    print("\n--- Cadastro de República ---")
    nome = input("Nome da República: ")
    login = input("Login da República: ")
    senha = input("Senha: ")
    telefone = input("Telefone do responsável: ")
    instagram = input("@Instagram da República: ")

    print("\nSelecione o tipo de república que melhor descreve sua casa.")
    tipo = selecionar_tipo_republica()

    republica = Republica(nome, login, senha, telefone, instagram, tipo)
    republicas.append(republica)
    salvar_dados(republicas, REPUBLICAS_FILE)
    print("\nRepública cadastrada com sucesso!")