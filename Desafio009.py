#DESAFIO009 Faça um programa que leia um número inteiro qualquer e mostre sua tabuada.

print('{0}TABUADA{0}'.format('-'*20))
t = int(input('Digite um número:'))
print('A Tabuada do número {} é:'.format(t))
print('{0} x  1 = {1:2} \n{0} x  2 = {2:2} \n{0} x  3 = {3:2} \n{0} x  4 = {4:2} \n{0} x  5 = {5:2} \n{0} x  6 = {5:2}\n{0} x  7 = {7:2} \n{0} x  8 = {8:2} \n{0} x  9 = {9:2} \n{0} x 10 = {10:2} '.format(t, t*1,t*2, t*3 ,t*4, t*5, t*6, t*7, t*8, t*9, t*10))