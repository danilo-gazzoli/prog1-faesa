def ex4():
    start = input("""
        Vamos começar cadastrando os alunos. Primeiro informe o nome e depois a nota. 
        \n * Pressione 1 para iniciar cadastro 
        \n * Pressione 0 para encerrar o cadastro
        """).strip()

    if start != '1':
        print('Cadastro nao iniciado')
        return

    alunos = {}
    
    nome = input('Digite o nome do aluno ou 0 para sair: ').strip()

    while nome != '0':

        try:
            nota = float(input(f'\n Nota de {nome}: '))
        except ValueError:
            print('Nota inválida! Digite um numero (Ex: 9.35) \n')
            continue

        alunos[nome] = nota

        nome = input('Digite o nome do aluno ou 0 para sair: ').strip()

    if not alunos:
        return print('\n Nenhum aluno foi cadastrado')

    media = sum(alunos.values()) / len(alunos)
    
    print(f'A media da turma foi: {media:.2f}')

ex4()
