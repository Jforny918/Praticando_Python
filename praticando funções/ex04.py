def area (largura, comprimento):
    area = largura* comprimento
    print (f"A área de um terreno de {largura} x {comprimento} é de {area:.2f} m²")

print ("CONTROLE DE TERRENOS")
print ("="*30)
largura = float (input ("Largura (m): "))
comprimento = float (input ("Comprimento (m): "))
area (largura, comprimento) 
    