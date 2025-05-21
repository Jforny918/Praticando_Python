def contador ( * num): #função que irá exibir os números que foram passados como parâmetro
    for valor in num: #para cada valor na variável num, irá imprimir
        #a variável num é uma tupla, então não é necessário usar o range porque ela já é uma sequência de valores
        print (f"{valor} ", end = ' ') #como será exibido cada vez que chamar a função
    print ("FIM")
#chamando a função
contador (1, 2, 3, 4, 5) 
contador (8, 0)
contador (4, 5, 6, 7, 8, 9)


def contador ( * num):
    print (f'Recebi os valores {num} e são {len(num)} números')

#chamando a função
contador (1, 2, 3, 4)
contador (8, 0)