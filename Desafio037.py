#DESAFIO037 Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 - binário 2 -octal 3 - hexadecimal.

n = int(input('Digite um número qualquer: '))
print('''1 - Binário
2 - Octal
3 - Hexadécimal
    ''')
c = int(input('Escolha uma opção: '))
if c == 1:
    print('O Seu número em Binário é {}'.format(bin(n) [2:]))
elif c == 2:
    print('O Seu número em Decimal é {}'.format(oct(n)[2:]))
elif c == 3:
    print('O Seu número em Hexadecimal é {}'.format(hex(n)[2:]))
else:
    print('Escolha uma das opções!')