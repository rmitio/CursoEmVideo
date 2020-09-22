#DESAFIO065 Crie um programa que leia vários números inteiros pelo telcado. No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valoreslidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
maior = menor = c = s = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um valor: '))
    continuar = str(input('Quer continuar? [S/N]'))
    c += 1
    if c == 1:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    s += n
média = s/c
print('A média dos valores é {}, o menor é {} e o maior é {}'.format(média,menor, maior))

