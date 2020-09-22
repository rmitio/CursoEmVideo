#DESAFIO036 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quaantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.

vc = float(input('Qual o Valor da Casa: R$'))
sal = float(input('Qual o seu salário: R$'))
anos = int(input('Em quantos anos pretende pagar a Casa:'))

maxp = (sal * 30) / 100
tempo = anos * 12
vp = vc/tempo
print('Para pagar uma casa no valor R${:.2f} em {} anos, a prestação será R${:.2f}'.format(vc,anos, vp))
if vp >= maxp:
    print('Negado!')
else:
    print('Aprovado')
