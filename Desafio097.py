'''DESAFIO097 Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva('Olá, Mundo')

Saída:
----------
Olá, Mundo
----------'''

def escreva(txt):
    t = len(txt)
    print('~' * t)
    print('  {txt}')
    print('~' * t)


texto = str(input('Digite o texto: '))
escreva(texto)