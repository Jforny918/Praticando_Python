pesomaior = 0 #declara a variável pesomaior com o valor 0
pesomenor = 0 #declara a variável pesomenor com o valor 0
for p in range (1, 6):
    peso = float (input ("Digite o peso da {}ª pessoa: ".format(p)))
    if p == 1: #primeira vez que o laço é executado ele entende que o peso maior e menor são iguais
        #o p é a posição
        pesomaior =  peso
        pesomenor = peso
    else: #a partir da segunda vez que o laço é executado ele compara os pesos 
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print ("O MAIOR peso lido foi de {} Kg e o MENOR peso lido foi de {} Kg.".format(pesomaior, pesomenor))