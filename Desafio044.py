#DESAFIO044 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de ppagamento: -à vista dinheiro/cheque: 10% de desconto - à vista no cartão: 5% de desconto -em até 2x no cartão: preço normal - 3x ou mais no cartão: 20% de juros

preço = float(input('Digite o valor do produto. R$ '))
print('''1 - Á Vista (Dinheiro ou cheque)
2 - Á Vista no cartão
3 - até 2x no cartão
4 - 3x ou mais no cartão
''')
pagamento = int(input('Escolha a forma de pagamento: N'))

if pagamento == 1:
    preço = preço - ((preço * 10) / 100)
elif pagamento == 2:
    preço = preço - ((preço * 5) / 100)
elif pagamento == 3:
    preço = preço
elif pagamento == 4:
    preço = preço = preço + ((preço*20)/100)
else:
    print('Escolha entre as opções acima!')
print('O valor final é R${:.2f}'.format(preço))