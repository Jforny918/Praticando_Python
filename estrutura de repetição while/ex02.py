from random import randint
from time import sleep
computador = randint (0, 10)
nome = input ("Olá, bem vindo ao jogo de advinhação! Qual o seu nome? ")
print (("Olá, {}! Eu sou seu computador!".format (nome)))
print ("Vou pensar num número entre 0 e 10. Tente advinhar...")
sleep (2) #tempo de espera simulando o computador estar pensando
print ("Pronto! Já pensei em um número! Tente advinhar!")
acertou = False #variável innicializada como False
palpites = 0 #palpites iniciais é 0
while not acertou: #enquanto não acertar, ele irá pedir para o jogador tentar novamente
    jogador = int (input ("Qual é o seu palpite? "))
    palpites += 1 #palpites + 1
    if jogador == computador: #se o jogador acertar o número que o computador pensou, ele exibirá a mensagem de parabenização
        acertou = True
    else:
        if jogador < computador: #se o jogador digitar um valor menor que o número que o computador pensou, ele exibirá a mensagem abaixo
            print ("Mais...Tente novamente!")
        elif jogador > computador: #se o jogador digitar um valor maior que o número que o computador pensou, ele exibirá a mensagem abaixo
            print ("Menos...Tente novamente!")   
print ("Parabéns, {}! Você acertou! O número que eu pensei foi {}".format (nome, computador))
print ("Foram necessários {} palpites para você acertar!".format (palpites))
