print ('======DESAFIO 13======')
#Calcular a área de um terreno e a quantidade de tinta necessária para pintá-lo sabendo que cada litro de tinta pinta uma área de 2m.
l=float(input("Digite a largura do terreno: "))
c=float(input('Digite o comprimento do terreno: '))
a=l*c
t=a/2
print ('A área do terreno é {} m² e a quantidade de tinta necessária para pintá-lo é {} litros'.format(a,t))
