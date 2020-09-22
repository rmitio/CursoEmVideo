#DESAFIO0113 Reescreva a função leiaInt() que fizemos no desafio 104, incliundo agora a posibilidade da digitação de um número de tipo inválido. Aproveite e crie também a função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n



def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número Real válido. \033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor Inteiro digitadao foi {n1}')
print(f'O valor Real digitadao foi {n2}')