
#Calculadora (+, -, *, /)

def soma (N1, N2):
    print(f"{N1} + {N1} = {N1 + N2} ")

def subtracao (N1, N2):
    print(f"{N1} - {N1} = {N1 - N2} ")

def multiplicacao (N1, N2):
    print(f"{N1} * {N1} = {N1 * N2} ")

def divisao (N1, N2):
    print(f"{N1} / {N1} = {N1 / N2} ")


O = 0
while O != 'fim':

    O = str(input('Escolha a operação: +, -, *, / ou fim: '))
    if O == 'fim':
        break

    N1 = int(input('Digite um numero: '))
    N2 = int(input('Digite outro numero: '))

    if O == '+':
        soma(N1, N2)

    elif O == '-':
        subtracao(N1,N2)

    elif O == '*':
        multiplicacao(N1, N2)

    elif O == '/':
        divisao(N1, N2)

    else:
        print('Digito invalido, tente novamente: ')



