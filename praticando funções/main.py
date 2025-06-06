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

#FUNÇÕES PARTE 2
#help () - função que mostra a documentação de uma função, ou seja, o que a função faz, como se fosse um manual.
#help (print) - mostra a documentação da função print - então dentro do parênteses, você coloca o nome da função que deseja ver a documentação.

#docstrings - são strings que ficam dentro de uma função e servem para documentar o que a função faz.
#exemplo de docstring:
def somar (a, b):
    """Essa função recebe dois números e retorna a soma deles."""
    return a + b
#chamando a função
print (somar(4, 5)) #irá retornar a soma de 4 e 5, que é 9



