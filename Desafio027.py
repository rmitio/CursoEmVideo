#DESAFIO027 Faça um programa que leia o nome de uma pessoa mostrando em seguida o primeiro e o último nome separadamente. EX. Ana Maria de Souza primeiro: Ana último: Souza
nome = input('Digite seu nome completo: ')
div = nome.split()
print('primeiro:{}\nultimo: {}'.format(div[0], div[len(div)-1]))
