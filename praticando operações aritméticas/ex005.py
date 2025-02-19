print ('======DESAFIO 05======')
# Formas de escrever na tela
nome=input ('Qual o seu nome? ')
print('Prazer em te conhecer {}!'. format(nome))
print (' Prazer em te conhecer {:20}!'. format(nome)) # 20 espaços
print (' Prazer em te conhecer {:>20}!'. format(nome)) # 20 espaços alinhado a direita
print (' Prazer em te conhecer {:<20}!'. format(nome)) # 20 espaços alinhado a esquerda
print (' Prazer em te conhecer {:^20}!'. format(nome)) # 20 espaços centralizado
print (' Prazer em te conhecer {:=^20}!'. format(nome)) # 20 espaços centralizado com sinal de igual
print (' Prazer em te conhecer {:=>20}!'. format(nome)) # 20 espaços alinhado a direita com sinal de igual
print (' Prazer em te conhecer {:=<20}!'. format(nome)) # 20 espaços alinhado a esquerda com sinal de igual

print ('======DESAFIO 05_PART 3======') #Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.
n1=int(input('Digite um número: '))
print ('O sucessor de {} é {} e o antecessor é {}'.format(n1, n1+1, n1-1))