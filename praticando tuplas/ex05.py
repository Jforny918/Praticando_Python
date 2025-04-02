listagem = ('Lápis', 1.75, 'Caneta', 2.00, 'Borracha', 0.50, 'Caderno', 15.90, 'Mochila', 120.00,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.00,
            'Canetas', 22.30, 'Régua', 6.50, 'Cola', 3.00, 'Tesoura', 8.00)
print ('-'*40)
print (f'{'LISTAGEM DE PREÇOS':^40}')	#O ^  é para centralizar o texto na tela
print ('-'*40) 
for pos in range (0, len(listagem)): #ele vai percorrer a lista de 0 até o final
    if pos % 2 == 0: #se a posição for par, ele vai exibir o nome do produto
        print (f'{listagem[pos]:.<30}', end = '') #O .< é para alinhar a esquerda o nome do produto 
#end = '' é para não pular de linha
#listagem[pos]:.<30 é para exibir o nome do produto com 30 espaços a esquerda
#se a posição for ímpar, ele vai exibir o preço do produto
else:
        print (f'R${listagem[pos]:>7.2f}')