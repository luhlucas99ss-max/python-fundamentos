def ajuda(com):
    help(com)

def titulo(msg,cor=0):
    tam = len(msg) + 4
    print('='*tam)
    print(f'  {msg}')
    print('='*tam)


comando = ''
while True:
    titulo('Sistema de ajuda PYHelp')
    comando = input('Função ou biblioteca => ').strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('Até logo!')