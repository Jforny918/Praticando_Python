#função em linguagem de programação está associada à rotina de execução de um programa,
#ou seja< é um bloco de código que pode ser chamado em qualquer parte do programa.

#função é um bloco de código que pode ser chamado em qualquer parte do programa.

#def é a palavra reservada para definir uma função.

#exemplo de função
def mostralinha ():
    print ("-" * 30)
#chamando a função
mostralinha()
print ("Curso em Vídeo")
mostralinha()
print ("Aprendendo Python")
mostralinha()
print ("Aprendendo Funções")
mostralinha()

#função com parâmetro
def mostralinha (msg): #a função irá receber a variável msg
    print ("-" * 30) 
    print (msg)
    print ("-" *30)
#chamando a função
mostralinha ("CURSO EM VÌDEO") #cada vez que chamar a função, irá imprimir a mensagem que foi passada para o parâmetro
mostralinha ("APRENDENDO PYTHON")