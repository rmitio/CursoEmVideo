#DESAFIO0104 Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor númerico. Ex: n = leiaInt('Digite um n')

def leiaInt(m):
    n = input(m)
    while n not in '0123456789':
        n = input(m)
    return n


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
