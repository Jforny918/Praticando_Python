#galera = [['Júlia', 20], ['Cláudia', 55], ['Bruno', 53], ['Gabriel', 27], ['Snow', 8]]

#for p in galera: 
    #print (f'{p[0]} tem {p[1]} anos de idade.')
#p[0] vai mostrar o nome na posição 0 de cada sublista e p[1] vai mostrar a idade na posição 1 de cada sublista


galera =[]
dado = []
totmaior = totmenor = 0
for c in range (0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input ('Idade: ')))
    galera.append(dado[:]) #adiciona a lista dado na lista galera
    dado.clear() #limpa a lista para não repetir dados
print (galera)
for p in galera:
    if p[1] >= 18:
        print (f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print (f'{p[0]} é menor de idade.')
        totmenor += 1
print (f'Temos {totmaior} maiores de idade e {totmenor} menores de idade.')
    