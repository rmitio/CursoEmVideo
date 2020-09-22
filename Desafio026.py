#DESAFIO026 Faça um programa que leia uma frase pelo teclado e mostre: Quantas Vezes aparece a letra "A". Em que posição ela aparece a primeira vez. Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip()
print('A frase tem {} letras a, ela aparece na {}ª posição pela primeira vez e na {}ª posição pela ultima vez!'.format(frase.count('a'), frase.lower().find('a')+1, frase.lower().rfind('a')+1))
