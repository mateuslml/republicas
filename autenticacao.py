from cadastro import usuarios, republicas

def autenticar_usuario(login, senha):
    for usuario in usuarios:
        if usuario.login == login and usuario.senha == senha:
            print(f"\nBem-vindo(a), {usuario.nome}!\n")
            return usuario
    print("\nUsuário ou senha inválidos. Tente novamente.\n")
    return None

def autenticar_republica(login, senha):
    for republica in republicas:
        if republica.login == login and republica.senha == senha:
            print(f"\nBem-vindo(a) à República {republica.nome}!\n")
            return republica
    print("\nLogin ou senha inválidos. Tente novamente.\n")
    return None
