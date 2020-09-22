#DESAFIO014 Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
#formaula (0 °C × 9/5) + 32 = 32 °F

c = float(input('Digite a temperatura em ºC: '))
f = (c * 9/5) + 32
print('A temperatura em que você digitou é {}ºC e convertida fica {}ºF!'.format(c,f))