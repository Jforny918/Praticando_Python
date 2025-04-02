valores = []
while True: 
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print ('Valor duplicado! Não vou adicionar...')
    resp = input('Deseja continuar? [S/N]: ').strip().lower()
    if resp not in ('s', 'sim'):
        break

# Exibindo os resultados
print(f'Você digitou {len(valores)} valores.')
print(f'A lista formada a partir dos valores digitados foi: {valores}')
