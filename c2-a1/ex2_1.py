import getpass

def validar_senha(senha: str, usuario: str) -> list[str]:
    erros: list[str] = []
    especiais = set("!@#$%^&*?")

    if senha == usuario:
        erros.append('Erro: A senha não pode ser igual ao usuario')

    if len(senha) <= 8:
        erros.append('Erro: A senha precisa de pelo menos 8 caracteres')

    if not any(c.isalpha() for c in senha):
        erros.append('Erro: A senha precisa de pelo menos uma letra (A-Z ou a-z)')

    if not any(c.isdigit() for c in senha):
        erros.append('Erro: A senha precisa de pelo menos um numero')

    if not any(c in especiais for c in senha):
        erros.append('Erro: A senha precisa de pelo menos um caracter especial (!@#$%^&*?)')

    return erros

def ex2_1():
    usuario = input('digite o seu usuario: ')

    senha = getpass.getpass(prompt='\n digite a sua senha: ')

    erros = validar_senha(senha, usuario)

    while erros:
        print("Senha invalida")
        for e in erros:
            print(e)
        print()
        nova_senha = getpass.getpass(prompt='Tente novamente: ')
        erros = validar_senha(nova_senha, usuario)

    print(f'Bem vindo {usuario}!')

ex2_1()
