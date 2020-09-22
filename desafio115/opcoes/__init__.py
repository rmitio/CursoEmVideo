from desafio115.impressoes import imprimir_cabecalho


def cadastrar(nome, idade):
    leitura = open('dados.txt', 'r')
    ler = leitura.readlines()
    ler.append(nome)
    ler.append('\t')
    ler.append(idade)
    escrever = open('dados.txt', 'w')
    escrever.write('\n')
    escrever.writelines(ler)
    leitura.close()
    escrever.close()


def listar():
    ler = open('dados.txt', 'r')
    lista = ler.read()
    ler.close()
    return lista

def sair():
    imprimir_cabecalho('Volte Sempre!')

