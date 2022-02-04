'''
Meu primeiro código - Tabuada 1.0 
Inicio 03/05/2021
Finalizado 12/05/2021
'''
print('*' * 60)
print('*********** MINHA PRIMEIRA TABUADA - PYTHON 1.0. ***********')
print('*' * 60)

from time import sleep
opção = 0
#calculo
while opção != 5:
    #Escolha do tipo de operação
    print('\nInsira o número do operador:') 
    print (''' \n(1) Soma. (2) Subtração. (3) Multiplicação. (4) Divisão. (5) Sair\n ''')
  
    opção = int(input('Opção: '))
    #Escolha do valor a ser calculado
    n1 = int(input('\nInsira o número a ser calculado: '))
    n2 = 0
    #opção de operação    
    if opção == 1:
        print(f'Tabuada de {n1} : Soma.')
        for calcular in range(1, 11):
            n2 += 1
            resultado = n1 + n2
            print ('{} + {} = {}'.format(n1, n2, resultado))
    elif opção == 2:
        print(f'Tabuada de {n1} : Subtração.')
        for calcular in range(1, 11): 
            n2 += 1
            resultado = n1 - n2
            print ('{} - {} = {}'.format(n1, n2, resultado))
    elif opção == 3:
        print(f'Tabuada de {n1} : Mutiplicação.')
        for calcular in range(1, 11):
            n2 += 1
            resultado = n1 * n2
            print ('{} x {} = {}'.format(n1, n2, resultado)) 
    elif opção == 4:
        print(f'Tabuada de {n1} : Divisão.')
        for calcular in range(1, 11):
            n2 += 1
            resultado = n1 / n2
            resultado = ('{:.2f}'.format(resultado))
            print ('{} / {} = {}'.format(n1, n2, resultado))            
    elif opção == 5:
        print('Finalizando programa...') 
    else:
        print('Opção inválida! Tente novamente.')
    print('--' * 10)    
    sleep(2)
print("Fim do pragrama!")
