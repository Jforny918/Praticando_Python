#progressão aritmética
a1=int(input('Digite o primeiro termo da PA: ')) #primeiro termo da PA
r=int(input('Digite a razão da PA: ')) #razão da PA
n = int(input('Digite o número de termos da PA: ')) #número de termos da PA
for c in range (n): #ele vai mostrar a PA de acordo com o número de termos que o usuário escolher.
    an = a1 + c*r #fórmula da PA #o uso do c é para mostrar a PA de acordo com o número de termos que o usuário escolher (n).
    print(an, end=' ') #ele vai mostrar a PA na mesma linha. #end=' ' é para não pular linha.

    #podemos fazer também assim:
    #a1=int(input("digite o primeiro termo da PA: "))
    #r=int(input("digite a razão da PA: "))
    #décimo (ou o número de termos que você quiser) = a1 + (10 - 1) * r
    #for c in range(a1, décimo + r, r):
    #    print(c, end=' ')
    #print('Fim')
    #décimo é o número de termos que você quer mostrar da PA.
    #o uso do 10 é para mostrar 10 termos da PA.
    #o uso do 10 - 1 é para mostrar 9 termos da PA.
    #output: 1 3 5 7 9 11 13 15 17 19 Fim