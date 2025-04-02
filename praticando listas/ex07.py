valores = []

while len(valores) < 5:  # Continua até que a lista tenha 5 valores
    valor = int(input('Digite um número: '))
    if valor not in valores:
        # Encontrar a posição correta para inserir o valor
        pos = 0
        while pos < len(valores) and valores[pos] < valor:
            pos += 1
        valores.insert(pos, valor)  # Insere o valor na posição correta
        print(f'Valor {valor} adicionado na posição {pos} da lista!')
    else: 
        print('Valor duplicado! Não será adicionado na lista.')

    # Pergunta se o usuário deseja continuar
    if len(valores) < 5:  # Apenas pergunta se a lista ainda não tem 5 valores
        continuar = input('Deseja continuar adicionando valores? [S/N]: ').strip().lower()
        if continuar not in ('s', 'sim'):
            break

print(f'Os valores digitados formaram a lista abaixo:\n{valores}')