class Republica:
    """
    Superclasse que representa uma república genérica no sistema.
    """
    def __init__(self, nome, login, senha, telefone, instagram, tipo=None):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.telefone = telefone
        self.instagram = instagram
        self.tipo = tipo

    def exibir_informacoes(self):
        return {
            "Nome da República": self.nome,
            "Telefone": self.telefone,
            "Instagram": self.instagram,
            "Tipo de República": self.tipo,
        }

    def to_dict(self):
        return {
            "nome": self.nome,
            "login": self.login,
            "senha": self.senha,
            "telefone": self.telefone,
            "instagram": self.instagram,
            "tipo": self.tipo,
        }

    @staticmethod
    def from_dict(data):
        return Republica(data["nome"], data["login"], data["senha"], data["telefone"], data["instagram"], data.get("tipo"))