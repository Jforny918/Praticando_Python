#comando de escrita mais avançado que o print
def escreva (msg):

    tam = len(msg) + 4 #tamanho da mensagem + 4 para adicionar as bordas
    print ('^'*tam) #imprime o caractere de acordo com o tamanho da mensagem
    print (msg)
    print ('^'*tam) #imprime o caractere de acordo com o tamanho da mensagem

escreva ('Júlia Forny ama aprender Python!')
escreva ('Emily é linda e o cabelo dela é maravilhoso!')
