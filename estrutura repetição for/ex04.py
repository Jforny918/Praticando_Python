# Problem: Tabuada
n=int(input('Digite um número para ver a sua tabuada: '))
for c in range (1, 11):
    print ('{} x {:2} = {}'.format(n, c, n*c)) # {:2} é para alinhar os números da tabuada.
# n é o número da tabuada que o usuário escolher.
# c é o contador que vai do 1 até o 10.
# n*c é o resultado da tabuada. 

