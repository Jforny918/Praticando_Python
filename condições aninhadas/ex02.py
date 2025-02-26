print ('EXERCÍCIO 03 - APROVANDO EMPRÉSTIMO BANCÁRIO')
print ()
nome=str(input('Qual é o seu nome? '))
print ('Bem-vindo, {}!'.format(nome)) 
print ()
print ('Para aprovar o seu empréstimo para a compra da sua casa preciso que digite algumas informações abaixo: ')
print ()
casa=float(input('Valor da casa: R$'))
salario=float(input('Salário do comprador: R$'))
anos=int(input('Quantos anos de financiamento? '))
prestaçao=casa / (anos * 12)
mínimo= salario * 30 / 100
print ('Para pagar uma casa de R${:.2f} em {} anos'.format(casa,anos))
print ('a prestação será de R${:.2f}'.format(prestaçao))
print ('O valor da sua casa é R${:.2f}'.format(casa))
if prestaçao<= mínimo:
    print ('Empréstimo CONCEDIDO.')
else:
    print ('Empréstimo NEGADO.')

