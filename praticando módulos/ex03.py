print ("Exercício 03") #calculando a hipotenusa de um triângulo retângulo
print ("")
import math
catadj=float(input('Digite o valor do cateto adjacente: '))
catop=float(input('Digite o valor do cateto oposto: '))
h1= math.hypot(catadj,catop) 
print ('O valor da hipotenusa é {}'.format(h1))

from math import hypot
catadj=float(input('Digite o valor do cateto adjacente: '))
catop=float(input('Digite o valor do cateto oposto: '))
h2= hypot(catadj,catop)
print ('O valor da hipotenusa é {}'.format(h2))