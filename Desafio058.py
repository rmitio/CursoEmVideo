#DESAFIO058 Melhore o jogo do DESAFIO028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


from random import randint
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente advinhar ...')
print('-=-' * 20)
computador  = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual Número pensei?'))
    palpites += 1
    if jogador == computador:
        print('PARABÉNS! Você acertou!')
        acertou = True
    else:
        if jogador < computador:
            print('O Nùmero é maior...Tente mais uma vez!')
        else:
            print('O Nùmero é menor...Tente mais uma vez!')
print('Você acertou o número em {} tentativas'.format(palpites))
