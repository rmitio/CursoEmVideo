#DESAFIO043 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: - Abaixo de 18.5: Abaixo do peso - Entre 18.5 e 25: Peso Ideal - 25 até 30: Sobrepeso - 30 até 40: Obesidade  - Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
IMC = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Abaixo do seu peso')
elif IMC > 18.5 and IMC < 25:
    print('Peso Ideal')
elif IMC > 25 and IMC < 30:
    print('Sobrepeso')
elif IMC > 30 and IMC < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
