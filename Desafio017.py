#DESAFIO017 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = int(input('Digite o cateto oposto: '))
ca = int(input('Digite o cateto adjacente: '))
h = hypot(ca, co)
print('O cateto adjacente é {} o cateto oposto é {} e a hipotenusa é {}'.format(ca, co, int(h)))