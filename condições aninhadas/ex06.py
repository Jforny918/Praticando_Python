n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m=(n1+n2)/2
print ('A sua média foi {}'.format(m))
if m<6:
    print ('Você está abaixo da média e será REPROVADO')
elif m>6:
    print ('Você está acima da média e está APROVADO')
else:
    print ('Você está na média e está APROVADO')