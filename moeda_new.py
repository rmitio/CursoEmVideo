def aumentar(p, aum, formatado = True):
    if formatado:
        return f'R${p + ((p * aum) / 100):>7.2f}'
    else:
        return p + ((p * aum) / 100)


def diminuir(p, red, formatado = True):
    if formatado:
        return f'R${p - ((p * red) / 100):>7.2f}'
    else:
        return p - ((p * red) / 100)


def dobro(p, formatado = True):
    if formatado:
        return f'R${p * 2:>7.2f}'
    else:
        return p * 2


def metade(p, formatado = True):
    if formatado:
        return f'R${p / 2:>7.2f}'
    else:
        return p / 2


def moeda(p):
    return f'R${p:>7.2f}'


def resumo(p, aum, red):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'Preço Analisado:     {moeda(p)}')
    print(f'Dobro do Preço:      {dobro(p)}')
    print(f'Metade do Preço:     {metade(p)}')
    print(f'{aum}% de aumento:      {aumentar(p, aum)}')
    print(f'{red}% de redução:      {diminuir(p, red)}')
    print('-' * 40)
