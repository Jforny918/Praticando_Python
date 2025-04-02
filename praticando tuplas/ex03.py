num = (1,2,3,4,5,6,7,8,9,10) #decarando uma tupla com números de 1 a 10
from random import randint #randint é uma função que gera números aleatórios
num = (randint(0,10), randint(0,10), randint (0,10), randint (0,10)) #vai realizar o sorteio de 4 
#números aleatórios entre os que estão na tupla
print (F'OS NÚMEROS SORTEADOS FORAM: ', end= '') #o end='' vai fazer com que a próxima linha não pule 
#de linha
for n in num: #para cada variável n em num (que é a tupla)
    print (f'{n} ', end = '') #vai exibir os números sorteados
    soma = sum(num) #a função sum vai somar todos os valores sorteados .
print (f'\nO maior valor sorteado foi {max(num)}') #max vai exibir o maior número da tupla
print (f'O menor valor sorteado foi {min(num)}') #min vai exibir o menor número da tupla
print (f'A soma dos valores sorteados é: {soma}') #vai exibir a soma dos valores sorteados

