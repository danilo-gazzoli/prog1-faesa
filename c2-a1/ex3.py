def ex3():
    start = input("""
        Vamos começar cadastrando os clientes. Primeiro informe o numero da matricula, depois altura em metros (m) e a peso em 'kg'. 
        \n * Pressione 1 para iniciar cadastro 
        \n * Pressione 0 para encerrar o cadastro
        """).strip()

    if start != '1':
        print('Cadastro nao iniciado')
        return

    clientes: dict[str, dict[str, float]] = {}

    codigo = input('Digite o codigo cliente (ou 0 para sair): ').strip()

    while codigo != '0':

        # valida codigo
        if not codigo.isdigit():
            print('Código inválido! Digite apenas numeros')
            codigo = input('Código do cliente (ou 0 para sair): ').strip
            continue
        
        # le e valida altura
        try:
            altura = float(input(f'\n Altura (em metro) do cliente #{codigo}: ').strip())

            while altura >= 2.5 or altura <= 0:
                altura = float(input('Esse valor parece irreal. Digite novamente: ').strip())

        except ValueError:
            print('Altura inválida! Confira se os valores são numéricos.\n')
            continue

        # le e valida peso
        try:
            peso = float(input(f'\n Peso (em kg) do cliente #{codigo}: ').strip())

            while peso >= 250 or peso <= 0:
                peso = float(input('Esse valor parece irreal. Digite novamente: ').strip())
        
        except ValueError:
            print('Peso inválido! Confira se os valores são numéricos.\n')
            continue

        # armazena os dados
        clientes[codigo] = {'altura': altura, 'peso': peso}

        codigo = input('\nDigite o codigo do cliente ou 0 para sair: ').strip()

    if not clientes:
        return print('\nNenhum cliente foi cadastrado')

    # calculo de media
    alturas = [d["altura"] for d in clientes.values()]
    pesos = [d["peso"] for d in clientes.values()]
    media_altura = sum(alturas) / len(alturas)
    media_peso = sum(pesos) / len(pesos)

    # verifica os maiores valores
    codigo_mais_alto, dados_mais_alto = max(clientes.items(), key=lambda key_value: key_value[1]["altura"])
    codigo_mais_baixo, dados_mais_baixo = min(clientes.items(), key=lambda key_value: key_value[1]["altura"])
    codigo_mais_pesado, dados_mais_pesado = max(clientes.items(), key=lambda key_value: key_value[1]["peso"])
    codigo_mais_leve, dados_mais_leve = min(clientes.items(), key=lambda key_value: key_value[1]["peso"])
    
    # imprimindo resultados
    print(f'\nMedia de altura: {media_altura:.2f} m')
    print(f'\nMedia de peso: {media_peso:.2f} kg')

    print(f"\nMais alto → código: {codigo_mais_alto}, altura: {dados_mais_alto['altura']:.2f} m")
    print(f"\nMais baixo → código: {codigo_mais_baixo}, altura: {dados_mais_baixo['altura']:.2f} m")
    print(f"\nMais pesado → código: {codigo_mais_pesado}, peso: {dados_mais_pesado['peso']:.2f} kg")
    print(f"\nMais magro → código: {codigo_mais_leve}, peso: {dados_mais_leve['peso']:.2f} kg")
ex3()
