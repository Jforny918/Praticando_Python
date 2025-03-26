from random import randint
v = 0
while True:
    usuario = int (input ('Digite um valor de 0 a 10: '))
    computador = randint (0, 11)
    total = usuario + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = input ('Par ou ímpar? [P/I] ').strip().upper()[0]
    print (f'Você jogou {usuario} e o computador jogou {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print ('Você VENCEU!')
            v+= 1
        else:
            print ('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print ('Você VENCEU!')
            v+= 1
        else:
            print ('Você PERDEU!')
            break
        print ('Vamos jogar novamente...')
print (f'Game Over! Você venceu {v} vezes!')

