def ex1():
    nota = float(input('Digite uma nota entre 0 e 10: '))

    while nota > 10 or nota < 0:
        nota = float(input('Erro: A nota não pode ser maior que dez (10) e nem menor que zero (0) \n Digite novamente: '))
    
    print(f'A sua nota é {nota}')

ex1()
