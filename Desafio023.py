#DESAFIO023 Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. Ex. Digite um número: 1834 Unidade: 4 Dezena: 3 Centena: 8 Milhar: 1

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))





'''if len(num) == 1:
    print('Unidade: {0} \nDezena: {1} \nCentena: {1} \nMilhar: {1} '.format(num, 0))
elif len(num) == 2:
    print('Unidade: {0} \nDezena: {1} \nCentena: {2} \nMilhar: {2} '.format(num[1], num[0], 0))
elif len(num) == 3:
    print('Unidade: {0} \nDezena: {1} \nCentena: {2} \nMilhar: {3} '.format(num[2], num[1], num[0], 0))
elif len(num) == 4:
    print('Unidade: {0} \nDezena: {1} \nCentena: {2} \nMilhar: {3} '.format(num[3], num[2], num[1], num[0]))
'''
