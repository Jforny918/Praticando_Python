soma = 0 #ele começa a soma com 0.
cont = 0 #ele começa a contagem com 0.
for c in range (1,7):
    n=int(input('Digite um valor: ')) #ele vai pedir para digitar um valor 7 vezes
    if n % 2 == 0: #se o número for par, ele vai somar.
        soma += n
        cont += 1
print ('Voce informou {} números PARES e a soma deles é {}'.format(cont, soma)) #ele vai mostrar quantos números foram digitados e a soma deles.