print ('Exercício 05 - Alistamento militar')
print ()
from datetime import date
atual = date.today().year
nome = str(input('Digite qual o seu nome: '))
print ('---'*20)
print ('Prazer em te conhecer, {}'.format (nome))
nasc = int(input('Em que ano você nasceu? '))
print ()
print ('O ano que você nasceu é {}'.format(nasc))
idade = atual - nasc
print ('Você tem {} anos!'.format(idade))
if idade == 18:
    print ('Você precisa se alistar IMEDIATAMENTE')
elif idade < 18: 
    saldo = 18 - idade
    print ('Você ainda não tem 18 anos, faltam {} anos para o seu alistamento'.format(saldo))
    ano = atual + saldo
    print ('O seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print ('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print ('Seu alistamento foi em {}'.format(ano))


