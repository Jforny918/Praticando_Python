from time import sleep
def contador (inicio,fim, passo): #determina a ordem dos parâmetros que serão passados para a função
    #função que irá contar de um número até outro, com um passo definido.

    print (f'\nContagem de {inicio} até {fim} de {passo} em {passo}')
    
    if passo < 0:
        passo *= - 1
    if passo == 0: 
        print ('Passo inválido! Considerando Passo igual a 1.')
        passo = 1

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print (f'{cont} ', end = '')
            sleep (0.5)
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print (f'{cont} ', end = '')                    
            sleep (0.5)
            cont -= passo

#chamando a função
contador (0, 100, 10)
contador (10, 0, 2) #contagem regressiva
print ()
print ('Agora é a sua vez de personalizar a contagem!')
ini = int (input ('Início: '))
fi = int (input ('Fim: '))
pas = int (input ('Passo: '))
contador (ini, fi, pas)
print ('Fim da contagem!') #mensagem de fim da contagem
