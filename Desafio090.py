#DESAFIO090 Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

dados = dict()

dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input(f'Média de {dados["Nome"]}:'))
print(f'O Nome é {dados["Nome"]} ')
print(f'Média é igual a {dados["Média"]}')
if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'
print(f'Situação é igual a {dados["Situação"]}')
