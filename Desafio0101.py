#DESAFIO0101 Crie um programa que tenha um função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem o voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições



def voto(nasc):
    from datetime import datetime
    atual = datetime.today().year
    idade = atual - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 18 > idade >= 16 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTA OBRIGATÓRIO'


n = int(input('Em que ano você nasceu? '))
print(voto(n))




