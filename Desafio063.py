#DESAFIO063 Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
#Ex. 0->1->1->2->3->5->8


n = int(input('Digite quantos números deseja ver da Sequência de Fibonacci:'))
n -= 3
c = 0
f1 = 0
f2 = 1
f = 0
print('{}->{}'.format(f1, f2), end='')
while c <= n:
    f = f1 + f2
    print('->{}'.format(f), end='')
    f1 = f2
    f2 = f
    c += 1