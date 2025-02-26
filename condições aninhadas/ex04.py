print('Exercíco 04 - Comparando números')
print()
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print()
if n1==n2:
    print('O número {} e o número {} são IGUAIS!'.format(n1, n2))
elif n1<n2:
    print('O número {} é menor que o número {}'.format(n1, n2))
elif n1>n2:
    print('O número {} é maior que o número {}'.format(n1, n2))
