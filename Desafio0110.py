#DESAFIO0110 Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações gerada pela funções que já temos no módulo criado até aqui.

import moeda_new

p = float(int(input('Digite o preço: R$ ')))
moeda_new.resumo(p, 80, 35)
