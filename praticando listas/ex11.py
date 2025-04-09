teste = list ()
teste.append ('Júlia')
teste.append (20)
galera = list ()
galera.append (teste[:]) #@o [:] serve para copiar a lista teste, se não usar o [:] ele vai adicionar a lista teste na lista galera
#e não os valores dela
teste [0] = 'Maria'
teste [1] = 22
galera.append (teste[:])
print (galera)