#DESAFIO010 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar


print('{0}-CONVERTENDO DOLAR-{0}'.format('$'*30))
r = float(input('Digite quanto você tem na carteira: R$'))
d = r/5.02
print('Você tem R${:.2f} na carteira e com isso pode comprar US${:.2f}'.format(r, d))