from abc import ABC, abstractmethod

class Usuario(ABC):
    """
    Classe abstrata que representa um usuário genérico do sistema
    (pode ser Estudante ou República).
    """
    def __init__(self, username, password, nome, telefone, instagram):
        self.username = username
        self.password = password
        self.nome = nome
        self.telefone = telefone
        self.instagram = instagram

    @abstractmethod
    def preencher_formulario(self):
        pass

    def checar_senha(self, password):
        return self.password == password


class Estudante(Usuario):
    def __init__(self, username, password, nome, telefone, instagram):
        super().__init__(username, password, nome, telefone, instagram)
        self.respostas = {}
        self.personalidade = {}  # Guardará as classificações de cada categoria
        self.perfil_final = None

    def preencher_formulario(self):
        """
        Recebe as 30 perguntas, cada resposta é de 0 a 5,
        e salva no dict self.respostas.
        """
        print(f"\n--- Formulário de Estudante ({self.username}) ---")

        perguntas = [
            # 1 a 5 (Extroversão)
            "Em uma festa, você prefere interagir com muitas pessoas?",
            "Você costuma fazer novos amigos com facilidade?",
            "Prefere atividades em grupo em vez de atividades individuais?",
            "Você se sente confortável em iniciar conversas com desconhecidos?",
            "É importante para você ter uma vida social ativa?",
            # 6 a 10 (Organização)
            "Você costuma planejar seu dia com antecedência?",
            "Você se considera uma pessoa organizada?",
            "É comum você seguir prazos e compromissos?",
            "Você prefere manter seus espaços pessoais limpos e arrumados?",
            "Você se incomoda quando outras pessoas são desorganizadas?",
            # 11 a 15 (Tolerância e Flexibilidade)
            "Você é flexível com mudanças de planos?",
            "Consegue lidar bem com pessoas de hábitos muito diferentes dos seus?",
            "Você prefere ambientes onde há poucas regras?",
            "É fácil para você perdoar pequenas falhas nos outros?",
            "Consegue manter a calma em situações de conflito?",
            # 16 a 20 (Hábitos Diários)
            "Você gosta de acordar cedo?",
            "Prefere noites tranquilas em casa a saídas animadas?",
            "Você tem horários regulares para comer e dormir?",
            "Costuma fazer muito barulho em casa (música alta, TV, etc.)?",
            "Você é uma pessoa que gosta de cozinhar em casa?",
            # 21 a 25 (Preferências Pessoais)
            "Você prefere ambientes minimalistas e silenciosos?",
            "Gosta de compartilhar refeições e tempo com colegas de casa?",
            "Prefere ambientes com muitas plantas e decorações naturais?",
            "Gosta de animais de estimação em casa?",
            "Você tem hobbies que ocupam muito espaço (como instrumentos musicais ou artes)?",
            # 26 a 30 (Conflitos e Resolução)
            "Você evita confrontos diretos em situações de desacordo?",
            "Você busca resolver problemas de convivência rapidamente?",
            "Acha importante comunicar suas expectativas claramente?",
            "Costuma deixar os outros tomarem a iniciativa em resolver conflitos?",
            "Você consegue separar sentimentos pessoais de questões práticas?",
        ]

        self.respostas.clear()

        for i, pergunta in enumerate(perguntas, start=1):
            while True:
                try:
                    valor = int(input(f"{i}. {pergunta} (0 a 5): "))
                    if 0 <= valor <= 5:
                        self.respostas[f"Pergunta {i}"] = valor
                        break
                    else:
                        print("Por favor, insira um valor entre 0 e 5.")
                except ValueError:
                    print("Entrada inválida. Digite um número entre 0 e 5.")

        print("\nFormulário de Estudante preenchido com sucesso!")

    def determinar_personalidade(self):
        """
        Somar cada bloco de 5 perguntas, classificar em faixas e,
        com base nas combinações, definir o perfil final.
        Salva o resultado em self.perfil_final e também armazena
        as classificações parciais em self.personalidade.
        """
        if len(self.respostas) < 30:
            print("Você não preencheu todas as 30 perguntas ainda.")
            return
        
        # 1. Somar cada bloco
        sum_extro = sum(self.respostas[f"Pergunta {i}"] for i in range(1, 6))
        sum_org = sum(self.respostas[f"Pergunta {i}"] for i in range(6, 11))
        sum_flex = sum(self.respostas[f"Pergunta {i}"] for i in range(11, 16))
        sum_hab = sum(self.respostas[f"Pergunta {i}"] for i in range(16, 21))
        sum_pref = sum(self.respostas[f"Pergunta {i}"] for i in range(21, 26))
        sum_conf = sum(self.respostas[f"Pergunta {i}"] for i in range(26, 31))

        # 2. Classificar cada soma em: 0-8, 9-17, 18-25
        cat_extro = self._classificar_extroversao(sum_extro)
        cat_org = self._classificar_organizacao(sum_org)
        cat_flex = self._classificar_flexibilidade(sum_flex)
        cat_hab = self._classificar_habitos(sum_hab)
        cat_pref = self._classificar_preferencias(sum_pref)
        cat_conf = self._classificar_conflitos(sum_conf)

        # Armazenar no dicionário self.personalidade, se quiser exibir depois
        self.personalidade = {
            "Extroversão e Socialização": cat_extro,
            "Organização e Responsabilidade": cat_org,
            "Tolerância e Flexibilidade": cat_flex,
            "Hábitos Diários e Estilo de Vida": cat_hab,
            "Preferências Pessoais": cat_pref,
            "Conflitos e Resolução": cat_conf
        }

        # 3. Determinar perfil final (match_profile)
        self.perfil_final = self._match_profile(cat_extro, cat_org, cat_flex, cat_hab, cat_pref, cat_conf)

        print("\nClassificações Parciais:")
        for k, v in self.personalidade.items():
            print(f" - {k}: {v}")
        print(f"\nPerfil Final: {self.perfil_final}")

    ### Métodos privados de classificação

    def _classificar_extroversao(self, score):
        if 0 <= score <= 8:
            return "Introvertido"
        elif 9 <= score <= 17:
            return "Ambivertido"
        else:
            return "Extrovertido"

    def _classificar_organizacao(self, score):
        if 0 <= score <= 8:
            return "Espontâneo"
        elif 9 <= score <= 17:
            return "Moderadamente Organizado"
        else:
            return "Altamente Organizado"

    def _classificar_flexibilidade(self, score):
        if 0 <= score <= 8:
            return "Inflexível"
        elif 9 <= score <= 17:
            return "Moderadamente Flexível"
        else:
            return "Altamente Flexível"

    def _classificar_habitos(self, score):
        if 0 <= score <= 8:
            return "Noturno e Relaxado"
        elif 9 <= score <= 17:
            return "Equilibrado"
        else:
            return "Diurno e Estruturado"

    def _classificar_preferencias(self, score):
        if 0 <= score <= 8:
            return "Independente"
        elif 9 <= score <= 17:
            return "Moderadamente Social"
        else:
            return "Cooperativo"

    def _classificar_conflitos(self, score):
        if 0 <= score <= 8:
            return "Evitador"
        elif 9 <= score <= 17:
            return "Neutro"
        else:
            return "Resolutivo"

    ### Método privado para casar o perfil final (9 possibilidades)

    def _match_profile(self, extro, org, flex, hab, pref, conf):
        """
        Casamos as combinações para chegar nos 9 perfis possíveis.
        """
        # 1. Líder Sociável = Extrovertido + Altamente Organizado + Resolutivo
        if extro == "Extrovertido" and org == "Altamente Organizado" and conf == "Resolutivo":
            return "Líder Sociável"
        # 2. Criativo Independente = Introvertido + Espontâneo + Independente
        elif extro == "Introvertido" and org == "Espontâneo" and pref == "Independente":
            return "Criativo Independente"
        # 3. Flexível Harmonizador = Ambivertido + Moderadamente Flexível + Cooperativo
        elif extro == "Ambivertido" and flex == "Moderadamente Flexível" and pref == "Cooperativo":
            return "Flexível Harmonizador"
        # 4. Organizado Pacifista = Introvertido + Altamente Organizado + Neutro
        elif extro == "Introvertido" and org == "Altamente Organizado" and conf == "Neutro":
            return "Organizado Pacifista"
        # 5. Extrovertido Descontraído = Extrovertido + Espontâneo + Noturno e Relaxado
        elif extro == "Extrovertido" and org == "Espontâneo" and hab == "Noturno e Relaxado":
            return "Extrovertido Descontraído"
        # 6. Mediador Empático = Ambivertido + Moderadamente Flexível + Resolutivo
        elif extro == "Ambivertido" and flex == "Moderadamente Flexível" and conf == "Resolutivo":
            return "Mediador Empático"
        # 7. Organizado Extrovertido = Extrovertido + Altamente Organizado
        elif extro == "Extrovertido" and org == "Altamente Organizado":
            return "Organizado Extrovertido"
        # 8. Introvertido Flexível = Introvertido + Altamente Flexível
        elif extro == "Introvertido" and flex == "Altamente Flexível":
            return "Introvertido Flexível"
        # 9. Social e Resolutivo = Cooperativo + Resolutivo
        elif pref == "Cooperativo" and conf == "Resolutivo":
            return "Social e Resolutivo"
        else:
            return "Perfil não mapeado"


