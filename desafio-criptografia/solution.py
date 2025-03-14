class Solution:
    def __init__(self):
        self.contagem = {}

    # função principal responsável para descriptografar a mensagem
    def descriptografar(self, criptografia):
        contar_char_mensagem(criptografia)

        
    # conta quantas vezes cada caracter aparece na mensagem criptografada e retorna um hashmap
    def contar_char_mensagem(self, criptografia):
        total = 0

        # contagem de caracteres
        for char in criptografia:
            if char not in '.- ':
                total += 1
                self.contagem[char] = self.contagem.get(char, 0) + 1

        # Depois, calcula a frequência relativa de cada caractere
        self.contagem = {char: (count / total) * 100 for char, count in self.contagem.items()}

        self.ordenagem_decrescente(self.contagem)

        # retorna a contagem ordenada
        return self.contagem

    # ordena o dicionario em ordem ordenagem 
    def ordenagem_decrescente(self, dicionario):
        self.contagem = dict(sorted(
            dicionario.items(),
            key=lambda item: item[1],
            reverse = True
        ))
