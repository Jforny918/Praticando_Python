soma = 0
cont = 0
for c in range (1, 501, 2): #ele vai contar de 1 até 500, de 2 em 2.
    if c % 3 == 0: #se o número for múltiplo de 3, ele vai mostrar na tela.
        print(c, end=' ') #ele vai mostrar os números de 3 em 3 na mesma linha. #end=' ' é para não pular linha.
        soma += c #ele vai somar os números múltiplos de 3.
        cont += 1 #ele vai contar quantos números múltiplos de 3 ele encontrou.
print('\nA soma de todos os {} valores é {}'.format(cont, soma)) #ele vai mostrar quantos números múltiplos de 3 ele encontrou e a soma deles.
