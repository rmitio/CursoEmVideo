'''DESAFIO075 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, Mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares.'''

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))
n3 = int(input('Digite um valor:'))
n4 = int(input('Digite um valor:'))
t = (n1, n2, n3, n4)
print(f'Você digitou {t}')
print(f'O número 9 apareceu {t.count(9)} vezes')
if 3 not in t:
    print('O número 3 não foi digitado')
else:
    print(f'O número 3 foi digitado primeiro na posição {t.index(3)+1}')
print('Números pares: ', end='')
for p in t:
    if p % 2 == 0:
        print(p, end=' ')