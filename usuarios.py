class Usuario:
    """
    Classe base para representar um usuário genérico no sistema.
    """
    def __init__(self, login, senha, nome, telefone, instagram, respostas_formulario=None):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.telefone = telefone
        self.instagram = instagram
        self.respostas_formulario = respostas_formulario or {}

    def exibir_informacoes(self):
        return {
            "Nome": self.nome,
            "Telefone": self.telefone,
            "Instagram": self.instagram,
            "Respostas do Formulário": self.respostas_formulario,
        }

    def visualizar_personalidade(self):
        if not self.respostas_formulario:
            return "O formulário ainda não foi respondido."

        categorias = determinar_personalidade(self.respostas_formulario)
        perfil = determinar_perfil(categorias)
        resultado = "\n--- Resultado de Personalidade ---\n"
        for categoria, valor in categorias.items():
            resultado += f"{categoria}: {valor}\n"
        resultado += f"\nPerfil Determinado: {perfil.descricao}\n"
        return resultado

    def to_dict(self):
        return {
            "login": self.login,
            "senha": self.senha,
            "nome": self.nome,
            "telefone": self.telefone,
            "instagram": self.instagram,
            "respostas_formulario": self.respostas_formulario,
        }

    @staticmethod
    def from_dict(data):
        return Usuario(
            data["login"], 
            data["senha"], 
            data["nome"], 
            data["telefone"], 
            data["instagram"], 
            data.get("respostas_formulario")
        )
