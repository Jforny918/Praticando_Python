import ast

try:
    lista = [1, 2, 3]
    numero = ast.literal_eval(input("Digite um número: "))
    resultado = lista[numero]
except (ValueError): #o value error é para quando o input não é um número e não pode ser convertid0
    print("Valor inválido! Digite um número inteiro.")
except IndexError: #o index error é para quando o número está fora do intervalo da lista
    print("Índice fora do intervalo da lista.")
except Exception as e: #captura qualquer outro erro que possa ocorrer
    print("Ocorreu um erro inesperado:", str(e))


