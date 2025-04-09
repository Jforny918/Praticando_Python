matriz = []
maior = spar = scol = 0
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

print('-' * 40)
#Soma dos valores da terceira coluna
for i in range (3):
    scol += matriz[i][2]
#Soma dos valores da segunda linha
for j in range (3):
    spar += matriz[1][j]
#Maior valor da matriz
for i in range (3):
    for j in range (3):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
#Imprimindo os resultados
print(f'A soma dos valores da terceira coluna é: {scol}')
print(f'A soma dos valores da segunda linha é: {spar}')
print(f'O maior valor da matriz é: {maior}')
print('-' * 40)