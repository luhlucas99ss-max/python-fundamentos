# Variavel Primaria.
listatot = list()
# Variavel do exercicio.
pessoa = {}
soma = media = 0

while True:

    pessoa.clear()
    pessoa['nome'] = input('Informe o nome: ').strip()

    while True:### Recebimento e Validação ['sexo']
        try:
            pessoa['sexo'] = input('Informe se o sexo é [M]asculino ou [F]eminino: ').strip().upper()[0]
            if pessoa['sexo'] not in ('M', 'F'):
                print('Escolha entre Masculino e Feminino. ')
            else:
                break
        except IndexError:
            print('Informe uma das letras.')
            
    while True:### Recebimento e validação ['idade']
        try:
            pessoa['idade'] = int(input(f'Informe a idade do {pessoa["nome"]} por favor: '))
            if pessoa['idade'] < 0 or pessoa['idade'] > 105:
                print('Infome uma idade maior que 0 ou menor que 105.')
            else:
                break
        except ValueError:
            print('Apenas Numeros nesse campo.')
    soma += pessoa['idade']

    ### Tranferindo o dicionario para lista 
    listatot.append(pessoa.copy())

    resp = None 
    while resp not in ('S' , 'N'):### Validação da continuação do cadastro. 
        try:
            resp = input('Deseja continuar cadastrando: [S]im ou [N]ão ').strip().upper()
            if resp not in ('S' ,'N' ):
                print('Escolha entre [S]im ou [N]ão.')
            else:
                break
        except IndexError:
            print('Apenas letras nesse campo.')
    if resp == 'N':
        break
print('XxX'*20)

print(f'Foram cadastradas um total de {len(listatot)} pessoas. ')
media = soma /len(listatot)
print('XxX'*20)

print(f'A media de idade das pessoas cadastradas é {media}')
print('XxX'*20)

for mulher in listatot:
    if mulher['sexo'] == 'F':
        print(f'\n {mulher["nome"]} ', end='')
print('XxX'*20)

for maior in listatot:
    if maior['idade'] >= media:
        for cont, valor in maior.items():
            print(f'{cont} = {valor}', end='')
        print()

print('>>>> Encerrado<<<<')