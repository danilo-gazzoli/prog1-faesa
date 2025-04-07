from mensagens import *

def cadastrar_candidatos():
    num_candidatos = int(input(cadastro_candidatos))

    # Dicionario para armazenar candidatos
    candidatos = {}

    # Dicionario para armazenar votos
    votos = {}

    print("Agora digite, nessa sequencia, o nome do candidato e em seguida o numero dele")

    for num in range(1, num_candidatos + 1):
        nome = input(f"\n Digite o nome do {num}º candidato: ")
        numero = int(input(f"\n Digite o numero do {num}º candidato: "))

        candidatos[numero] = nome
        votos[numero] = 0

    # Inicializando contagem de votos nulos e brancos
    votos["nulos"] = 0
    votos["brancos"] = 0

    return votos, candidatos

def exibir_resultado(votos, candidatos, total_votos):
    print("\n Resultado da eleição:")

    for numero, nome in candidatos.items():
        porcentagem = (votos[numero] / total_votos) * 100 if total_votos > 0 else 0
        print(f"{nome} (Número {numero}): {votos[numero]} votos ({porcentagem:.2f}%)")

    # Exibindo votos nulos e brancos
    total_nulos = votos["nulos"]
    total_brancos = votos["brancos"]

    porcentagem_nulos = (total_nulos / total_votos) * 100 if total_votos > 0 else 0
    porcentagem_brancos = (total_brancos / total_votos) * 100 if total_votos > 0 else 0

    print(f"\n Votos Nulos: {total_nulos} votos ({porcentagem_nulos:.2f}%)")
    print(f"Votos Brancos: {total_brancos} votos ({porcentagem_brancos:.2f}%)")

def iniciar_votacao(votos, candidatos):
    # Iniciando a votacao
    inicio = int(input("\nOs candidatos foram cadastrados com sucesso. \n Pressione 1 para iniciar a votacao ou 0 para sair: "))

    if inicio == 0:
        print(sair)
        exit()

    # Variavel para controlar o loop da eleicao
    eleicao = True
    total_votos = 0

    # Loop para registrar votos
    while eleicao:
        voto = input(explicar_votos)

        # Condicoes para tratar os votos
        if voto == "fim":
            eleicao = False
            break
        elif voto == "branco":
            votos["brancos"] += 1
        elif voto.isdigit() and int(voto) in candidatos:
            votos[int(voto)] += 1
        elif voto != "fim" and voto != "branco":
            votos["nulos"] += 1

        total_votos += 1

    return total_votos
