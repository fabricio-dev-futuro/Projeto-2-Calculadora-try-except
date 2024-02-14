'***************** Calculadora Python com try/except *****************'

# Forma de inserir dados e corrigir possivel erro de digitação diferente de número
try:
    num1 = int(input('Digite um número: '))
except:
    print('Você não digitou um número.')

try:
    num2 = int(input('Digite outro número: '))
except:
    print('Você não digitou um número.')

operador = input('Insira o operador (+ , - , * , /): ')

# Lógica para erro de digitação no operador
if operador != '+':
    if operador != '-':
        if operador != '*':
            if operador != '/':
                print('Tente um operador válido.') 

# Corrigindo uma possivel divisão por zero                   
try:
    if num2 == 0 and operador == '/':
        print('Não é permitido divisão por zero!\nPor favor, mude o valor do 2º número.')
# Lógica da calculadora 
    else:
        if operador == '+':
            resultado = num1 + num2
            print('O resultado é: ', resultado)
        elif operador == '-':
            resultado = num1 - num2
            print('O resultado é: ', resultado)

        elif operador == '*':
            resultado = num1 * num2
            print('O resultado é: ', resultado)

        elif operador == '/':
            resultado = num1 / num2
            print('O resultado é: ', resultado)

# Mensagem de erro caso o usuário digite letras ao invés de números no input 1 e 2
except NameError:
    print('Você digitou algum caracter não permitido em alguma fase do processo!\nSó são permitidos numeros e o operador matemático no passo 3.')


    

