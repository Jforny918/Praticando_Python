print('=-' * 30)
print('LOJA MEGA BARATO')
print('=-' * 30)

totalcaro = 0
totalcompra = 0
cont = 0
menor = float('inf')  #inicializa menor com um valor muito alto
nome_barato = ""  #para armazenar o nome do produto mais barato

while True:
    nome = input('Nome do Produto: ')
    preco = float(input('Preço: R$ '))
    cont += 1 #soma a quantidade de vezes que foi digitado um novo produto
    totalcompra += preco #soma o preço de todas as compras realizadas

    #verifica se o preço é maior que 1000
    if preco > 1000:
        totalcaro += 1

    #verifica se o preço é o menor encontrado até agora
    if preco < menor:
        menor = preco
        nome_barato = nome  #atualiza o nome do produto mais barato

    r = input('Quer continuar? [S/N] ').strip().upper()[0]
    if r == 'N':
        break

# Exibe os resultados
print(f'O total da compra foi R$ {totalcompra:.2f}')
print(f'Temos {totalcaro} produto(s) custando mais de R$ 1000')
print(f'O produto mais barato foi {nome_barato} que custa R$ {menor:.2f}')
    