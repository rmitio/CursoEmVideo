#DESAFIO039 Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade: - Se ele ainda vai se alistar ao serviço militar. - Se é a hora de se alistar. - Se já passou do tempo de alistamento. Seu programa também deverá mostrar o tempoo que falta ou que passou do prazo.
import datetime
atual = datetime.date.today().year
ano = int(input('Digite o seu ano de nascimento: '))
idade = atual - ano

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade == 18:
    print('Você tem que se alistas IMEDIATAMENTE!')
elif idade < 18:
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(18-idade))
else:
    print('Você já deveria ter se alistado há {} anos'.format(idade-18))

