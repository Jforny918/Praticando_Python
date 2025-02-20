import math #Importando o módulo math inteiro
n1=float(input('Digite um número: '))
print ('O número {} tem a parte inteira {}'.format(n1,math.trunc(n1))) #Utilizando a função trunc do módulo math


from math import trunc #Importando a função trunc do módulo math (truncamento)
n1=float(input('Digite um número: '))
print ('O número {} tem a parte inteira {}'.format(n1,trunc(n1))) 


num = float(input('Digite um número: '))
print ('O número {} tem a parte inteira {}'.format(num,int(num))) #Utilizando a função int do Python
