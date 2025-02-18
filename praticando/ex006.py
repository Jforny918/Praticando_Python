print ('======DESAFIO 06======') 
#Crie um algoritmo que leia dois números e mostre a soma, produto, divisão e potência entre eles.
n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
s=n1+n2
m=n1*n2
d = n1/n2
d1 = n1//n2
e =n1**n2
print ('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' \n') 
# end=' ' faz com que o print não pule linha
# :3f faz com que a divisão tenha 3 casas decimais
# \n pula linha
print ('Divisão inteira é {} e a potência é {}'.format(d1, e))