for c in range (1, 51): #ele vai contar de 1 até 50, de 1 em 1.
    if c % 2 == 0: #se o número for par, ele vai mostrar na tela.
        print(c, end=' ') #ele vai mostrar os números pares na mesma linha. #end=' ' é para não pular linha.
print('FIM') #ele vai mostrar FIM no final.

#outra forma de fazer essa contagem:

for c in range (2, 51, 2): #ele vai contar de 2 até 50, de 2 em 2.
    print(c, end=' ') #ele vai mostrar os números pares na mesma linha. #end=' ' é para não pular linha.
print('FIM') #ele vai mostrar FIM no final.
