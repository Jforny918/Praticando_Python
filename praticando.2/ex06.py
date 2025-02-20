print ('Exercício 06') #sorteando a ordem de apresentação de quatro alunos
print ('')
n1=input('Digite o nome de primeiro aluno: ')
n2=input('Digite o nome do segundo aluno: ')
n3=input('Digite o nome do terceiro aluno: ')
n4=input('Digite o nome do quarto aluno: ')
print ('')
lista =[n1,n2,n3,n4]
from random import shuffle #embaralhando a lista
print ('A ordem de apresentação será: ') 
shuffle(lista)
print (lista)

