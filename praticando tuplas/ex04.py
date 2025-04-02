cont = 0
n1 = int (input ('Digite um número: '))
n2 = int (input ('Digite outro número: '))
n3 = int (input ('Digite mais um número: '))
n4 = int (input ('Digite o último número: '))
valores = (n1, n2, n3, n4)
print (f'Você digitou os valores {valores} ')
print (f'O valor {n1} apareceu {valores.count(n1)} vezes')
print (f'O valor {n3} apareceu na posição {valores.index(n3)+1}')
print ('Os valores pares digitados foram: \n', end = '')
for n in valores:
    if n % 2 == 0:
        print (n, end = '')
        print ('')