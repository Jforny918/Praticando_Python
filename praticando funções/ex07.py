from time import sleep
#função que importa a biblioteca time que usa o sleep para fazer pausas entre os prints
def maior (* num): #o asterisco indica que a função vai receber vários parâmetros
#função que vai receber vários parâmetros e vai analisar qual é o maior valor informado
    cont = maior = 0 #inicializando as variáveis cont e maior como 0

    print ('\n Analisando os valores passados...')
    print ('='*30)
    for valor in num:
    #para cada valor informado em num, irá realizar o seguinte:
        print (f'{valor} ', end = '', flush = True) #o flush = True faz com que o print seja exibido imediatamente
        sleep (0.5) #pausa
        if cont == 0: #se o contador for igual a 0, ou seja, se for o primeiro valor informado
            #o maior valor será o primeiro valor informado.
            maior = valor
        else: #senão, se já houver um valor informado, então irá comparar o valor informado com o maior valor.
            if valor > maior:
                maior = valor 
        cont += 1 #incrementa o contador a cada valor informado
    print (f'\nForam informados {cont} valores ao todo.')
    print ('-'*30)
    print (f'O maior valor informado foi {maior}!')

#programa principal
#parâmetros
maior (2, 6, 8, 10, 3, 1)
maior (4, 7, 0)
maior (6)
maior (1, 5)
maior ()