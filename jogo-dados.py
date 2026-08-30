
from random import randint
from time import sleep
from operator import itemgetter

jogador = {'jogador 1': randint(1,6),
           'jogador 2': randint(1,6),
           'jogador 3': randint(1,6),
           'jogador 4': randint(1,6)}

print('Valores sorteados....')

for k, v in jogador.items():
    print(f'{k} tirou o valor {v} dado')
    sleep(1)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print('=-='*30)
print('  XxX RANKING DOS JOGADORES XxX')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)