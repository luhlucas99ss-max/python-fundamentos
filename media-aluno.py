
aluno = dict()
aluno['nome'] = str(input('Nome: '))

while True:
    try:
        aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
        if not 0 <= aluno['media'] <= 10:
            print('Digite um valor entre 0 e 10.')
        else:
            break
    except ValueError:
        print('Erro! Digite um numero valido para media.')

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

for k , v in aluno.items():
    print(f'{k} é igual a {v}')