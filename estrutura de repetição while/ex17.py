while True:
    n = int (input ('DIGITE o número que deseja exibir a TABUADA: '))
    if n <= 0:
        break
    print ('-'*30)
    for c in range (1,11):
        print (f' {n} X {c} = {c*n}')
    print ('-'*30)
print ('Programa de Tabuada ENCERRADO. Volte sempre!')
    
        