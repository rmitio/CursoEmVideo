#DESAFIO024 Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cid = input('Digite um cidade: ').strip()
print(cid[:5].upper() == 'Santo')

'''if cid[:5].strip().upper() == "SANTO":
    print('A cidade começa com santo')
else:
    print('A cidade não começa com Santo!')
'''
