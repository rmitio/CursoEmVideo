#DESAFIO029 Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 ppor cada km acima do limite.
v = int(input('Digite a velocidade  do carro: '))
if v > 80 :
    u = 7 * (v - 80)
    print('VOCÊ EXCEDEU O LIMITE DE VELOCIDADE!! Tem que pagar uma multa de R${:.2f}'.format(u))
else:
    print("Parabéns você está no limite!")