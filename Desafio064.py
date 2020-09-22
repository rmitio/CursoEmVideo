#DESAFIO064 Crie um programa que leia vários números inteiros pelo telcado. O programa só vai parar qual o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
c = 0
s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print('A soma dos números digitados é {} e você digitou {} números.'.format(s, c))