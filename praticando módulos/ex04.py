print ('Exercício 04')  #calculo de seno, cosseno e tangente de um ângulo
print ('')
from math import sin, cos, tan
ang=float(input('digite o valor do ângulo: '))
seno = sin(ang)
cosseno = cos (ang)
tangente = tan (ang)
print ('O ângulo {} tem como seno {}, cosseno {} e tangente {}'.format(ang,seno,cosseno, tangente))

#para o resultado ser em graus, é necessário converter o valor do ângulo para radianos
#para isso, é necessário importar a função radians do módulo math
#exemplo:
# from math import radians
# ang=float(input('digite o valor do ângulo: '))
# ang=radians(ang)
# seno = sin(ang)
# cosseno = cos (ang)
# tangente = tan (ang)
# print ('O ângulo {} tem como seno {}, cosseno {} e tangente {}'.format(ang,seno,cosseno, tangente))