'''
DESAFIO0105 Faça um programa que tenha uma função notas() que pode receber várias notas de aluno e vai retornar um dicionário com as seguintes informações:
- Quantida de notas
- A maior nota
- A menor nota
- A média da turma
- A situação(opcional)
Adicione também as docstrings da função.'''

def notas(*num, sit=False):
    """
    -> Função para analisar nota e situação de vários alunos
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indica se deve ou não mostrar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    info = dict()
    soma = maior = menor = 0
    for n in range(0, len(num)):
        if n == 0:
            maior = menor = num[n]
        else:
            if maior < num[n]:
                maior = num[n]
            if menor > num[n]:
                menor = num[n]
        soma += num[n]

    info['Quantidade'] = len(num)
    info['Maior'] = maior
    info['Menor'] = menor
    info['Média'] = soma/len(num)
    if sit:
        if info['Média'] >= 7:
            info['Situação'] = 'BOA'
        if 5 <= info['Média'] < 7:
            info['Situação'] = 'RAZÓAVEL'
        if info['Média'] < 5:
            info['Situação'] = 'RUIM'
        if info['Média'] < 3:
            info['Situação'] = 'PÉSSIMA'
    return info


resp = notas(2, 5, 7, sit=True)
print(resp)
