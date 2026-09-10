def voto(ano):
    from datetime import date
    '''
        ano: Recebe de fora o ano indicado pelo usuario
        Aqui é feita a logica da idade, que mostra a situação do voto
    '''
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'A pessoa tem {idade} o voto é NEGADO'
    elif idade > 18 or idade < 65:
        return f'A pessoa tem {idade} o voto é OBRIGATORIO'
    elif idade > 65:
        return f' A pessoa tem {idade} o voto é OPCIONAL'
    
nasc = int(input('Informe o ano de nascimento: '))
print(voto(nasc))


