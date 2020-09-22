#DESAFIO049 Refaça o DESAFIO009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite o número que deseja ver a tabuada: '))
for c in range(0, 11):
    print('{} x {:2} = {:2}'.format(n, c, n*c))