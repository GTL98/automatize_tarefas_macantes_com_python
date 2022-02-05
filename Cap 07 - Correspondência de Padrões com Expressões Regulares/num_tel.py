def numero_telefone(texto):
    if len(texto) != 12:
        return False

    for i in range(0, 3):
        if not texto[i].isdecimal():
            return False

    if texto[3] != '-':
        return False

    for i in range(4, 7):
        if not texto[i].isdecimal():
            return False

    if texto[7] != '-':
        return False

    for i in range(8, 12):
        if not texto[i].isdecimal():
            return False

    return True

print('415-555-4242 é um número de telefone:')
print(numero_telefone('415-555-4242'))
print('Olá olá é um número de telefone:')
print(numero_telefone('Olá olá'))

print('\n')

mensagem = 'Me ligue no 415-555-1011 amanhã. 415-555-9999 é meu escritório.'
for i in range(len(mensagem)):
    pedaco = mensagem[i:i+12]
    if numero_telefone(pedaco):
        print(f'Número de telefone encontrado: {pedaco}')
print('Fim')
