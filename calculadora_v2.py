#Controle
saida = ""

#Operações Básicas
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        print('Não foi possível realizar a divisão por 0')
    else:
        return a / b

#Função Calculadora    
def calculadora(num1, num2, operacao):
    operacao = operacao.lower()
    resultado = None

    if operacao in ['+', 'adicao', 'adição', 'soma']:
        resultado = adicao(num1, num2)
    elif operacao in ['-', 'subtracao', 'subtração', 'menos']:
        resultado = subtracao(num1, num2)
    elif operacao in ['*', 'multiplicacao', 'multiplicação', 'x', 'vezes']:
        resultado = multiplicacao(num1, num2)
    elif operacao in ['/', 'divisao', 'divisão']:
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida'

    return resultado

#Laço Repetição
while saida.lower() != 'n':
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segunto número: '))
        operacao = input('Digite a operação desejada (+, -, *, / ou nome): ')

        resultado = calculadora(num1, num2, operacao)
        print(f'Resultado da operação: {resultado}')
    except ValueError:
        print('Entrada inválida! Por favor, digite apenas números')

    saida = input("Deseja continuar? (S/N): ")