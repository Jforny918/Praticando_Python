pessoas = []
totcadastros = 0
pesadas = leves = 0

while True:
    nome = input('Nome: ')
    peso = int(input('Peso: '))
    
    # Adiciona os dados da pessoa à lista
    pessoas.append([nome, peso])
    
    # Atualiza contadores
    totcadastros += 1
    if peso > 90:
        pesadas += 1
    else:
        leves += 1
    
    resposta = input('Deseja continuar? [S/N]: ').strip().lower()
    if resposta not in ('s', 'sim'):
        break

# Exibindo os resultados
print(f'Você cadastrou {totcadastros} pessoas.')


# Exibindo as pessoas mais pesadas e leves
print('As pessoas mais pesadas foram:')
for pessoa in pessoas:
    if pessoa[1] >= 90:
        print(f'Nome: {pessoa[0]}, Peso: {pessoa[1]}')
    
print('As pessoas mais leves foram:')
for pessoa in pessoas:
        if pessoa[1] <= 90:
            print(f'Nome: {pessoa[0]}, Peso: {pessoa[1]}')
    
