def calculatora(numero1, numero2, operador):
    if operador == '+':
        return numero1 + numero2
    elif operador == '-':
        return numero1 - numero2
    elif operador == '*':
        return numero1 * numero2
    elif operador == '/':
        return numero1 / numero2
    else:
        return 'Operador inválido'

print(calculatora(2, 3, '+'))
