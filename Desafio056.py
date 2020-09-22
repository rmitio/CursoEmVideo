'''DESAFIO056 Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final, do programa mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.'''

soma = 0
media = 0
maiorhomem = 0
nomevelho = ''
qtm20 = 0
for c in range(1, 5):
    print('---- {}ª PESSOA-----'.format(c))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [M/F]')).strip()
    soma += idade
    if c == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        qtm20 += 1
media = soma/4
print('A média de idade do grupo é de {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorhomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(qtm20))