class Republica(Usuario):
    def __init__(self, username, password, nome, telefone, instagram):
        super().__init__(username, password, nome, telefone, instagram)
        self.tipo_escolhido = None
        self.descricao_tipo = None

    def preencher_formulario(self):
        print(f"\n--- Formulário de República ({self.username}) ---")
        opcoes = {
            "1": ("Tipo 1-", "Essa república é ideal para pessoas sociáveis que gostam de ter a casa organizada e resolver problemas de forma prática e rápida. A casa valoriza eventos em grupo, como reuniões semanais, festas e estudos colaborativos. Os moradores preferem um ambiente animado, mas com regras claras para manter a convivência harmoniosa."),
            "2": ("Tipo 2-", "Uma república tranquila e flexível, voltada para quem valoriza privacidade e liberdade. Não existem muitas regras rígidas, e os moradores têm total autonomia sobre seus espaços pessoais. Ideal para pessoas criativas, introspectivas e que gostam de manter a convivência simples e leve, sem muita imposição de rotinas."),
            "3": ("Tipo 3-", "Essa república é voltada para estudantes que gostam de equilibrar socialização e privacidade. A convivência é baseada em colaboração, com tarefas divididas de forma justa e flexível. Perfeita para quem quer um ambiente agradável e amigável, mas sem excessos em festas ou regras rígidas."),
            "4": ("Tipo 4-", "Uma república ideal para pessoas descontraídas e que preferem horários flexíveis. Perfeita para quem gosta de estudar à noite, curtir música, jogar videogames ou até mesmo organizar encontros informais com amigos. Não é a melhor opção para quem gosta de muita ordem ou silêncio constante."),
            "5": ("Tipo 5-", "Um ambiente reservado, com regras claras e espaços bem organizados. É a escolha ideal para quem prefere calma, silêncio e foco nos estudos. Conflitos são raros, pois os moradores respeitam as regras e buscam um convívio equilibrado.")
        }
        for k, v in opcoes.items():
            print(f"{k}. {v[0]} - \"{v[1]}\"\n")

        while True:
            escolha = input("Escolha o tipo de república (1 a 5): ")
            if escolha in opcoes:
                self.tipo_escolhido = opcoes[escolha][0]
                self.descricao_tipo = opcoes[escolha][1]
                print(f"Tipo escolhido: {self.tipo_escolhido}")
                return
            else:
                print("Opção inválida. Tente novamente.")
