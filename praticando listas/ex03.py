valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate (valores):
    print (f'NA POSIÇÃO {c} ENCONTREI O VALOR {v}')
print ('-'*40)
print ('CHEGUEI AO FINAL DA LISTA!')