from datetime import date
atual = date.today().year
nome = (input ("Qual é o seu nome? "))
idade = int(input('Qual a sua idade? '))
idade = atual - idade
print (f'{nome} nasceu em {idade}')
