lanche = ('Hamburguer', 'Pizza', 'Suco', 'Pudim')
#HAMBURGUER [0], PIZZA [1], SUCO [2], PUDIM [3]
print (lanche [3]) # vai exibir o valor da posição 3 da tupla
print (lanche [1:3]) # vai exibir os valores da posição 1 até a 3 (não inclui a 3)
print (lanche [1:]) # vai exibir os valores da posição 1 até o final
print (lanche [1]) #vai exibir o valor da posição 1 da tupla
print (lanche [0]) #vai exibir o valor da posição 0 da tupla

for comida in lanche:
    print (f'Eu comi {comida}')
print ('Comi para caramba hoje!')

for cont in range (0, len(lanche)):
    print (f'Eu comi {lanche[cont]}') #o cont é o contador que vai de 0 até o tamanho da tupla 
    #- len(lanche) - e vai exibir os valores da tupla
print ('Comi para caramba hoje!')

for posicao, comida in enumerate (lanche): #o enumerate serve para enumerar os valores da tupla
    #ou seja, vai exibir o valor e a poisição da tupla.
    print (f'Vou comer {comida} na posição {posicao}')
print ('Comi para caramba hoje!')

print (sorted(lanche)) #vai ordenar os valores em ordem alfabética
#print (lanche) #não vai alterar a tupla original e vai exibir na ordem original

print (lanche.count('Pizza')) #vai contar quantas vezes o valor 'pizza' aparece na tupla
print (lanche.index('Suco')) #vai exibir a posição do valor 'pizza' na tupla

#del (lanche) #vai deletar a tupla
#print (lanche) #vai dar erro porque a tupla foi detectada