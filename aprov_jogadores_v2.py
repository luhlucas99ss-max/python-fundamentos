## variaveis 
time = []
jogador = {}

print('    >>>> BRASILEIRÃO <<<<')
while True:
    jogador.clear()
    jogador['nome'] = input('Informe o Nome do Jogador: ').strip()

    try:
        tot = int(input(f'Informe quantas partidas o {jogador["nome"]} jogou: '))
        if tot < 0 or tot > 38:
            print('Digite um numero acima de 0 ou abaixo de 38.')
    except ValueError:
        print('Apenas numeros neste campo. ')

    gols = []
    for cont in range(0, tot):
        while True:
            try:
                gol = int(input(f'Quantos gols o {jogador["nome"]} fez na partida {cont+1}: '))
                if gol < 0 or gol > 10:
                    print('Informe uma quantidade real de gols. ')
                else:
                    gols.append(gol)
                    break
            except ValueError:
                print('Apenas numeros nesse campo. ')
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())

    resp = None
    while resp not in ('S', 'N'):
        try:
            resp = input('Deseja continuar cadastrando os jogadores: [S]im ou [N]ão ').strip().upper()[0]
            if resp not in ('S', 'N'):
                print('Escolha entre [S] ou [N]')
        except IndexError:
            print('Apenas letras neste campo. ')

    if resp == 'N':
        break
print('==='*20)
print('cod', end='')
for elemento in jogador.keys():
    print(f'{elemento:<15}', end='')
print()
 
print('==='*20)
for cont, valor in enumerate(time):
    print(f'{cont:>3} ', end ='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print()
print('==='*20)
resp = None
while resp not in ('S', 'N'):
    try:
        resp = input('Deseja mostrar od dados dos jogadores: [S]im ou [N]ão ').strip().upper()[0]
        if resp not in ('S', 'N'):
            print('Escolha entre [S] ou [N]')
    except IndexError:
        print('Apenas letras neste campo. ')

if resp == 'S':
    while True:
        buscar = int(input('Mostrar os dados de qual jogador: '))
        if buscar >= len(time) or buscar < 0:
            print('Error! Jogador inesistente.')
        else:
            print(f'---- LEVANTAMENTO DO JOGADOR {time[buscar]["nome"]}')
            for indice, quantidade in enumerate(time[buscar]["gols"]):
                print(f'    no jogo {indice+1} fez {quantidade} gols')
        print('==='*20)

        continuar = None
        while continuar not in ('S', 'N'):
                try:
                    continuar = input('Mostrar os dados de qual jogador: ')
                    if continuar not in ('S', 'N'):
                        print('Escolha entre [S] ou [N]')
                except IndexError:
                    print('Apenas letras neste campo. ')
        if continuar == 'N':
            break
        
print('>>> Encerado <<<')


