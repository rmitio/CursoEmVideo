#DESAFIO019 Um professor quer sortear um dos seus quatroa alunos para apagar o quadro. Faça ele, lendo o nome

from random import choice

a1 = input('Digite o nome do 1º Aluno: ')
a2 = input('Digite o nome do 2º Aluno: ')
a3 = input('Digite o nome do 3º Aluno: ')
a4 = input('Digite o nome do 4º Aluno: ')
lista = [a1, a2, a3, a4]
s = choice(lista)
print('O Aluno sorteado foi {}'.format(s))
