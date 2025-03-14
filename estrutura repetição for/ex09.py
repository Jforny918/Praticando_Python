from datetime import date 
atual = date.today().year #importa a função do módulo datetime e declara a variável atual com o ano atual
totmaior = 0 #declara a variável totmaior com o valor 0
totmenor = 0 #declara a variável totmenor com o valor 0
for pess in range (1, 8): #repete o bloco de instruções 7 vezes
    nasc = int (input ("Digite o ano do seu nascimento: ")) #solicita o ano de nascimento dos 7 usuários
    idade = atual - nasc #calcula a idade atual 
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print ("Ao todo tivemos {} pessoas maiores de idade e {} pessoas menores de idade!".format(totmaior, totmenor)) #imprime a quantidade de pessoas maiores de idade


    