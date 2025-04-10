print ('-------- MEGA SENA --------')
from random import randint #importando biblioteca que gera números aleatórios
from time import sleep #importando a biblioteca que faz o programa "dormir" por um tempo determinado 
lista = [] #criando uma lista vazia para armazenar os números sorteados
jogos = [] #criando uma lista vazia para armazenar o número de jogos
print ('-'*30)
quant = int (input ('Quantos jogos você deseja sortear? ')) 
tot = 1 #variável que controla o número de jogos, iniciando em 1
while tot <= quant: #enquanto o total de jogos for menor que a quantidade de jogos informada, ele vai executar o loop abaixo
    cont = 0 #quantidade de números sorteados, iniciando em 0
    while (True): #enquanto o número sorteado não estiver na lista, ele vai executar o loop abaixo
        num = randint (1, 60) #gerando um número aleatório entre 1 e 60
        if num not in lista: #se o número ainda não estiver na lista, ele vai adicionar o número à lista
            lista.append (num)
            cont += 1 #incrementando a quantidade de números sorteados
        if cont >= 6: #se o contador for maior ou igual a 6, ele vai sair do loop
            break
    lista.sort() #ordenando em ordem crescente a lista de números sorteados
    jogos.append(lista[:]) #adicionando a lista de números sorteados à lista de jogos
    lista.clear() #limpando a lista de número sorteados para o próximo jogo
    tot += 1 #incrementando ao total de jogos
print ('-'*3, f'Sorteando {quant} jogos', '-' *3)
for i, l in enumerate (jogos): #para cada jogo, ele vai imprimir os números sorteados
    print (f'Jogo {i+1}: {l}')
    sleep (2)
print ('-'*8, 'BOA SORTE!', '-'*8)


