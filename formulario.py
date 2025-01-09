def perguntas_formulario():
    perguntas = [
        "Em uma festa, você prefere interagir com muitas pessoas?",
        "Você costuma fazer novos amigos com facilidade?",
        "Prefere atividades em grupo em vez de atividades individuais?",
        "Você se sente confortável em iniciar conversas com desconhecidos?",
        "É importante para você ter uma vida social ativa?",
        "Você costuma planejar seu dia com antecedência?",
        "Você se considera uma pessoa organizada?",
        "É comum você seguir prazos e compromissos?",
        "Você prefere manter seus espaços pessoais limpos e arrumados?",
        "Você se incomoda quando outras pessoas são desorganizadas?",
        "Você é flexível com mudanças de planos?",
        "Consegue lidar bem com pessoas de hábitos muito diferentes dos seus?",
        "Você prefere ambientes onde há poucas regras?",
        "É fácil para você perdoar pequenas falhas nos outros?",
        "Consegue manter a calma em situações de conflito?",
        "Você gosta de acordar cedo?",
        "Prefere noites tranquilas em casa a saídas animadas?",
        "Você tem horários regulares para comer e dormir?",
        "Costuma fazer muito barulho em casa (música alta, TV, etc.)?",
        "Você é uma pessoa que gosta de cozinhar em casa?",
        "Você prefere ambientes minimalistas e silenciosos?",
        "Gosta de compartilhar refeições e tempo com colegas de casa?",
        "Prefere ambientes com muitas plantas e decorações naturais?",
        "Gosta de animais de estimação em casa?",
        "Você tem hobbies que ocupam muito espaço (como instrumentos musicais ou artes)?",
        "Você evita confrontos diretos em situações de desacordo?",
        "Você busca resolver problemas de convivência rapidamente?",
        "Acha importante comunicar suas expectativas claramente?",
        "Costuma deixar os outros tomarem a iniciativa em resolver conflitos?",
        "Você consegue separar sentimentos pessoais de questões práticas?",
    ]

    respostas = {}
    print("\n--- Formulário de Perfil ---")
    for i, pergunta in enumerate(perguntas, start=1):
        while True:
            try:
                resposta = int(input(f"{i}. {pergunta} (0 a 5): "))
                if 0 <= resposta <= 5:
                    respostas[f"Pergunta {i}"] = resposta
                    break
                else:
                    print("Por favor, insira um valor entre 0 e 5.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número entre 0 e 5.")
    return respostas

def determinar_personalidade(respostas):
    categorias = {
        "Extroversão e Socialização": sum(respostas[f"Pergunta {i}"] for i in range(1, 6)),
        "Organização e Responsabilidade": sum(respostas[f"Pergunta {i}"] for i in range(6, 11)),
        "Tolerância e Flexibilidade": sum(respostas[f"Pergunta {i}"] for i in range(11, 16)),
        "Hábitos Diários e Estilo de Vida": sum(respostas[f"Pergunta {i}"] for i in range(16, 21)),
        "Preferências Pessoais": sum(respostas[f"Pergunta {i}"] for i in range(21, 26)),
        "Conflitos e Resolução": sum(respostas[f"Pergunta {i}"] for i in range(26, 31))
    }

    return categorias
