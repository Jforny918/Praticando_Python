print ('EXERCÍCIO 02 - MULTANDO CARROS')
print ()
v1=int(input('Qual a velocidade do seu carro em Km/h? '))
multa=v1*7
if v1>80:
    print ('Você está acima da velocidade permitida e será MULTADO!')
    print ('O valor da sua multa é R${:.12f}!'.format (multa))
else:
    print ('Tenha um excelente dia e dirija com segurança!')