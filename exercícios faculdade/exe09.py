
def fibonacci (n): #funçaõ recursiva 
    if n == 1 or n == 2: #se n for 1 ou 2 irá retornar 1
    #pois os dois primeiros números da sequência são 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    #chamada recursiva da funçaõ, somando os dois números
    #anteriores da sequência

result = int (input ("Digite um número inteiro positivo: ")) 
#input do usuário para escolher qual número da sequência deseja saber
fifi= (fibonacci(result)) #chamada da funçao fibonacci
print (f"O {result}º de Fibonacci é: {fifi}") #exibição no terminal

