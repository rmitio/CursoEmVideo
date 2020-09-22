from desafio115.impressoes import imprimir_cabecalho, imprimir_opcoes, imprimir_cadatros
from desafio115.validacao import valida_opcao, valida_idade
from desafio115.opcoes import *
#cores:
cor = {'Vermelho': '\033[31m',
       'Verde': '\033[32m',
       'Amarelo': '\033[33m',
       'Azul': '\033[34m',
       'Magenta': '\033[35m',
       'Ciano': '\033[36m',
       'Cinza': '\033[37m'
       }

while True:
       imprimir_cabecalho('MENU PRINCIPAL')
       test = [1, 'Ver pessoas cadastradas', 2, 'Cadastrar Nova Pessoa', 3, 'Sair do Sistema']
       imprimir_opcoes(test, cor['Amarelo'], cor['Azul'], ' - ' )
       op = valida_opcao('Sua opção: ')
       if op == 2:
              nome = input('Nome: ')
              idade = valida_idade('Idade: ')
              cadastrar(nome, idade)
              print(f'{nome} cadastrado com sucesso!')
       if op == 1:
              nomes = listar()
              imprimir_cadatros(nomes)
       else:
              if op == 3:
                     sair()
                     break


