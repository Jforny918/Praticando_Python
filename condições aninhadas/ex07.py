from datetime import date
anoatual = date.today().year
print ('Hoje vamos descobrir a sua categoria no esporte NATAÇÃO através da sua idade!')
print ()
anonasc=int(input('Digite o ano em que você nasceu: '))
idade = anoatual - anonasc
print ('A sua idade é {}'.format(idade))
if idade <= 9: 
    print ('Você é um nadador da categoria MIRIM.')
elif idade > 9 and idade <=14:
    print ('Você é um nadador da categoria INFANTIL.')
elif idade > 14 and idade <=19:
    print ('Você é um nadador da categoria JUNIOR.')
elif idade > 19 and idade <=25:
    print ('Você é um nadador da categoria SÊNIOR.')
else:
    print ('Você é um nadador da categoria MASTER.')

