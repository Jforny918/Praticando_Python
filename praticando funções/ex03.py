def dobra (lista):
    pos = 0 
    while pos < len (lista):
        lista [pos] *= 2
        pos += 1
#ou seja, enquanto a posição for menor que o tamanho da lista, irá multiplicar por 2

#outra forma de fazer
#def dobra (lista):
#    for pos in range (len(lista)):
#        lista [pos] *= 2
#ou seja, para cada posição na lista, irá multiplicar por 2

valores = [7, 8, 9, 10]
dobra(valores)
print (valores)
