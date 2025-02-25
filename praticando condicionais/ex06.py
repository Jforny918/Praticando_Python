print ('CALCULANDO QUANTAS LIBRAS EU PRECISO LEVAR PARA A MINHA VIAGEM PARA A INGLATERRA')
print()
v1=float(input('Quantos reais eu tenho no momento? '))
print ("Você tem R$ {:.2f} até agora para a sua viagem".format(v1))
v2= v1*0.1375
print ('Então você tem {:.2f} libras.'.format(v2))
if v2<= 900:
    print ('Ainda falta mais um pouquinho se quiser ser feliz rs')
else:
    print ('Agora você está pronta para aproveitar sua viagem')