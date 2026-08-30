
from datetime import datetime
pessoa = {}
### ---------- Comecei calculando o ano atual ---------- ###
ano_atual = datetime.now().year
### ---------- Primeiro loop para nomes e anos ---------- ###
while True:

        pessoa['nome'] = input('Digite o nome: ').strip()

        try:
                pessoa['ano'] = int(input('Informe o ano de nascimento: '))
                if pessoa['ano'] <= 0 or pessoa['ano'] > ano_atual:
                        print('Erro! Informe um numero valido.')
                else:
                    break
        except ValueError:
                print('Erro! Apenas numeros neste campo.')

pessoa['idade'] = ano_atual - pessoa['ano']

### ---------- Perguntando se a pessoa tem carteira de trabalho ---------- ###
resp = None
while resp not in ('S', 'N'):
    resp = input('A pessoa possui carteira de Trabalho(CTPS)? [S]im ou [N]ão ').strip().upper()
    if resp not in ('S','N'):
        print('Escolha entre [S]im ou [N]ão')

if resp == 'N':
    pessoa['carteira'] = 0
        
elif resp == 'S':
### ---------- Loop da carteira, contratação e salario ---------- ###          
    while True:
        try:
            pessoa['carteira'] = int(input('Informe o numero da carteira de trabalho(CTPS): '))
            if pessoa['carteira'] < 0:
                print('Erro! Informe um numero valido.')
            else:
                break
        except ValueError:
                print('Erro! Apenas numeros neste campo.')

    if pessoa['carteira'] != 0:
        while True:
            try:
                pessoa['contratacao'] = int(input('Informe o ano de contratação: '))
                if pessoa['contratacao'] <=0:
                    print('Erro! Informe um ano valido.')
                else:
                    break
            except ValueError:
                print('Erro! Apenas numeros neste campo.')
        while True:
            try:
                pessoa['salario'] = float(input('Informe o salario: '))
                if pessoa['salario'] <=0:
                    print('Erro! Informe um salario valido.')
                else:
                    break
            except ValueError:
                print('Erro! Apenas numeros neste campo.')

### ---------- calculo do tempo restante para a aposentadoria legislação brasileira define um minimo de 35 anos ---------- ###
    tempo_contribu = 35 - (ano_atual - pessoa['contratacao'])
    if tempo_contribu < 0:
        pessoa['aposentadoria'] = pessoa['idade'] # Ja se aposenta.
    else:
        pessoa['aposentadoria'] = pessoa['idade'] + tempo_contribu
print('\n --- Dados cadastrados --- ')
### ---------- mostranto o resultado ---------- ###
for k, v in pessoa.items():
     if k == 'salario':
          print(f'{k.title()}: R$ {v:.2f}')
     else:
        print(f'{k.title()}: {v}')
