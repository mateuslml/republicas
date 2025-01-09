from usuarios import Usuario

class LiderSociavel(Usuario):
    descricao = "Extrovertido, Altamente Organizado e Resolutivo"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CriativoIndependente(Usuario):
    descricao = "Introvertido, Espontâneo e Independente"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class FlexivelHarmonizador(Usuario):
    descricao = "Ambivertido, Moderadamente Flexível e Cooperativo"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class OrganizadoPacifista(Usuario):
    descricao = "Introvertido, Altamente Organizado e Neutro"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ExtrovertidoDescontraido(Usuario):
    descricao = "Extrovertido, Espontâneo e Noturno"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class MediadorEmpatico(Usuario):
    descricao = "Ambivertido, Moderadamente Flexível e Resolutivo"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class OrganizadoExtrovertido(Usuario):
    descricao = "Extrovertido e Altamente Organizado"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class IntrovertidoFlexivel(Usuario):
    descricao = "Introvertido e Altamente Flexível"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class SocialResolutivo(Usuario):
    descricao = "Cooperativo e Resolutivo"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def determinar_perfil(categorias):
    """
    Determina o perfil do usuário com base nas categorias calculadas.
    """
    if categorias["Extroversão e Socialização"] >= 18 and \
       categorias["Organização e Responsabilidade"] >= 18 and \
       categorias["Conflitos e Resolução"] >= 18:
        return LiderSociavel
    elif categorias["Extroversão e Socialização"] <= 8 and \
         categorias["Organização e Responsabilidade"] <= 8 and \
         categorias["Preferências Pessoais"] <= 8:
        return CriativoIndependente
    elif 9 <= categorias["Extroversão e Socialização"] <= 17 and \
         9 <= categorias["Tolerância e Flexibilidade"] <= 17 and \
         18 <= categorias["Conflitos e Resolução"]:
        return MediadorEmpatico
    elif categorias["Extroversão e Socialização"] <= 8 and \
         categorias["Organização e Responsabilidade"] >= 18:
        return OrganizadoPacifista
    elif categorias["Extroversão e Socialização"] >= 18 and \
         categorias["Tolerância e Flexibilidade"] <= 8:
        return ExtrovertidoDescontraido
    elif categorias["Extroversão e Socialização"] >= 18 and \
         categorias["Organização e Responsabilidade"] >= 18:
        return OrganizadoExtrovertido
    elif categorias["Extroversão e Socialização"] <= 8 and \
         categorias["Tolerância e Flexibilidade"] >= 18:
        return IntrovertidoFlexivel
    elif categorias["Preferências Pessoais"] >= 18 and \
         categorias["Conflitos e Resolução"] >= 18:
        return SocialResolutivo
    else:
        return FlexivelHarmonizador