'''DESAFIO070 Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. no final mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000
C) Qual o nome do produto mais barato.'''
t = m1000 = mbp = 0
mb = ''
while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    preço = float(input('Preço: R$'))
    c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    t += preço
    if mb == '':
        mb = produto
        mbp = preço
    elif preço < mbp:
        mb = produto
        mbp = preço
    if preço > 1000.00:
        m1000 += 1
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if c == 'N':
            break
    if c == 'N':
        break
print(f'O total da compra foi R${t:.2f}')
print(f'Temos {m1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {mb} que custa R${mbp:.2f}')
