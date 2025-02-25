print ('EXERCÍCIO 04 - CALCULANDO O CUSTO DE VIAGEM POR KM')
print ()
D1=int(input("Qual é a distância da sua viagem em KM? "))
print()
print ('Você está prestes a começar uma viagem de {} Km!'.format(D1))
p1= D1*0.50
p2= D1*0.45
print()
if D1<=200:
    print('O custo da sua passagem será de R${:.2f}'.format(p1))
else: 
    print ('O custo da sua passagem será de R${:.2f}'.format(p2))
    
    