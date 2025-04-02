# Tupla de palavras
palavras = ('Andar', 'Correr', 'Pular', 'Comprar', 'Programar', 'Estudar', 
            'Dormir', 'Cantar', 'Falar', 'Brincar', 'Jogar', 'Aprender')

# Loop para percorrer cada palavra
for p in palavras: 
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    # Loop para verificar as vogais
    for letra in 'aeiou': #letra é a variável que vai receber as vogais
        if letra in p.lower():
            print(letra, end=' ')
