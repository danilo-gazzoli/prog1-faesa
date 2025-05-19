import getpass

def ex2():
    usuario = input('digite o seu usuario: ')

    senha = getpass.getpass(prompt='\n digite a sua senha: ')

    while usuario == senha:
        senha = getpass.getpass(prompt='Erro: A senha não pode ser igual ao usuario. \n Digite novamente: ')

    print(f'Bem vindo {usuario}!')

ex2()
