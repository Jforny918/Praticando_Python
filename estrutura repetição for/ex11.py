hmaisvelho = 0
nmaisvelho = "" #string vazia
mulheres = 0
soma = 0
mediaidade = 0
for p in range (1, 5):
    print ("----- {}ª PESSOA -----".format(p))
    nome = str (input ("Nome: ")).strip()
    idade = int (input ("Idade: "))
    sexo = str (input ("Sexo [M/F]: ")).strip().upper()
    print (" ")
    soma += idade
    if p == 1 and sexo in "Mm":
        hmaisvelho = idade
        nmaisvelho = nome
    if sexo in "Mm" and idade > hmaisvelho:
        hmaisvelho = idade
        nmaisvelho = nome 
    if sexo in "Ff" and idade < 20:
        mulheres += 1
mediaidade = soma / 4
print ("A média de idade do grupo é de {} anos.".format(mediaidade))
print ("O homem mais velho tem {} anos e se chama {}. ".format (hmaisvelho,nmaisvelho))
print ("Ao todo são {} mulheres com menos de 20 anos ".format(mulheres))
   


