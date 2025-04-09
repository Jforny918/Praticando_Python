valores = []
while True:
    valor = int(input('Digite um número: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado na lista.')

    escolha = input('Você deseja continuar? [S/N] ').strip().lower()
    if escolha not in ('s', 'sim'):
        break

print('A lista completa é: {}'.format(valores))

# Criando a lista de pares
lista_pares = [num for num in valores if num % 2 == 0]
# Corrigindo a lista de ímpares
lista_impares = [num for num in valores if num % 2 != 0]

print('A lista de pares é: {}'.format(lista_pares))
print('A lista de ímpares é: {}'.format(lista_impares))
