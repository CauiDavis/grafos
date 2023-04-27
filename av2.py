import numpy as np

def encontra_saida(labirinto, linha_atual, coluna_atual):
    # Define as direções possíveis (cima, baixo, esquerda, direita)
    direcoes = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    # Define a posição atual como visitada
    labirinto[linha_atual][coluna_atual] = 2

    # Percorre as direções possíveis a partir da posição atual
    for direcao in direcoes:
        nova_linha = linha_atual + direcao[0]
        nova_coluna = coluna_atual + direcao[1]
        
        # Verifica se a nova posição está dentro do labirinto
        if nova_linha < 0 or nova_linha >= len(labirinto) or nova_coluna < 0 or nova_coluna >= len(labirinto[0]):
            continue
        
        # Verifica se a nova posição é uma saída
        if labirinto[nova_linha][nova_coluna] == 3:
            print(np.matrix(labirinto))
            return True
        
        # Verifica se a nova posição é um caminho válido
        if labirinto[nova_linha][nova_coluna] == 1:
            if encontra_saida(labirinto, nova_linha, nova_coluna):
                return labirinto
   
    return False

labirinto = [
        [0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1],
        [0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 3]
    ]
possivel = encontra_saida(labirinto, 1, 0)
if( possivel == False):
    print("Não há saída")
else:
    print("existe saida")

