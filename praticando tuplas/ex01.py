from time import sleep

# Tupla com os números por extenso
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 
        'dezoito', 'dezenove', 'vinte')

while True:
    # Solicita a entrada do usuário
    n1 = int(input('Digite um número entre 0 e 20: '))
    n2 = int(input('Digite outro número entre 0 e 20: '))
    
    # Verifica se os números estão dentro do intervalo permitido
    if 0 <= n1 <= 20 and 0 <= n2 <= 20:
        break
    print('Tente novamente. ', end='')

# Realiza a soma
num = n1 + n2

# Exibe os resultados
print(f'Você digitou o número {cont[n1]} e o número {cont[n2]}')
print('Realizando a soma dos números...')
sleep(2)
print(f'A soma entre {cont[n1]} e {cont[n2]} é igual a {num}')

#o cont[num] é um tupla que contém os números por extenso