#DESAFIO060 Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex 5! 5x4x3x2x1 = 120

'''n = int(input('Digite um número:'))
resultado = 1
for c in range(n, 0, -1):
    if c != 1:
        print(' {} '.format(c), end='X')
    else:
        print(' {} '.format(c), end='=')
    resultado *= c
print(' {}'.format(resultado))'''

n = int(input('Digite um número:'))
resultado = 1
c = n
while c != 0:

    if c != 1:
        print(' {} '.format(c), end='X')
    else:
        print(' {} '.format(c), end='=')
    resultado *= c
    c -= 1
print(' {}'.format(resultado))
