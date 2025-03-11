n=int(input("Digite um número: "))
tot = 0 #ele começa a contagem com 0.
for c in range (1, n+1): #traduzindo: para cada c no intervalo de 1 até n+1.
    if n % c == 0: #condição para saber se o número é divisível por n.	#o c é o contador que vai de 1 até n.
        print ("\033[33m", end=' ') #\033[33m é para deixar a cor amarela nos números que são divisíveis por n.
        tot += 1 #ele vai contar quantas vezes o número foi divisível.
    else:
        print ("\033[31m", end=' ') #\033[31m é para deixar a cor vermelha nos números que não são divisíveis por n.
    print( ' {} '.format(c), end=' ') #ele vai mostrar os números de 1 até n.
print ("\n\033[mO número {} foi divisível {} vezes.".format(n, tot)) #ele vai mostrar quantas vezes o número foi divisível.
if tot == 2: #se o número for divisível por 2 números, ele é primo.
    print ("E por isso ele é PRIMO.")
else: #se o número não for divisível por 2 números, ele não é primo.
    print ("E por isso ele NÃO É PRIMO.")

  
