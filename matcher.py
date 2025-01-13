
import json
import os

class DataCollector:
    """
    Esta classe varre o user_data.json e coleta:
      - Quais repúblicas existem (username, tipo_escolhido, descricao_tipo, etc.)
      - Quais estudantes existem (username, perfil_final, etc.)
    """

    def __init__(self, file_path="user_data.json"):
        self.file_path = file_path
        self.republicas = []   # lista de dicionários
        self.estudantes = []   # lista de dicionários

    def collect_data(self):
        """Lê o user_data.json e preenche self.republicas e self.estudantes."""
        if not os.path.exists(self.file_path):
            print("Arquivo JSON não encontrado. Nenhum dado coletado.")
            return
        
        with open(self.file_path, "r", encoding="utf-8") as f:
            data_list = None
            try:
                data_list = json.load(f)   # É uma lista de objetos (Estudante ou República)
            except json.JSONDecodeError:
                print("Erro ao decodificar o JSON. Arquivo vazio ou inválido?")
                return

        if not data_list:
            print("Nenhum dado encontrado no JSON.")
            return

        # Percorrer cada objeto no data_list
        for item in data_list:
            tipo = item.get("tipo")
            if tipo == "republica":
                # Extraímos dados básicos da república
                self.republicas.append({
                    "username": item["username"],
                    "nome": item["nome"],
                    "telefone": item["telefone"],
                    "instagram": item["instagram"],
                    "tipo_escolhido": item.get("tipo_escolhido"),
                    "descricao_tipo": item.get("descricao_tipo")
                })
            elif tipo == "estudante":
                # Pegar perfil_final 
                self.estudantes.append({
                    "username": item["username"],
                    "nome": item["nome"],
                    "telefone": item["telefone"],
                    "instagram": item["instagram"],
                    "perfil_final": item.get("perfil_final")
                })
        # Agora self.republicas e self.estudantes estão preenchidas

    def get_republicas(self):
        return self.republicas

    def get_estudantes(self):
        return self.estudantes


class MatchMaker:
    """
    Classe que realiza o match entre o perfil final do estudante
    e as repúblicas cadastradas.
    """

    def __init__(self, data_collector):
        self.dc = data_collector
        # Exemplo de tabela de compatibilidade:
        self.match_rules = {
            "Líder Sociável": ["República Líder Social", "República Equilíbrio e Paz"],
            "Extrovertido Descontraído": ["República Líder Social", "República Relax Noturna"],
            "Organizado Pacifista": ["República Equilíbrio e Paz"],
            "Criativo Independente": ["República Criativa e Livre"],
            "Flexível Harmonizador": ["República Harmonia Flex"],
            "Mediador Empático": ["República Harmonia Flex", "República Equilíbrio e Paz"],
        }

    def match_republicas_for(self, perfil_final):
        """
        Retorna uma lista de repúblicas (dicionários) que combinam
        com o 'perfil_final' do estudante.
        """
        # 1. Obter a lista de repúblicas
        republicas = self.dc.get_republicas()

        # 2. Ver se o perfil_final está mapeado na match_rules
        tipos_compat = self.match_rules.get(perfil_final)
        if not tipos_compat:
            # Se não estiver mapeado, assumimos que não há regras definidas
            return []

        # 3. Filtrar as repúblicas cujo "tipo_escolhido" esteja em tipos_compat
        matched = []
        for rep in republicas:
            tipo_r = rep.get("tipo_escolhido")
            if tipo_r and tipo_r in tipos_compat:
                matched.append(rep)

        return matched

    def exibir_republicas_compat(self, perfil_final):
        """
        Exibe na tela as repúblicas compatíveis com esse perfil.
        """
        matched = self.match_republicas_for(perfil_final)
        if not matched:
            print(f"\nNão há repúblicas compatíveis com o perfil '{perfil_final}' ou não definimos regras para este perfil.\n")
            return
        
        print(f"\nRepúblicas compatíveis com o perfil '{perfil_final}':\n")
        for rep in matched:
            print(f" - {rep['tipo_escolhido']} de {rep['nome']} (User: {rep['username']})")
            print(f"   Telefone: {rep['telefone']}")
            print(f"   Instagram: {rep['instagram']}")
            if rep["descricao_tipo"]:
                print(f"   Descrição: {rep['descricao_tipo']}")
            print()
