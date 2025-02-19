print ('======DESAFIO 17======')
#algoritmo para calcular a hipotenusa de um triângulo retângulo
l1=float(input('Digite o comprimento do cateto oposto: '))
l2=float(input('Digite o comprimento do cateto adjacente:'))
h=(l1**2+l2**2)**(1/2)
print ('A hipotenusa do triângulo retângulo é {:.2f}'.format(h))