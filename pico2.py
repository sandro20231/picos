import sys

# início contagem do tempo

# Array de uma dimensão
Array = [1.0, 2.14, 3.28, 4.41, 5.55, 6.69, 7.83, 8.97, 10.10, 11.24,
         12.38, 13.52, 14.66, 15.79, 16.93, 18.07, 19.21, 20.34, 21.48, 22.62,
         23.76, 24.90, 26.03, 27.17, 28.31, 29.45, 30.59, 31.72, 32.86, 34.00,
         35.14, 36.28, 37.41, 38.55, 39.69, 40.83, 41.97, 43.10, 44.24, 45.38,
         46.52, 47.66, 48.79, 49.93, 51.07, 52.21, 53.34, 54.48, 55.62, 56.76,
         57.90, 59.03, 60.17, 61.31, 62.45, 63.59, 64.72, 65.86, 67.00, 68.14,
         69.28, 70.41, 71.55, 72.69, 73.83, 74.97, 76.10, 77.24, 78.38, 79.52,
         80.66, 81.79, 82.93, 84.07, 85.21, 86.34, 87.48, 88.62, 89.76, 90.90,
         92.03, 93.17, 94.31, 95.45, 96.59, 97.72, 98.86, 100.00, 100.00, 99.11,
         98.22, 97.32, 96.43, 95.54, 94.65, 93.76, 92.86, 91.97, 91.08, 90.19,
         89.30, 88.41, 87.51, 86.62, 85.73, 84.84, 83.95, 83.05, 82.16, 81.27,
         80.38, 79.49, 78.59, 77.70, 76.81, 75.92, 75.03, 74.14, 73.24, 72.35,
         71.46, 70.57, 69.68, 68.78, 67.89, 67.00, 66.11, 65.22, 64.32, 63.43,
         62.54, 61.65, 60.76, 59.86, 58.97, 58.08, 57.19, 56.30, 55.41, 54.51,
         53.62, 52.73, 51.84, 50.95, 50.05, 49.16, 48.27, 47.38, 46.49, 45.59,
         44.70, 43.81, 42.92, 42.03, 41.14, 40.24, 39.35, 38.46, 37.57, 36.68,
         35.78, 34.89, 34.00, 33.11, 32.22, 31.32, 30.43, 29.54, 28.65, 27.76,
         26.86, 25.97, 25.08, 24.19, 23.30, 22.41, 21.51, 20.62, 19.73, 18.84,
         17.95, 17.05, 16.16, 15.27, 14.38, 13.49, 12.59, 11.70, 10.81, 9.92,
         9.03, 8.14, 7.24, 6.35, 5.46, 4.57, 3.68, 2.78, 1.89, 1.00]
# definição do tamanho total do array
alt = len(Array)
# divisão por dois para achar o número do meio
v = alt // 2

# função recursiva para achar o pico


def pico(v):
    # se ovalor estiver fora do Array aparece mensagem de erro e fecha o programa
    if v <= 0 or v >= alt - 1:
        print("Valor fora do escopo do Array")
        sys.exit(1)
    # definição dos três valores
    a = Array[v-1]
    b = Array[v]
    c = Array[v+1]
    # se os tres valores estiverem subindo ache a metade da metade a frente
    if a < b < c:
        diferencial = (alt - v) // 2
        v = min(v + diferencial, alt-1)
        # recursivamente execute a função
        pico(v)
    # se os tres valores estiverem descendo ache a metade da metade para traz
    elif a > b > c:
        diferencial = (alt - v) // 2
        v = max(v-diferencial, 0)
        # recursiva função
        pico(v)
    # Em ultimo caso o pico foi encontrado
    else:
        print("pico encontrado: ", Array[v])
        sys.exit(0)


pico(v)
