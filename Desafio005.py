#DESAFIO005 faça  um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
print('{}SUCESSOR E ANTECESSOR{}'.format('-'*5, '-'*5))
n = int(input('Digite um número: '))
print('Você digitou o número {}, e o sucessor é {} e o antecessor é {}'.format(n, n+1, n-1))