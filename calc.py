print("====================================================")
print("=================  Bemvindo a Calc  =================")
print("=====================================================")
print("                                                         ")
print("                                                         ")




#variavel para escolher a operação usando input para que o ususario consiga mandar sua resposta para que tenha um retorno
# as 3 ''' significa que vc pode usar strings em multiplas linhas 
operation= input('''
Oque você quer calcular?
                      
+ para adição   
- para subtração    
* para multiplicação
/ para divisão
''')

#duas variaveis com o valor int(input) para reconhecer que é um numero inteiro,
# assim vc digita um string e depois reocnhece como um número na frente da string usando dois parênteses
number_1 = int(input('Digite o primeiro numero: '))
print("                                                ")
number_2 = int(input('Digite o segundo numero: '))

# Addition - nome das operações matemáticas cada uma 
if operation == '+':
    print("                                                         ")
    print("                                                         ")
    print("                 CALCULANDO.............                 ")
    print("                                                         ")
    print("                                                         ")
    # formatações de strings nelas vc usa os colchetes {} para tranferir oque quer colocar
    #usando o (.format) nele vc consegue colocar valores como strings ou números
    print('{} + {} = '.format(number_1, number_2))
    #depois que vc da o comando input vc precisa realizar a operação para que apareça no terminal
    #usando o print(e a operação matematica sendo feita)
    print(number_1 + number_2)
    print("                                                         ")
    print("obrigado por usar nossa {}".format("CALCULADORA KABUM"))

# Subtraction
elif operation == '-':
    print("                                                         ")
    print("                                                         ")
    print("                 CALCULANDO.............                 ")
    print("                                                         ")
    print("                                                         ")
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)
    print("                                                         ")
    print("obrigado por usar nossa {}".format("CALCULADORA KABUM"))

# Multiplication
elif operation == '*':
    print("                                                         ")
    print("                                                         ")
    print("                 CALCULANDO.............                 ")
    print("                                                         ")
    print("                                                         ")
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)
    print("                                                         ")

    print("obrigado por usar nossa {}".format("CALCULADORA KABUM"))

# Division
elif operation == '/':
    print("                                                         ")
    print("                                                         ")
    print("                 CALCULANDO.............                 ")
    print("                                                         ")
    print("                                                         ")
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
    print("                                                         ")
    print("obrigado por usar nossa {}".format("CALCULADORA KABUM"))
    
    
    


