#DESAFIO077 Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

palavras = ('teste', 'python', 'programa', 'delinquente', 'chaves', 'kiko', 'twix', 'lasanha', 'academia', 'guanabara', 'youtube')

for p in palavras:
    print(f'\nNa palavra {p} temos ', end=' ')
    for l in p:
        if l in 'aeiou':
            print(l, end =' ')


