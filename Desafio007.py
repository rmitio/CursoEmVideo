#DESAFIO007 Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

a = '-' * 30
print('{0}CALCULANDO MÉDIA{0}'.format(a))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Suas notas foram {} e {} e sua média é {}'.format(n1,n2,m))