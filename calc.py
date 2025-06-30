print('''
                 _                  _               _                        
   ___    __ _  | |   ___   _   _  | |   __ _    __| |   ___    _ __    __ _ 
  / __|  / _` | | |  / __| | | | | | |  / _` |  / _` |  / _ \  | '__|  / _` |
 | (__  | (_| | | | | (__  | |_| | | | | (_| | | (_| | | (_) | | |    | (_| |
  \___|  \__,_| |_|  \___|  \__,_| |_|  \__,_|  \__,_|  \___/  |_|     \__,_|
      
Bem vindo a Calculadora Python!
Digite 'sair' para encerrar o programa.
Digite a operação que deseja realizar:
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Potenciação
6. Raiz Quadrada
7. Fatorial
      
      ''')

operation = int(input('Escolha uma operação de (1-7): '))

if operation == 1:
    number1= int(input('Digite o primeiro número: '))
    number2 = int(input('Digite o segundo número: '))
    result = (number1 + number2)
    print(f'O resultado da adição é: {result}')
    print("obrigado por usar a calculadora Python!")
elif operation == 2:
    number1= int(input('Digite o primeiro número: '))
    number2 = int(input('Digite o segundo número: '))
    result = (number1 - number2)
    print(f'O resultado da subtração é: {result}')
    print("obrigado por usar a calculadora Python!")
elif operation == 3:
    number1= int(input('Digite o primeiro número: '))
    number2 = int(input('Digite o segundo número: '))
    result = (number1 * number2)
    print(f'O resultado da multiplicação é: {result}')
    print("obrigado por usar a calculadora Python!")
elif operation == 4:
    number1= int(input('Digite o primeiro número: '))
    number2 = int(input('Digite o segundo número: '))
    if number2 ==0:
        print('Divisão por zero não é permitida.')
    else:
        result = (number1 / number2)
        print(f'O resultado da divisão é: {result}')
        print("obrigado por usar a calculadora Python!")
elif operation == 5:
    number1= int(input('Digite o primeiro número: '))
    number2 = int(input('Digite o segundo número: '))
    result = (number1 ** number2)
    print(f'O resultado da potenciação é: {result}')
    print("obrigado por usar a calculadora Python!")
elif operation == 6:
    number1 = int(input('Digite o número para calcular a raiz quadrada: '))
    if number1 < 0:
        print('Raiz quadrada de número negativo não é permitida.')
    else:
        result = (number1 ** 0.5)
        print(f'O resultado da raiz quadrada é: {result}')
        print("obrigado por usar a calculadora Python!")
elif operation == 7:
    number1= int(input('Digite o número para calcular o fatorial: '))
    if number1 < 0:
        print('Fatorial de número negativo não é permitido.')
        print("obrigado por usar a calculadora Python!")
        
    else:
            num_para_fatorial = int(number1) 
            result = 1 
            for i in range(1, num_para_fatorial + 1):
                result *= i
            print(f'O resultado do fatorial é: {result}')
else:
    print('Operação inválida. Por favor, escolha uma operação válida.')
