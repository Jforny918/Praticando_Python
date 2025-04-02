valores = []
valores.append(5)
valores.append(8)
valores.append(6)
valores.append(4)
valores.append(10)

for c, v in enumerate(valores):
#a função enumerate() retorna o índice e o valor de cada elemento na lista
    print (f'Na posição {c} encontrei o valor {v}')
print ('-'*40)
print ('Cheguei ao final da lista!')