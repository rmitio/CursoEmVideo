tam = 40

def imprimir_cabecalho(texto):
    print('-' * tam)
    print(texto.center(tam))
    print('-' * tam)


def imprimir_opcoes(lista, cor1='\033[m', cor2='\033[m', separacao=''):
    for l in range(0, len(lista), 2):
        print(cor1, end='')
        print(lista[l], end=separacao)
        print(cor2, end='')
        print(lista[l+1], end='')
        print('\033[m')
    print('-' * tam)


def imprimir_cadatros(lista):
    print(lista)


def imprimir_erro(opcao='opção'):
    print(f'\033[32mERRO: Por favor, digite um {opcao} válido. \033[m')