#DESAFIO031 Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km e R$ 0,45 para viagens mais longas.
d = int(input('Digite a distância  em KM: '))
if d <= 200:
    print(d*0.5)
else:
    print(d*0.45)