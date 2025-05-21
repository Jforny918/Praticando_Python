a = 4
b = 5
s = a + b
print (s)

a = 8 
b = 9
s = a + b
print (s)

a = 2
b = 1 
s = a + b
print (s)

# s = a + b aparece várias vezes, então para evitar isso, podemos criar uma função

def soma (a, b):
    s = a + b
    print (s)

soma (4, 5)
soma (8, 9)
soma (2, 1)
soma (1, 1)
soma (10, 3)

#posso dizer explicitamente qual é o valor de a e b
#exemplo
#def soma (a, b):
#    s = a + b
#    print (s)
#soma (b = 4, a = 5)
