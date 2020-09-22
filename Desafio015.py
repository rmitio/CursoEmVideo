#DESAFIO015 Escreva um programa que perguunte a quantidade de Km percorridos por um carro alugado e a quantidade  de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
kp = float(input('Digite os km percorridos: '))
d = int(input('Quantos dias ele foi alugado: '))
p = (d * 60) + (kp * 0.15)
print('O Carro foi alugado por {} dias, e foram rodados {}km, portanto o valor total a pagar é R${:.2f}'.format(d, kp, p))
