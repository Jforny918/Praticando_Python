n = soma = 0 
#inicializam com 0
cont = 1 
#inicializa com 1
while True:
#enquanto o bloco for verdade, ele vai executar o bloco de código abaixo 
    n = int(input('Digite um número: [999 para PARAR] '))
#pedindo para o usuário inserir um valor
    cont += 1 
#contador acrescenta + 1 a cada número digitado
    if n == 999:
#quando o número 999 for digitado, o programa vai parar de ser executado
        break
    soma+= n
#faz a soma dos valores inseridos pelo usuário
print (f'Foram digitados {cont} números e a soma entre eles foi {soma}')
#exibe a soma e a quantidade de números que foram digitados
     