n = cont = soma = 0 
n = int (input ('Digite um número [99 para parar]: '))
while n!= 99:
   cont += 1
   soma += n
   n = int (input("Digite um número [99 para parar]: "))
print ('Você digitou {} números e a soma entre eles foi {}'.format (cont, soma))
   
