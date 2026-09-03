#Varivel principal
apjog = dict()
gols = []
partidas = 0
while True: 
###---------- Leitura do Nome ----------###
    apjog['nome'] = input('Informe o NOME do jogador: ').strip()
###---------- Leitura das Partidas ----------###
    try:
        partidas = int(input(f'Quantas partidas o jogador {apjog["nome"]} foram jogadas: '))
        if partidas < 0:
            print('Erro! informe uma quantidades de partidas jogadas.')
        else:
            break
    except ValueError:
        print('Erro! informe um numero neste campo.')
###---------- Leitura da quantidade de gols ----------###
for cont in range(0, partidas):
    while True:      
        try:
            gol = int(input(f'    Quandots gols o jogador {apjog["nome"]} fez na partida {cont +1}ª: '))
            if gol < 0:
                print('Erro! Informe um numero valido.')
            else:
                gols.append(gol)
                break
        except ValueError:
            print('Erro! Informe um numero.')
    apjog['gol'] = gols[:]
    totalgols = sum(gols)
    apjog['totalgols'] = totalgols
    apjog['partidas'] = partidas
print('      --- Resultados Simples --- ')
print(f' O jogador {apjog['nome']} fez um total de {totalgols} durante {partidas}.') 

print('      --- Resultados Dicionario --- ')
print(apjog)

print('      --- Resultados 3 tipo de demonstrar --- ')
for k, v in apjog.items():
    print(f'O Campo {k} tem o valor {v}')

print('      --- Resultados 4 tipo de demonstrar --- ')
print(f'o jogador {apjog["nome"]} jogou {len(apjog["gol"])} partidas.')
for indice, valor in enumerate(apjog['gol']):
    print(f'    => na partida {indice}, fez {valor} gols')
print(f'Foi um total de {apjog["totalgols"]} gols')