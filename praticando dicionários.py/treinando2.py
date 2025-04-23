estado = dict()
brasil = list()
for c in range (0, 3):
    estado ['UF'] = str(input ('Unidade Federativa: '))
    estado ['Sigla'] = str (input ('Sigla do estado: '))
    brasil.append(estado.copy()) #copiando o dicionário para a lista brasil
print (brasil)
for e in brasil: 
    print (f'A siga do estado {e['UF']} é {e['Sigla']}')
    for k, v in e.items (): #para cada item no dicionário, ele vai exibir a mensagem abaixo
        print (f'O campo {k} tem valor {v}')
