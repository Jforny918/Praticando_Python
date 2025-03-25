n = soma = 0 
#o n e a soma inicializam com valor 0
while True:
#enquanto o usuário digitar números diferentes de 99
#ele vai continuar enviando a mensagem para digitar um novo número
    n = int (input ('Digite um número: '))
#o comando só parará de ser executado quando o número digitado for 99, pois ele está em break
    if n == 99:
        break
#o break joga para fora da estrutura while e finaliza o programa
    soma += n 
#soma os números inseridos pelo usuário
#print ('A soma vale {}'.format (soma))
print (f'A soma vale {soma}')
#f string é uma forma de utilizar o .format sem precisá-lo digitar inteiro
#somente utilizando no formato que está acima