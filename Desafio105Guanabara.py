def notas(*n, sit=False):
    """
        -> Função para analisar nota e situação de vários alunos
        :param num: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indica se deve ou não mostrar a situação
        :return: dicionário com várias informações sobre a situação da turma
        """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        if 5 <= r['média'] < 7:
            r['situação'] = 'RAZÓAVEL'
        if r['média'] < 5:
            r['situação'] = 'RUIM'
        if r['média'] < 3:
            r['Situação'] = 'PÉSSIMA'
    return r


# Programa Principal
resp = notas(5.5, 2.5, 8.5)
print(resp)