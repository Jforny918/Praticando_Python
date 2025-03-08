for c in range (1,6):
    print('Oi')
print('FIM')
# Output: Oi Oi Oi Oi Oi FIM 
#ele executa o oi 5 vezes, pois o range vai de 1 a 6, ou seja, 1,2,3,4,5. (ele não conta o 6)
#se quiséssemos incluir o 6, teríamos que colocar 1,7.
#o FIM está fora do loop, então ele só é executado uma vez.
#se colocar oo FIM dentro do loop, ele será executado 5 vezes.
for c in range (0,6):
    print(c)
print('FIM')
# Output: 0 1 2 3 4 5 FIM
#ele começa do 0 e vai até o 5, ou seja, 0,1,2,3,4,5.
#ele conta o 5, pois o 6 não está incluído.

for c in range (6,0,-1):
    print(c)
print('FIM')
# Output: 6 5 4 3 2 1 FIM
#ele começa do 6 e vai até o 1, ou seja, 6,5,4,3,2,1.
#ele conta o 1, pois o 0 não está incluído.
#o -1 é o passo, ou seja, ele vai de 1 em 1, se fosse -2, ele iria de 2 em 2, e assim por diante.

for c in range (0,7,2):
    print(c)
print('FIM')
# Output: 0 2 4 6 FIM
#ele começa do 0 e vai até o 6, ou seja, 0,2,4,6.
#ele conta o 6, pois o 7 não está incluído.
#o 2 é o passo, ou seja, ele vai de 2 em 2.

n=int(input('Digite um número: ')) #ele vai perguntar um número e vai contar até esse número.
for c in range (0,n+1): #o n+1 é para incluir o número digitado.
    print(c)
print('FIM')
# Output: 0 1 2 3 4 5 FIM

i=int(input('Início: ')) #ele vai perguntar o início, o fim e o passo.
f=int(input('Fim: '))
p=int(input('Passo: '))
for c in range (i,f+1,p): #o f+1 é para incluir o número digitado.
    print(c) #ele vai contar de acordo com o início, fim e passo.
print('FIM') #ele vai mostrar o FIM no final.


for c in range (0,3):
    n=int(input('Digite um valor: '))
print('FIM')
#ele vai pedir para digitar um valor 3 vezes.
#ele não vai mostrar os valores digitados, pois não tem print dentro do loop.

s=0
for c in range (0,4):
    n=int(input('Digite um valor: ')) #ele vai pedir para digitar um valor 4 vezes.
    s+=n #ele vai somar os valores digitados.
print('O somatório de todos os valores foi {}'.format(s)) #ele vai mostrar a soma dos valores digitados.
