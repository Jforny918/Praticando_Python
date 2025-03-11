frase = str (input ("Digite uma frase: ")).strip().upper() 
#ele vai pedir para digitar uma frase ou palavra e vai tirar os espaços e colocar em maiúsculo.
print ("Voc~e digitou a frase {}".format(frase)) #ele vai mostrar a frase digitada.
palavras = frase.split() #ele vai separar as palavras da frase. Ex [Ana, Maria, ama, mama]
junto = ''.join(palavras) #ele vai juntar as palavras sem espaços. Ex [AnaMariaamamama]
inverso = '' #ele começa o inverso com vazio. 
for letra in range (len(junto) -1, -1, -1): #para cada letra no intervalo de junta -1 até -1, de -1 em -1. 
    #ele vai começar do último caractere até o primeiro, de trás para frente, invertendo a palavra.
    #len(junto) é o tamanho da palavra.
    inverso += junto[letra] #ele vai inverter a palavra.
print ('O inverso de {} é {}'.format(junto, inverso)) #ele vai mostrar a palavra e o inverso dela.
if inverso == junto: #se o inverso for igual a palavra, é um palíndromo.
    print ('Temos um palíndromo!')
else:
    print ('A frase digitada não é um palíndromo.') #se o inverso não for igual a palavra, não é um palíndromo.