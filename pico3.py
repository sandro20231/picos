import sys

matriz = [
    [10, 12, 15, 20, 28, 38, 50, 65, 83, 105,
        130, 105, 83, 65, 50, 38, 28, 20, 15, 12],
    [12, 15, 20, 28, 38, 50, 65, 83, 105, 130,
        160, 130, 105, 83, 65, 50, 38, 28, 20, 15],
    [15, 20, 28, 38, 50, 65, 83, 105, 130, 160,
        195, 160, 130, 105, 83, 65, 50, 38, 28, 20],
    [20, 28, 38, 50, 65, 83, 105, 130, 160, 195,
        235, 195, 160, 130, 105, 83, 65, 50, 38, 28],
    [28, 38, 50, 65, 83, 105, 130, 160, 195, 235,
        280, 235, 195, 160, 130, 105, 83, 65, 50, 38],
    [38, 50, 65, 83, 105, 130, 160, 195, 235, 280,
        330, 280, 235, 195, 160, 130, 105, 83, 65, 50],
    [50, 65, 83, 105, 130, 160, 195, 235, 280, 330,
        385, 330, 280, 235, 195, 160, 130, 105, 83, 65],
    [65, 83, 105, 130, 160, 195, 235, 280, 330, 385,
        445, 385, 330, 280, 235, 195, 160, 130, 105, 83],
    [83, 105, 130, 160, 195, 235, 280, 330, 385, 445,
        510, 445, 385, 330, 280, 235, 195, 160, 130, 105],
    [105, 130, 160, 195, 235, 280, 330, 385, 445, 510,
        1000, 510, 445, 385, 330, 280, 235, 195, 160, 130],
    [130, 160, 195, 235, 280, 330, 385, 445, 510, 1000,
        1000, 1000, 510, 445, 385, 330, 280, 235, 195, 160],
    [105, 130, 160, 195, 235, 280, 330, 385, 445, 510,
        1000, 510, 445, 385, 330, 280, 235, 195, 160, 130],
    [83, 105, 130, 160, 195, 235, 280, 330, 385, 445,
        510, 445, 385, 330, 280, 235, 195, 160, 130, 105],
    [65, 83, 105, 130, 160, 195, 235, 280, 330, 385,
        445, 385, 330, 280, 235, 195, 160, 130, 105, 83],
    [50, 65, 83, 105, 130, 160, 195, 235, 280, 330,
        385, 330, 280, 235, 195, 160, 130, 105, 83, 65],
    [38, 50, 65, 83, 105, 130, 160, 195, 235, 280,
        330, 280, 235, 195, 160, 130, 105, 83, 65, 50],
    [28, 38, 50, 65, 83, 105, 130, 160, 195, 235,
        280, 235, 195, 160, 130, 105, 83, 65, 50, 38],
    [20, 28, 38, 50, 65, 83, 105, 130, 160, 195,
        235, 195, 160, 130, 105, 83, 65, 50, 38, 28],
    [15, 20, 28, 38, 50, 65, 83, 105, 130, 160,
        195, 160, 130, 105, 83, 65, 50, 38, 28, 20],
    [12, 15, 20, 28, 38, 50, 65, 83, 105, 130,
        160, 130, 105, 83, 65, 50, 38, 28, 20, 15]
]

tamanho = len(matriz)


def encontrar_pico():
    for i in range(1, tamanho - 1):  # Evita bordas
        for j in range(1, tamanho - 1):
            # Pega os vizinhos
            cima = matriz[i-1][j]
            baixo = matriz[i+1][j]
            esquerda = matriz[i][j-1]
            direita = matriz[i][j+1]
            centro = matriz[i][j]

            # Verifica se é um pico
            if centro > cima and centro > baixo and centro > esquerda and centro > direita:
                print(f"Pico encontrado em ({i}, {j}) com valor {centro}")
                return

    print("Nenhum pico encontrado")


encontrar_pico()
