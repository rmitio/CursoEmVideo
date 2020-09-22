#DESAFIO072 Crie um programa que tenha uma tupla totalmente preenchiad com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.

números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

n = int(input('Digite um número entre 0 e 20: '))

while True:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente.', end='')


print(f'Você digitou o número {números[n]}')