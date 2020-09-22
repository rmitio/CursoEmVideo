'''DESAFIO059 Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa
''')
operação = int(input('Digite a operação desejada: '))

while operação != 5:
    if operação == 1:
        resultado = n1+n2
        print('Você escolheu Soma e o resultado foi {}'.format(resultado))
    elif operação == 2:
        resultado = n1 * n2
        print('Você escolheu Multiplicação e o resultado foi {}'.format(resultado))
    elif operação == 3:
        print('Você escolhou descobrir qual é o Maior!')
        if n1 > n2:
            print('{} é maior'.format(n1))
        elif n2 > n1:
            print('{} é maior'.format(n2))
        else:
            print('Os números são iguais.')
    elif operação == 4:
        print('Você decidiu digitar novos números')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    else:
        print('OPÇÃO INVALIDA! Digite uma opção valida')
        print('''        
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos Números
        [5] Sair do programa
        ''')
    operação = int(input('Digite a operação desejada: '))