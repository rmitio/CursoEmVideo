'''DESAFIO087 Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O Maior valor da segunda linha'''

matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
somapares = terceira = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
        if c == 2:
            terceira += matriz[l][c]
        if l == 1:
            if maior < matriz[l][c]:
                maior = matriz[l][c]


for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é {somapares}')
print(f'A soma dos valores da terceira coluca é {terceira}')
print(f'O maior valor da segunda linha é {maior}')