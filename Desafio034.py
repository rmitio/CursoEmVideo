#DESAFIO034 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite seu salário: R$ '))

#sal > 1250 10%
#sal < 1250 15%

if sal > 1250:
    novo = sal + (sal * 10 / 100)
else:
    novo = sal + (sal * 15 / 100)

print('Quem ganhava R${:.2f} passa a ganhar R$ {:.2f} agora'.format(sal, novo))