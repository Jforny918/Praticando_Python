n = float (input ('Digite um número: '))
r = input ('Quer continuar? [S/N] ').upper().strip()[0]
media = 0 
#inicializa a media com valor 0
soma = 0
#inicializa a soma com valor 0
cont = 0
#inicializa o contador com valor 0
soma+= n 
#soma = soma + n -> vai somar os valores digitados 
cont+= 1
#cont = cont + 1 -> vai somar a quantidade de números que foi digitado
while r == "S":
    #enquanto a resposta for S (SIM), ele vai continuar pedindo para digitar um número
    n = float (input ('Digite um número: '))
    soma+= n 
    cont+= 1
    r = input ('Quer continuar? [S/N] ').upper()

if cont > 0: 
    #se o contador for maior que 0, ele pode executar o cálculo da média normalmente e exibir os resultados
    media = soma / cont
    print ('Foram digitados {} números e a média entre eles é {}'.format (cont, media))
else: 
    #senao ele irá exibir que nenhum valor foi digitado
    print ('Nenhum número foi digitado.')

