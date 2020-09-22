#DESAFIO041 A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de  um atleta e mostre sua categoria, de acordo com a idade: - Até 9 Anos: MIRIM - Até 14 anos: INFANTIL - Até 19 anos: JUNIOR -Até 25 anos: Sénior - Acima: MASTER
from datetime import date
atual = date.today().year
n = int(input('Digite o ano de nascimento: '))
idade = atual - n
print('O Atleta tem {} anos.'.format(idade))
if idade < 9:
    print('MIRIM')
elif idade < 14:
    print('INFANTIL')
elif idade < 19:
    print('JUNIOR')
elif idade < 25:
    print('SENIOR')
else:
    print('MASTER')