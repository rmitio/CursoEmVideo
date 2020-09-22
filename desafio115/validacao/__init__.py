from desafio115.impressoes import imprimir_erro


def valida_opcao(m):
    n = leiaInt(m)
    try:
        if int(n) < 4:
            return int(n)
    except ValueError:
        imprimir_erro()
        valida_opcao(m)


def valida_idade(idade):
    try:
        id = leiaInt(idade)
        return str(id)
    except:
        imprimir_erro('número inteiro')
        valida_idade(idade)

def leiaInt(m):
    n = input(m)
    try:
        int(n)
    except ValueError:
        imprimir_erro('Número inteiro')
        leiaInt(m)
    except KeyboardInterrupt:
        return 0
    return n
