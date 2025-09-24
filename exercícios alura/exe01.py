def somar (a, b):
    return a +b

try:
    n1= float(input ("Digite o primeiro número: "))
    n2= float (input ("Digite o segundo número: "))


    resultado = somar(n1,n2)
    print(f"A soma é: {resultado}")

except ValueError:
    print("Erro: Digite apenas números válidos!")                           