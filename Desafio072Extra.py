#Extra do Desafio 72 perguntar se deseja continuar

números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {números[n]}')
        c = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
        if c == 'N':
            break
        while c not in 'SN':
            c = str(input('Atenção!! Digite S para SIM e N para não. Deseja continuar: [S/N]')).strip().upper()[0]
    else:
        print('Tente novamente.', end='')


