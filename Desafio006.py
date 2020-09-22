#DESAFIO006 Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.



print('{:=^20}DOBRO, TRIPLO E RAIZ QUADRADA{:=^20}'.format('-', '*'))
n = float(input('Digite um número: '))
#print('O Número que digitou foi {}, o dobro é {}, o triplo é {} e a raiz quadrada é {}!'.format(n, n*2, n*3, int(n**0.5)))
print('O Número que digitou foi {}, o dobro é {}, o triplo é {} e a raiz quadrada é {}!'.format(n, n*2, n*3, pow(n, (1/2))))
