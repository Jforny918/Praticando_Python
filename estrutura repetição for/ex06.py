#progressão aritmética
a1=int(input('Digite o primeiro termo da PA: ')) #primeiro termo da PA
r=int(input('Digite a razão da PA: ')) #razão da PA
n = int(input('Digite o número de termos da PA: ')) #número de termos da PA
an = a1 + (n-1)*r #fórmula da PA
for c in range (a1, n, an):
    print(c, end=' ')