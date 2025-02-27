a1=float(input('Primeiro segmento: '))
a2=float(input('Segundo segmento: '))
a3=float(input('Terceiro segmento: '))
if a1+a2>a3 and a1+a3>a2 and a2+a3>a1:
    print ('Os segmentos PODEM FORMAR um triângulo!')
    if a1==a2==a3:
        print ('O triângulo é EQUILÁTERO.')
    elif a1!=a2!=a3!=a1:
        print ('O triângulo é ESCALENO.')
    else:
        print ('O triângulo é ISÓSCELES.')
else:   
    print ('Os seguimentos NÃO PODEM FORMAR um triângulo!')