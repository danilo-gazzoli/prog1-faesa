from metodos import *
from mensagens import *

resposta = int(input(explicacao_eleicao))

if resposta == 0:
    print(sair)
    exit()

votos, candidatos = cadastrar_candidatos()

# Chama a funcao para iniciar a votacao
total_votos = iniciar_votacao(votos, candidatos)

# Chama a funcao para exibir o resultado
exibir_resultado(votos, candidatos, total_votos)
