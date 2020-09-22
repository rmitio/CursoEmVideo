#DESAFIO076 Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)


'''p = 0
while p < len(produtos):
    print(f'{produtos[p]:.<30}R${produtos[p+1]:7.2f}')
    p += 2'''
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>7.2f}')