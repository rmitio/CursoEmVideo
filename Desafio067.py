#DESAFIO067 Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

n = 0
while True:
    n = int(input('Digite um valor para mostrar a tabuada(negativo para parar): '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {c*n}')