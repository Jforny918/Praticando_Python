sexo = input ("Digite o sexo [M/F]: ").strip().upper() [0] #pega a primeira letra
while sexo not in 'MF': #enquanto o sexo não for M ou F ele irá mostrar a mensagem de erro abaixo
    sexo = input ("Dados inválidos. Por favor, informe seu sexo: ").strip().upper()[0]
if sexo == 'M': #se o sexo digitado for M, netão ele irá mostrar a mensagem abaixo
    print ("Sexo masculino registrado com sucesso!")
else: #senão, ou seja, se o sexo digitado for F, netão ele irá mostrar a mensagem abaixo
    print ("Sexo feminino registrado com sucesso!")
