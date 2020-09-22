#DESAFIO096 Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e copmrimento) e mostre a área do terreno
print('Controle de Terrenos')
print('-'*20)


def área(lar, com):
    print(f'A área de um terreno {lar}x{com} é de {lar*com}m²')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)