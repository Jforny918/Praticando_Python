from random import randint #importando randint do módulo random para gerar números aleatórios

def somapar (lista): #função que irá somar os valores pares de uma lista
    soma = 0 #inicializando soma como 0
    for valor in lista: #para cada valor na lista, ele irá realizar:
        if valor % 2 == 0: #verificar se o valor for par, se for, então:
            soma += valor #soma o valor à variável soma
    return soma #retorna a soma dos valores pares
    
lista = [] #gerando uma lista vazia para armazenar os valores aleatórios
for i in range (5): #para cada número de 0 a 4 (5 números no total):
    lista.append (randint (1,100)) #irá sortear número aleat´rio de 1 a 100 e adicionar à lista
    print (lista[i], end = '  ')
print ('\nA lista gerada foi: ', lista)
print ('\nA soma dos valores pares da lista é: ', somapar(lista))


