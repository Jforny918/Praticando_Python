matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'Digite um valor para a posição [{i}][{j}]: ')))
    matriz.append(linha)  # Adiciona a linha completa à matriz após preenchê-la

print('-' * 40)

# Imprimindo a matriz
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]}]', end=' ')
    print()  # Para pular para a próxima linha após imprimir uma linha da matriz