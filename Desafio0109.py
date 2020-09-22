#DESAFIO0109 Modifique as funções que foram ciradas no desafio107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio108.
import moeda_new

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda_new.moeda(p)} é {moeda_new.metade(p, True)}')
print(f'O dobro de {moeda_new.moeda(p)} é {moeda_new.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda_new.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda_new.diminuir(p, 13,  True)}')
