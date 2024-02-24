def calculadora(numero1, numero2, operador):

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

    
while True:    
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    operador = str(input('Digite o operador: '))
    print(calculadora(numero1, numero2, operador))

    opcao = str(input('Digite "s" para continuar ou qualquer tecla para sair: '))
    if opcao == 's':
        continue
    else:
        break


