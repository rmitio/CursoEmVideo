#DESAFIO018 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cossenoe tangente desse ângulo
import math

a = int(input('Digite o ângulo: '))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))
print('O Valor do seno é {:.2f}, o valor do cosseno é {:.2f}, o valor da tangente é {:.2f}'.format(seno, cosseno, tangente))

