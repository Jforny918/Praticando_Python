valores = []
maior = menor = 0 
for c in range (0,5):
   valores.append(int(input(f'Digite um valor na posição {c}: ')))

   if c == 0:
        maior = menor = valores[c]

   else: 
        if valores[c] > maior:
            maior = valores[c]

        if valores[c] < menor:
            menor = valores[c]

print ('=-'*40)
print (f'A lista criada foi {valores}') 
print ('=-'*40)   
print (f'O MAIOR valor digitado foi {maior} na posições: ',end = '')   
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end = '')
print()
print ('-'*40)
print (f'O MENOR valor digitado foi {menor} nas posições: ',end = '')   
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end = '')    
print()

     