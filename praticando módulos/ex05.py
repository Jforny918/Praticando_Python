print ('Exercício 05') #sorteando um nome entre quatro alunos
print ('')
n1=input('Digite o nome do primeiro aluno: ')
n2=input('Digite o nome do segundo aluno: ')
n3=input('Digite o nome do terceiro aluno: ')
n4=input('Digite o nome do quarto aluno: ')
print ('')
lista = [n1,n2,n3,n4]
from random import choice 
print ('O aluno escolhido foi {}'.format(choice(lista)))
    
