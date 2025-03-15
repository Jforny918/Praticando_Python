#from math import factorial - utilizando math.factorial
#n1 = int ("Digite um número para calcular o seu fatorial: ")
#print (" O fatorial de {} é {}".format (n1, f))

n = int (input ("Digite um número para calcular o seu fatorial: "))
c = n
f = 1
print ("Calculando {}! = ".format(n), end="") #o end="" serve para não pular linha
while c > 0: #enquanto c for maior que 0, ele irá imprimir o valor de c e multiplicar pelo
#valor de f, depois irá decrementar 1 do valor de c
    print ("{}".format (c), end="") #imprime o valor de c
    print ( " x " if c > 1 else " = ", end= "") #se c for maior que 1, ele irá imprimir "x", senão, ele irá imprimir "="
    f *= c 
    c -= 1
print ("{}".format (f))

    