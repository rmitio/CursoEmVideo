#DESAFIO079 Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso onúmero já exista lá dentro, ele não será adicionado. No final serão exibidos todos os valores únicos digitados, em ordem crescente.

numero = list()
while True:
    n = int(input('Digite um número: '))
    if n not in numero:
        numero.append(n)
        print('Número adicionado com Sucesso!')
    else:
        print('Número duplicado. Não vai ser adicionado')
    continuar = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Atenção Digite S para sim e N para não. Deseja Continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
numero.sort()
print(numero)