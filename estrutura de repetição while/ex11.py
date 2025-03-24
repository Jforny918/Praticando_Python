resp = 'S' 
soma = quant = media = 0
while resp in 'Ss': 
    #enquanto a resposta for igual a S ou s (SIM ou sim) ele vai executar o bloco de código abaixo
    n = int (input ('Digite um número: ')) 
    #ele vai pedir para o usuário informar um número
    soma += n 
    #soma = soma + 1 -> vai somar os valores inseridos
    quant += 1 
    #quant = quant + 2 -> vai somar a quantidade de números que foram digitados
    if quant == 1: 
        #se quantidade de números digitados for igual a 1, então o maior número é o menor número
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resp = input ('Quer continuar? [S/N] ').upper().strip()[0]
media = soma / quant
print ('Você digitou {} números e a média foi {:.2f}.'.format(quant, media))
print ('O MAIOR valor foi {} e o MENOR valor foi {}.'.format (maior, menor))