#DESAFIO0114 Crie um código em Python que testa se o site Pudim está acessível pelo computador usado.
import urllib.request

try:
    urllib.request.urlopen("http://www.pudim.com.br").getcode()
    print('Funcionado!')
except:
    print('Nâo Disponivel')