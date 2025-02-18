print ("======DESAFIO 08======")
#Crie um algoritmo que leia um número e mostre o seu dobro, o triplo e a raiz quadrada.
n1=int(input ('Digite um número: '))
d=n1*2
t=n1*3
r=n1**(1/2)
print ('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(n1, d, t, r))
# {:.2f} faz com que a raiz quadrada tenha 2 casas decimais