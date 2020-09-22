#DESAFIO0102 Crie um programa que tenha um função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicado se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: número a ser calculado
    :param show: mostra ou não o calculo
    :return:
    """
    f = 1
    msg = ''
    for c in range(num, 0, -1):
        f *= c
        if c != 1:
            msg += f' {c} X'
        else:
            msg += f' {c} ='

    if show:
        return f'{msg} {f}'
    else:
        return f'O fatorial de {num} é {f}'


print(fatorial(4, True))

