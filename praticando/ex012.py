print ('======DESAFIO 12======')
#transformar reais em dólares
#1 dólar = 5.38 reais
n1=float(input('Quantos reais você tem na carteira? '))
d=n1/5.38
print ('Com R${:.2f} você pode comprar US${:.2f}'.format(n1,d))
