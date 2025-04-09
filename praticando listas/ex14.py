valores = []
for c in range (0, 7):
    valores.append(int(input('Digite um valor: ')))
    resposta = input ('Deseja continuar? [S/N]: ').strip().lower()
    if resposta not in ('sim','s'):
        break
print ('-'*40)
lista_pares = [num for num in valores if num % 2 == 0]
# Corrigindo a lista de ímpares
lista_impares = [num for num in valores if num % 2 != 0]

print (f'A lista de PARES é: {sorted(lista_pares)}')
print (f'A lista de ÍMPARES é: {sorted(lista_impares)}')
    