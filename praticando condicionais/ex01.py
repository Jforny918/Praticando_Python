from random import randint 
from time import sleep
print ('EXERCÍCIO 01 - ADVINHANDO O NÚMERO QUE O COMPUTADOR PENSOU')
print ()
computador = randint(0,5) #Faz o computador "pensar"
print ('Vou pensar em um número entre 0 e 5. Tente advinhar...')
jogador = int(input('em que número eu pensei? ')) #jogador tenta advinhar
print ('PROCESSANDO...')
sleep (2)
if jogador == computador: 
    print ('Parabéns, você conseguiu me vencer!')
else: 
    print ('Ganhei! eu pensei no número {} e não no número {}'.format(computador, jogador))
