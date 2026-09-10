def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um Numero...')
        if ok:
            break
    return valor

# Programa principal
n = leiaint('Digite um numero: ')
print(f'Voce acabou de digita o numero {n}')