#DESAFIO013 Faça um algoritmo que leia um salário e mostre seu novo salário, com 15% de aumento.
print('{0} AUMENTO DE SALÁRIO {0}'.format('$*'*20))
sal = float(input('Digite seu salário: R$'))
print('Seu salário atual é R${:.2f} e com aumento de 15% seu salário será de R${:.2f}'.format(sal, sal+(sal*0.15)))

