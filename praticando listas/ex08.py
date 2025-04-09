valores = [] 
cont = 0
maior = 0
menor = 0
while True:
    valor = int (input ('Digite um número: '))
    cont+= 1
    if cont == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        if valor not in valores:
            valores.append (valor)
            print ('Valor adicionado com sucesso!')
        else:
            print ('Valor duplicado! Não será adicionado na lista.')
    escolha = input ('Você deseja continuar? [S/N]: ').strip().lower()
    if escolha not in ('s', 'sim'):
        break
print ('Você digitou {} números'.format(cont))
print ('Os números em ordem descrescente são {}'.format (sorted(valores, reverse = True)))
if 5 in valores:
    print ('O número 5 está na lista!')
else:
    print ('O número 5 não está na lista!')
print ('O maior número digitado foi {}'.format(maior))
print ('O menor número digitado foi {}'.format(menor))
